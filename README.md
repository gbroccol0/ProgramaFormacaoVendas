# Formação Comercial — HI Tecnologia

Site estático (HTML/CSS/JS puro, sem build, sem frameworks) com a jornada de
formação do **setor de Vendas** da HI Tecnologia: 10 etapas em ~2 semanas
(cerca de 2 h por dia), com autoestudo e dois encontros com instrutor.

É uma cópia adaptada do site do Suporte Técnico (`Forma-o-HI`): mesma
estrutura, visual, busca, progresso, modo escuro, login e painel ADM. A
diferença principal é que **o material de estudo fica dentro das páginas**
(no suporte, as etapas só linkam PDFs e vídeos no OneDrive/YouTube).

---

## 1. Estrutura de pastas

```
Formacao-Vendas-HI/
├── index.html                ← home: trilha, como funciona, agenda, 10 cards de etapa
├── README.md
├── CLAUDE.md                 ← contexto, decisões e pendências para o Claude Code continuar
├── fontes/                   ← material de origem (originais só leitura + texto extraído); ver fontes/README.md
├── ferramentas/              ← extrator de PDF, gerador das páginas "em produção", testes de navegador
├── .github/workflows/        ← publicar-site.yml: copia o site para o repositório público (GitHub Pages)
├── supabase/
│   └── configuracao.sql      ← tabela progresso_vendas (rodar uma vez no Supabase)
└── Assets/
    ├── etapa.css             ← visual das páginas de etapa (NOVO, compartilhado)
    ├── quiz.js               ← quiz com correção na hora (NOVO)
    ├── responsive.css        ← igual ao do suporte
    ├── tema.js               ← igual ao do suporte (modo escuro)
    ├── busca-conteudo.js     ← igual ao do suporte (só comentários mudaram)
    ├── progresso.js          ← 10 etapas, chave própria no navegador
    ├── conta.js              ← login; tabela progresso_vendas; nomes das 10 etapas
    ├── config-conta.js       ← mesmo projeto Supabase do suporte
    ├── admin.html            ← painel ADM das 10 etapas
    ├── hi_tecnologia.html    ← Etapa 1
    ├── fundamentos.html      ← Etapa 2
    ├── comunicacao.html      ← Etapa 3
    ├── clps.html             ← Etapa 4
    ├── conectividade.html    ← Etapa 5
    ├── ihm_sensores.html     ← Etapa 6
    ├── supervisao.html       ← Etapa 7
    ├── solucoes.html         ← Etapa 8
    ├── conversa_venda.html   ← Etapa 9
    ├── avaliacao_final.html  ← Etapa 10
    └── Files/                ← imagens de produto copiadas do site do suporte
```

## 2. Status das etapas

| Etapa | Título | Arquivo | Status |
|------:|---|---|---|
| 1 | A HI Tecnologia | `hi_tecnologia.html` | **Aprovada** por Gabriel (04/11/2026), depois de 2 revisões |
| 2 | Fundamentos da Automação | `fundamentos.html` | **Aprovada** por Gabriel (04/11/2026) |
| 3 | Comunicação Industrial | `comunicacao.html` | **Aprovada** por Gabriel (05/11/2026) |
| 4 | Linha de CLPs | `clps.html` | Em produção |
| 5 | Gateways, Modem e Rádios | `conectividade.html` | Em produção |
| 6 | IHMs, Sensores e Acessórios | `ihm_sensores.html` | Em produção |
| 7 | Supervisão Local e em Nuvem | `supervisao.html` | Em produção |
| 8 | Soluções e Programas | `solucoes.html` | Em produção |
| 9 | A Conversa de Venda | `conversa_venda.html` | Em produção |
| 10 | Avaliação Final | `avaliacao_final.html` | Em produção |

Uma etapa é produzida por vez e só segue depois da revisão da anterior.

## 3. O que mudou em relação ao site do suporte

- **Progresso separado.** Os dois sites ficam no mesmo domínio do GitHub
  Pages e, por isso, compartilham o `localStorage`. O de vendas usa as chaves
  `formacaoVendasHI.*` (o suporte usa `formacaoHI.*`), então um não apaga nem
  soma o progresso do outro.
- **Mesmo Supabase, outra tabela.** O login (`auth.users`) e a tabela
  `admins` são os do suporte: quem é ADM lá também vê o painel de vendas. O
  progresso vai para `progresso_vendas`.
- **CSS central nas etapas.** As páginas de etapa usam `Assets/etapa.css`
  (o suporte repete o CSS em cada página). Ordem no `<head>`:
  `etapa.css` → `responsive.css` → `tema.js`.
- **Home:** mesmo `<head>`/CSS e mesmo script da home do suporte; mudaram o
  título, o corpo e um bloco de CSS no fim do `<style>` (trilha do hero, rotina,
  agenda, e o título do cabeçalho quebrando linha no celular).

## 4. Antes de publicar

1. **Rodar o SQL.** No mesmo projeto Supabase do suporte: SQL Editor → colar
   `supabase/configuracao.sql` → Run. Enquanto ele não rodar, o login funciona,
   mas o progresso não chega à conta (fica pendente no navegador).
