"""Gera as páginas "em produção" das Etapas 2 a 10 da Formação Comercial HI.

Uso: python -I gerar_etapas.py <pasta Assets do site de vendas>
Não sobrescreve página que já exista (etapa já produzida).
"""
import html, os, sys

ASSETS = sys.argv[1]

ETAPAS = [
    None,
    ("hi_tecnologia.html", "A HI Tecnologia", None, None, None, None, None),
    ("fundamentos.html", "Fundamentos da Automação",
     "Fundamentos da automação para quem vende",
     "O mínimo de técnica para entender o cliente industrial e não prometer o que não existe.",
     ["explicar com analogias o que é um processo industrial, um sensor, um atuador e um CLP;",
      "diferenciar alimentação AC e DC e saber por que o cliente escolhe uma ou outra;",
      "explicar sinais digitais (liga/desliga) e analógicos (0 a 100% de uma medida);",
      "situar cada produto HI na pirâmide da automação: campo, controle, supervisão e nuvem."],
     "2h30", "Treinamento de Produto, p. 3 a 5; apresentação de CLPs (slides 1 e 2)."),
    ("comunicacao.html", "Comunicação Industrial",
     "Comunicação industrial: meios físicos e protocolos",
     "A \"linha telefônica\" e o \"idioma\" que os equipamentos precisam ter em comum.",
     ["escolher entre RS232, RS485, Ethernet, Wi-Fi, rádio e 4G a partir de três perguntas: quantos equipamentos, a que distância e se há internet;",
      "explicar Modbus, MQTT, ASCII e SCP-HI como \"idiomas\" da automação;",
      "perceber, na conversa, quando o cliente precisa de um conversor ou gateway."],
     "2h", "Treinamento de Produto, p. 4; apresentação de CLPs (slide 3)."),
    ("clps.html", "Linha de CLPs",
     "Linha de CLPs: RION5, NEON5 e P7C",
     "Qual controlador indicar, pelo tamanho da aplicação e pelo que o cliente precisa conectar.",
     ["indicar RION5, NEON5 ou P7C pela quantidade de pontos de I/O, alimentação, SD Card e conectividade;",
      "explicar o uso do RION5 como I/O remoto de um NEON5;",
      "falar dos módulos de I/O sem entrar em ficha técnica;",
      "apresentar o HIstudio, o software de programação gratuito."],
     "2h30", "Treinamento de Produto, p. 5 a 9; Catálogo Geral, p. 6 a 10 e 32; apresentação de CLPs."),
    ("conectividade.html", "Gateways, Modem e Rádios",
     "Gateways, conversores, modem e rádios",
     "Como conectar o que o cliente já tem, sem trocar o equipamento, e como levar os dados longe.",
     ["reconhecer quando o cliente precisa só traduzir uma rede (GTON-C), adicionar inteligência (GTON-P), chegar à internet (GTON-M) ou ligar o computador (USB721);",
      "explicar quando o rádio integrado ao CLP basta e quando indicar o R9X307;",
      "conduzir a venda de rádio: visada, coordenadas em KML e estudo de altimetria pela Engenharia de Produto."],
     "2h30", "Treinamento de Produto, p. 11 a 16; Catálogo Geral, p. 15 a 22."),
    ("ihm_sensores.html", "IHMs, Sensores e Acessórios",
     "IHMs, sensores, fontes e acessórios",
     "O que completa o painel e aumenta o valor do pedido.",
     ["diferenciar a IHM (operar a máquina no painel) do supervisório (enxergar a planta inteira);",
      "apresentar a IHM GTI5, a linha própria da HI;",
      "citar os sensores THT863 e HPS850 e onde se usam;",
      "oferecer fonte, caixa GEM100 e kit RTK510 como complemento da solução."],
     "1h30", "Treinamento de Produto, p. 10, 17 e 18; Catálogo Geral, p. 11 a 14 e 23 a 28."),
    ("supervisao.html", "Supervisão Local e em Nuvem",
     "Supervisão: HIscada Pro × Portal de Telemetria",
     "Enxergar o processo na planta ou de qualquer lugar: como escolher e como se cobra cada um.",
     ["decidir entre HIscada Pro + MPL Server (rede local) e Portal de Telemetria (navegador, de qualquer lugar);",
      "explicar como cada um é licenciado: HIscada por tags e por quantidade de computadores, Portal por plano e quantidade de dados;",
      "saber que equipamento Modbus de outro fabricante exige licença do MPL Server;",
      "oferecer o HI Connect para fechar a solução IoT completa."],
     "2h30", "Treinamento de Produto, p. 19 a 23; Catálogo Geral, p. 29 a 33 e 38."),
    ("solucoes.html", "Soluções e Programas",
     "Soluções dedicadas e programas",
     "Soluções prontas da HI e os programas para parceiros, fabricantes e alunos.",
     ["apresentar o painel de aquisição de dados DAP5;",
      "apresentar a solução de óleo e gás (bombeio mecânico e HI OilTools);",
      "identificar quando o cliente é candidato a HI OEM, HI Partner ou HI University."],
     "1h30", "Catálogo Geral, p. 34 a 42."),
    ("conversa_venda.html", "A Conversa de Venda",
     "A conversa de venda",
     "Juntar tudo: qualificar o cliente, desenhar a solução e saber quando chamar o suporte ou a engenharia.",
     ["conduzir um roteiro de perguntas de qualificação;",
      "montar as arquiteturas típicas \"do sensor à nuvem\" com produtos HI;",
      "aplicar a lista do que não prometer;",
      "saber quando e como acionar o suporte técnico e a engenharia."],
     "2h30", "Todas as etapas anteriores e as orientações do setor de vendas."),
    ("avaliacao_final.html", "Avaliação Final",
     "Avaliação final",
     "Um atendimento completo, do primeiro contato à indicação da solução.",
     ["responder a avaliação final do programa;",
      "atender um cliente simulado pelo instrutor (role-play), do primeiro contato até a solução indicada."],
     "1h", "Todas as etapas."),
]

