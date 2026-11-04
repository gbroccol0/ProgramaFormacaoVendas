"""Extrai o texto de TODAS as paginas de um PDF, linha a linha (agrupa trechos pela posicao y).

Uso: python3 -I pdf_texto.py arquivo.pdf [deslocamento] > saida.txt
Somente leitura; biblioteca padrao. Cada pagina sai como "===== PDF p. N =====".
Com deslocamento (ex.: 1 para o Catalogo Geral, cuja capa nao e numerada), acrescenta
"(impressa N-deslocamento)", que e a numeracao a citar nas paginas do site.
"""
import re, zlib, sys
sys.stdout.reconfigure(encoding='utf-8', errors='replace')
path = sys.argv[1]; desl = int(sys.argv[2]) if len(sys.argv) > 2 else 0
data = open(path, 'rb').read()
WS = b' \t\r\n\x0c\x00'; DL = b'()<>[]{}/%'

class Ref:
    __slots__ = ('n',)
    def __init__(s, n): s.n = n
class Op(str): pass
class Name(str): pass

def skip(b, i):
    n = len(b)
    while i < n:
        c = b[i]
        if c in WS: i += 1
        elif c == 37:
            while i < n and b[i] not in (10, 13): i += 1
        else: break
    return i

def rend(b, i):
    n = len(b)
    while i < n and b[i] not in WS and b[i] not in DL: i += 1
    return i

numre = re.compile(rb'[+-]?(\d+\.?\d*|\.\d+)$')
refre = re.compile(rb'\s+(\d+)\s+R(?=[\s/<>\[\]()%]|$)')
ESC = {110: 10, 114: 13, 116: 9, 98: 8, 102: 12}

def parse(b, i):
    i = skip(b, i); c = b[i:i+1]
    if b[i:i+2] == b'<<':
        i += 2; d = {}
        while True:
            i = skip(b, i)
            if i >= len(b): return d, i
            if b[i:i+2] == b'>>': return d, i+2
            k, i = parse(b, i); v, i = parse(b, i); d[k] = v
    if c == b'[':
        i += 1; a = []
        while True:
            i = skip(b, i)
            if i >= len(b): return a, i
            if b[i:i+1] == b']': return a, i+1
            v, i = parse(b, i); a.append(v)
    if c == b'/':
        j = rend(b, i+1); return Name(b[i+1:j].decode('latin-1')), j
    if c == b'(':
        i += 1; dp = 1; out = bytearray(); n = len(b)
        while i < n:
            ch = b[i]
            if ch == 92:
                i += 1; e = b[i]
                if e in ESC: out.append(ESC[e]); i += 1
                elif 48 <= e <= 55:
                    j = i
                    while j < i+3 and j < n and 48 <= b[j] <= 55: j += 1
                    out.append(int(b[i:j], 8) & 255); i = j
                elif e in (10, 13):
                    i += 1
                    if e == 13 and i < n and b[i] == 10: i += 1
                else: out.append(e); i += 1
                continue
            if ch == 40: dp += 1
            elif ch == 41:
                dp -= 1
                if dp == 0: return bytes(out), i+1
            out.append(ch); i += 1
        return bytes(out), i
    if c == b'<':
        j = b.index(b'>', i); h = re.sub(rb'\s', b'', b[i+1:j])
        if len(h) % 2: h += b'0'
        return bytes.fromhex(h.decode()), j+1
    j = rend(b, i)
    if j == i: return Op(b[i:i+1].decode('latin-1')), i+1
    t = b[i:j]
    if numre.match(t):
        if b'.' not in t:
            m = refre.match(b[j:j+30])
            if m: return Ref(int(t)), j+m.end()
            return int(t), j
        return float(t), j
    return Op(t.decode('latin-1')), j

objs = {}
def R(v):
    for _ in range(20):
        if isinstance(v, Ref): v = objs.get(v.n, (None, None))[0]
        else: break
    return v

def flate(d, raw):
    f = R(d.get('Filter')); fl = f if isinstance(f, list) else ([f] if f else [])
    out = raw
    for x in fl:
        if R(x) == 'FlateDecode':
            try: out = zlib.decompressobj().decompress(out)
            except Exception: return None
        else: return None
    return out