2. **Repositório e publicação:**
   - `gbroccol0/ProgramaFormacaoVendas`, **público** (decisão da equipe em
     04/11/2026, ciente de que `fontes/` e o histórico ficam visíveis).
   - Site em **https://gbroccol0.github.io/ProgramaFormacaoVendas/**.
   - A Action `.github/workflows/publicar-site.yml` publica no GitHub Pages
     **a cada push no `main`** que mexa em `index.html` ou `Assets/` (e pode
     ser rodada à mão em Actions → Publicar site → Run workflow). Só
     `index.html` e `Assets/` vão para o endereço do site.
   - Configuração única: Settings → Pages → Build and deployment → Source:
     **GitHub Actions**.
   - O GitHub Pages diferencia maiúsculas de minúsculas: use os nomes de
     arquivo exatamente como estão.
   - Login: o cadastro pelo site não define endereço de retorno; se o Supabase
     exigir confirmação por e-mail, o link do e-mail leva ao endereço
     configurado no Supabase (o do suporte). Depois de confirmar, o login no
     site de vendas funciona normalmente.
3. **Testar localmente com servidor**, não com duplo clique: aberta como
   `file://`, a busca no conteúdo das etapas não funciona. Na pasta do site:
   `python -m http.server 8000` e abrir `http://localhost:8000`.

## 5. Como escrever uma etapa

Copie o esqueleto de `hi_tecnologia.html` e troque o conteúdo. Componentes
disponíveis (estilo em `etapa.css`):

| Classe | Uso |
|---|---|
| `.objetivos` | "Ao final desta etapa você consegue" + tempo estimado |
| `.sumario` | atalhos para as seções da etapa |
| `.step` + `<h3>` | cada seção do conteúdo; **é o que a busca da home indexa** |
| `.analogia` | caixa "Pense assim" |
| `.na-venda` | caixa "Na venda" (argumento, pergunta de cliente) |
| `.atencao` | caixa "Atenção" (o que não prometer, erro comum) |
| `.confirmar` | etiqueta `[CONFIRMAR]` para dado ainda não confirmado |
| `.tabela` | tabela com rolagem horizontal no celular |
| `.cartoes` / `.cartao` | grade de cartões (segmentos, perfis, produtos) |
| `.linha-tempo` | lista de marcos com ano |
| `.glossario` | `<dl>` de termos |
| `.diagrama` | SVG inline com cores que seguem o modo escuro. Classes internas: `d-titulo`, `d-caixa`, `d-rotulo`, `d-itens`, `d-seta`/`d-ponta`, `d-nota`, `d-cheio` (preenchimento laranja), `d-linha` (guia tracejada), `d-texto-claro` (texto branco sobre o laranja) |
| `.diagrama-corpo` | junto com `.diagrama`, para um SVG no meio do texto de uma seção (centralizado, com margem) |
| `.quiz-bloco` + `form.quiz` | quiz; marcação descrita no topo de `quiz.js` |
| `.caso` | preparação para o encontro com o instrutor |
| `.fonte` | página das fontes de onde saiu cada dado |

Regras de conteúdo:
- Toda informação de produto, cliente ou número vem das fontes (Catálogo
  Geral, Treinamento de Produto, apresentação de CLPs) com a página citada em
  `.fonte`. O que não tem fonte vai como `[CONFIRMAR]`.
- **Sem preços.** O programa explica como cada produto é cobrado (licença,
  plano, quantidade de dados); o valor sai do orçamento do setor de vendas.
- Páginas do catálogo citadas pela numeração **impressa** (uma a menos que a
  numeração do PDF).

## 6. Pendências de conteúdo `[CONFIRMAR]`

Dúvidas que ainda dependem da equipe. Cada uma aparece em amarelo na página
onde está.

| Onde | O que confirmar |
|---|---|
| Etapa 1, item 4 | Clientes de referência de Energia, Indústria 4.0, Meio ambiente, Hospitalar e Predial (Gabriel vai levantar com a equipe) |
| Etapa 1, item 5 | Qual representante (TBC Automação, 4Sys Sistemas) cobre cada região (Gabriel vai levantar) |
| Etapa 1, item 4 | Texto das áreas Indústria 4.0, Meio Ambiente, Hospitalar e Energia (catálogo p. 3–4, ilegível na extração; um print resolve) |
| Etapa 3, item 5 | Em que situações o vendedor precisa citar o SCP-HI (entre quais equipamentos e softwares HI ele é usado); as fontes só dizem que é o protocolo proprietário da HI |
| Etapa 5 (futura) | Alcance rural do R9X307: 60 km (catálogo) ou 105 km (Treinamento de Produto) |
| Etapa 5 (futura) | Nome do conversor: "GTON C SET" (Treinamento) ou "GTON-C" (catálogo) |
| Etapa 5 (futura) | ESC717/ESC713 entram na formação de vendas? (estão no site do suporte, não no catálogo) |
| Etapa 6 (futura) | MMI700 ainda é vendida? BPU508 ainda é vendida (o catálogo traz a SBC513)? |
| Etapa 9 (futura) | Processo comercial (orçamento, prazo, garantia) e regras para acionar suporte/engenharia |
| Etapa 9 (futura) | Cases reais (problema → solução → resultado); Gabriel ofereceu compartilhar |
| Fase 4 | Lista dos vídeos/tutoriais do suporte reaproveitáveis (começar pelos links do site Forma-o-HI) |