MOLDE = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>Formação Comercial HI Tecnologia - {nome}</title>

    <link rel="stylesheet" href="etapa.css">
    <link rel="stylesheet" href="responsive.css">
    <script src="tema.js"></script>
</head>
<body class="pagina-interna">

    <header>
        <h2>HI Tecnologia</h2>
    </header>

    <section class="hero">
        <div class="hero-content">
            <span class="etapa-badge">Etapa {n} de 10</span>
            <h1>{titulo}</h1>
            <p><strong>{chamada}</strong></p>
        </div>
    </section>

    <section class="section" style="background-color: var(--cinza-claro);">
        <h2 class="section-title">Formação Comercial HI Tecnologia</h2>

        <div class="training-container">
            <h2>Etapa {n} - {nome}</h2>

            <div class="objetivos">
                <h3>Ao final desta etapa você consegue:</h3>
                <ul>
{objetivos}
                </ul>
                <p class="tempo">Tempo estimado: {tempo}.</p>
            </div>

            <div class="em-producao">
                <strong>Conteúdo em produção</strong>
                Esta etapa está sendo escrita e entra no ar depois da revisão da etapa anterior.
            </div>

            <p class="fonte">Fontes previstas: {fontes}</p>
        </div>
    </section>

    <div class="etapa-nav">
        <div class="etapa-concluir">
            <button type="button" class="btn btn-concluir" data-etapa="{n}" aria-pressed="false">Marcar etapa como concluída</button>
        </div>
        <a href="../index.html" class="btn">Voltar</a>
        <a href="{anterior_arq}" class="btn btn-etapa">← Etapa {n_ant}: {anterior_nome}</a>
{proxima}
    </div>

    <footer>
        <p>Copyright © HI Tecnologia Automação Industrial. Todos os direitos reservados.</p>
    </footer>

    <script src="progresso.js"></script>
    <script src="config-conta.js"></script>
    <script src="conta.js"></script>
</body>
</html>
"""

e = html.escape
for n in range(2, 11):
    arq, nome, titulo, chamada, objetivos, tempo, fontes = ETAPAS[n]
    destino = os.path.join(ASSETS, arq)
    if os.path.exists(destino):
        print("mantida (já existe):", arq)
        continue
    ant = ETAPAS[n - 1]
    if n < 10:
        prox = ETAPAS[n + 1]
        proxima = '        <a href="%s" class="btn btn-etapa">Etapa %d: %s →</a>' % (prox[0], n + 1, e(prox[1]))
    else:
        proxima = ""
    pagina = MOLDE.format(
        n=n, nome=e(nome), titulo=e(titulo), chamada=e(chamada),
        objetivos="\n".join("                    <li>%s</li>" % e(o) for o in objetivos),
        tempo=tempo, fontes=e(fontes),
        anterior_arq=ant[0], n_ant=n - 1, anterior_nome=e(ant[1]), proxima=proxima)
    with open(destino, "w", encoding="utf-8", newline="\n") as f:
        f.write(pagina)
    print("criada:", arq)