skipto = 0
for m in re.finditer(rb'(\d+)\s+(\d+)\s+obj\b', data):
    if m.start() < skipto: continue
    num = int(m.group(1)); i = m.end()
    try: v, i = parse(data, i)
    except Exception: continue
    i = skip(data, i); st = None
    if isinstance(v, dict) and data[i:i+6] == b'stream':
        i += 6
        if data[i:i+2] == b'\r\n': i += 2
        elif data[i:i+1] in (b'\n', b'\r'): i += 1
        L = v.get('Length')
        if isinstance(L, int) and data.find(b'endstream', i+L, i+L+40) >= 0: st = data[i:i+L]
        else:
            e = data.find(b'endstream', i); st = data[i:e]
        skipto = i + len(st)
    objs[num] = (v, st)
for num, (v, st) in list(objs.items()):
    if isinstance(v, dict) and v.get('Type') == 'ObjStm' and st is not None:
        u = flate(v, st)
        if not u: continue
        F = v['First']; h = u[:F].split()
        for k in range(v['N']):
            on = int(h[2*k]); off = int(h[2*k+1])
            try: val, _ = parse(u, F+off)
            except Exception: continue
            if on not in objs: objs[on] = (val, None)

def S(v):
    if isinstance(v, Ref):
        d, st = objs.get(v.n, (None, None))
        if st is None or not isinstance(d, dict): return None
        return flate(d, st)

def d16(b): return b.decode('utf-16-be', 'replace')
cmc = {}
def cmap(ref):
    if not isinstance(ref, Ref): return None
    if ref.n in cmc: return cmc[ref.n]
    u = S(ref); res = None
    if u:
        mp = {}; w = 1
        for a in re.finditer(rb'begincodespacerange(.*?)endcodespacerange', u, re.S):
            hs = re.findall(rb'<([0-9A-Fa-f]+)>', a.group(1))
            if hs: w = len(hs[0]) // 2
        for a in re.finditer(rb'beginbfchar(.*?)endbfchar', u, re.S):
            for s, d in re.findall(rb'<([0-9A-Fa-f]+)>\s*<([0-9A-Fa-f]*)>', a.group(1)):
                mp[int(s, 16)] = d16(bytes.fromhex(d.decode()))
        for a in re.finditer(rb'beginbfrange(.*?)endbfrange', u, re.S):
            for lo, hi, rest in re.findall(rb'<([0-9A-Fa-f]+)>\s*<([0-9A-Fa-f]+)>\s*(<[0-9A-Fa-f]*>|\[[^\]]*\])', a.group(1)):
                lo = int(lo, 16); hi = int(hi, 16)
                if rest[:1] == b'[':
                    for k, dd in enumerate(re.findall(rb'<([0-9A-Fa-f]*)>', rest)): mp[lo+k] = d16(bytes.fromhex(dd.decode()))
                else:
                    base = bytes.fromhex(rest[1:-1].decode()); bv = int.from_bytes(base, 'big')
                    for k in range(min(hi-lo+1, 65536)): mp[lo+k] = d16((bv+k).to_bytes(len(base), 'big'))
        res = (w, mp)
    cmc[ref.n] = res; return res

def fdec(fd):
    fd = R(fd)
    if not isinstance(fd, dict): return lambda s: s.decode('cp1252', 'replace')
    cm = cmap(fd.get('ToUnicode'))
    if cm:
        w, mp = cm
        return lambda s: ''.join(mp.get(int.from_bytes(s[k:k+w], 'big'), '' if w == 2 else chr(s[k])) for k in range(0, len(s)-w+1, w))
    return lambda s: s.decode('cp1252', 'replace')

def mul(a, b):
    return [a[0]*b[0]+a[1]*b[2], a[0]*b[1]+a[1]*b[3], a[2]*b[0]+a[3]*b[2], a[2]*b[1]+a[3]*b[3],
            a[4]*b[0]+a[5]*b[2]+b[4], a[4]*b[1]+a[5]*b[3]+b[5]]

EIre = re.compile(rb'\sEI\s')
items = []
def run(c, res, ctm, depth=0):
    res = R(res) or {}; fonts = R(res.get('Font')) or {}; xo = R(res.get('XObject')) or {}
    dec = lambda s: s.decode('cp1252', 'replace'); decs = {}
    st = []; i = 0; n = len(c); stack = []
    tm = [1, 0, 0, 1, 0, 0]; tlm = tm[:]; lead = 0
    def emit(s):
        m = mul(tm, ctm)
        if s.strip(): items.append((round(m[5]), round(m[4]), s))
    while True:
        i = skip(c, i)
        if i >= n: break
        try: t, i = parse(c, i)
        except Exception:
            i += 1; continue
        if not isinstance(t, Op):
            st.append(t); continue
        op = str(t); nums = [x for x in st if isinstance(x, (int, float))]
        if op == 'q': stack.append(ctm[:])
        elif op == 'Q' and stack: ctm = stack.pop()
        elif op == 'cm' and len(nums) >= 6: ctm = mul(nums[-6:], ctm)
        elif op == 'BT': tm = [1, 0, 0, 1, 0, 0]; tlm = tm[:]
        elif op == 'Tm' and len(nums) >= 6: tm = nums[-6:]; tlm = tm[:]
        elif op in ('Td', 'TD') and len(nums) >= 2:
            tlm = mul([1, 0, 0, 1, nums[-2], nums[-1]], tlm); tm = tlm[:]
            if op == 'TD': lead = -nums[-1]
        elif op == 'TL' and nums: lead = nums[-1]
        elif op == 'T*': tlm = mul([1, 0, 0, 1, 0, -lead], tlm); tm = tlm[:]
        elif op == 'BI':
            m = EIre.search(c, i); i = m.end() if m else n
        elif op == 'Tf' and len(st) >= 2:
            nm = st[-2]
            if nm not in decs: decs[nm] = fdec(fonts.get(nm))
            dec = decs[nm]
        elif op == 'Tj' and st and isinstance(st[-1], bytes): emit(dec(st[-1]))
        elif op == 'TJ' and st and isinstance(st[-1], list):
            emit(''.join(dec(e) if isinstance(e, bytes) else (' ' if isinstance(e, (int, float)) and e < -180 else '') for e in st[-1]))
        elif op == 'Do' and st and isinstance(st[-1], Name) and depth < 8:
            x = xo.get(st[-1]); xd = R(x)
            if isinstance(xd, dict) and xd.get('Subtype') == 'Form':
                u = S(x)
                if u:
                    mtx = xd.get('Matrix') or [1, 0, 0, 1, 0, 0]
                    run(u, xd.get('Resources') or res, mul(mtx, ctm), depth+1)
        st = []

cat = None
for num, (v, s) in objs.items():
    if isinstance(v, dict) and v.get('Type') == 'Catalog': cat = v
pages = []
def walk(node, inh):
    node = R(node)
    if not isinstance(node, dict): return
    r = node.get('Resources', inh)
    if 'Kids' in node:
        for k in R(node.get('Kids')) or []: walk(k, r)
    else: pages.append((node, r))
walk(cat.get('Pages'), None)

def juntar(trechos):
    """Junta os trechos de uma linha. Fontes com kerning partem palavras em varios
    trechos ("of" "er" "ece"); estima a largura media do caractere pela propria linha
    e so poe espaco quando a distancia ate o proximo trecho passa do tamanho do anterior."""
    razoes = sorted((x2 - x1) / len(s1) for (x1, s1), (x2, s2) in zip(trechos, trechos[1:])
                    if len(s1.rstrip()) >= 1 and x2 > x1)
    cw = razoes[len(razoes) // 4] if razoes else 0
    out = trechos[0][1] if trechos else ''
    for (x1, s1), (x2, s2) in zip(trechos, trechos[1:]):
        if cw and (x2 - x1) <= len(s1) * cw * 1.25 + 0.5:
            out += s2
        else:
            out = out.rstrip() + ' ' + s2.lstrip()
    return re.sub(r' {2,}', ' ', out).strip()

for pno, (pg, res) in enumerate(pages, 1):
    items.clear()
    cs = pg.get('Contents')
    if not isinstance(cs, Ref): cs = R(cs)
    refs = cs if isinstance(cs, list) else [cs]
    c = b'\n'.join(filter(None, (S(r) for r in refs)))
    run(c, res, [1, 0, 0, 1, 0, 0])
    print('\n===== PDF p. %d%s =====' % (pno, ' (impressa %d)' % (pno - desl) if desl else ''))
    linhas = {}
    for y, x, s in items:
        chave = next((k for k in linhas if abs(k - y) <= 2), y)
        linhas.setdefault(chave, []).append((x, s))
    for y in sorted(linhas, reverse=True):
        print(juntar(sorted(linhas[y])))
