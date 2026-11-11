# Formação Comercial HI Tecnologia — passagem para o Claude Code

Contexto para continuar o trabalho. **Leia inteiro antes de mexer em qualquer
arquivo.** Responda sempre em **português do Brasil**.

Este arquivo foi escrito em 04/11/2026, quando o trabalho saiu do computador de
Gabriel (Claude Code local, VS Code no Windows) para o Claude Code na nuvem.
Tudo o que foi decidido até aqui está registrado abaixo; a conversa original não
vem junto.

---

## 1. Quem pediu e o que é

**Gabriel** trabalha no **suporte técnico da HI Tecnologia** (Campinas), que
fabrica CLPs, gateways, conversores, rádios e softwares de programação,
supervisão SCADA e supervisão em nuvem. O suporte tem um programa de formação
para novos colaboradores (o site `Forma-o-HI`); os outros setores não têm.

**Objetivo:** um programa de formação para o **setor de Vendas (B2B)** que leve
um colaborador **sem formação técnica** até o ponto em que ele consiga:
- explicar o que é automação industrial e onde a HI se encaixa;
- entender os problemas que cada linha de produto resolve e para que cliente;
- conduzir uma conversa comercial inicial, identificar necessidades e indicar
  a solução adequada;
- saber quando acionar o suporte técnico ou a engenharia.

O foco é **compreensão aplicada à venda**, não formação técnica. Profundidade
técnica só entra quando ajuda a vender ou a **não prometer o que o produto não
faz**.

Gabriel conhece bem a parte técnica, mas o leitor final do conteúdo é o
vendedor leigo. Gabriel gosta de entender o porquê das decisões.

## 2. Regras que não mudam

1. **Só informação das fontes.** Não inventar especificação, modelo,
   funcionalidade, cliente ou número. Faltou → etiqueta `[CONFIRMAR]` na página
   (classe `.confirmar`, aparece em amarelo) **e** linha na tabela de
   pendências do `README.md`.
   - **Exceção aprovada:** conceitos **gerais** de automação (o que é sensor,
     processo industrial, pirâmide da automação, IoT) e analogias podem vir de
     conhecimento geral. Tudo o que é **da HI** (modelos, specs, clientes,
     prazos) só com fonte.
2. **Não alterar nem apagar os originais** em `fontes/originais/`.
3. **Tudo em português do Brasil.**
4. **Sem preços.** Gabriel é do suporte e não tem os valores; eles variam por
   tipo de venda, comissão, produto etc. e saem das planilhas do setor de
   vendas. O programa ensina **como o preço se forma** (licença do HIscada por
   tags e viewers, plano do Portal por quantidade de dados, licença do MPL
   Server para equipamento de terceiros) e manda o vendedor para o orçamento.
   Nunca escrever valor em R$, nem "mais barato/econômico" sem fonte.
5. **Uma etapa por vez, com aprovação de Gabriel entre elas.** Entregar a
   etapa, esperar o retorno dele, aplicar as correções, só então seguir.
6. **Citar a fonte de cada dado** de produto/cliente num `<p class="fonte">`
   no fim da seção. Catálogo: página **impressa** (= página do PDF − 1).
   Treinamento: página do PDF.
7. **Não alterar o site do suporte** (`Otavio7w7/Forma-o-HI`). Ele é só modelo.
8. **As três regras de ouro** da home valem para todo o conteúdo e **nenhum
   quiz, caso ou texto pode contradizê-las**:
   - **Não invente.** Não sabe? Anote e confirme com a equipe.
   - **Preço só pelo orçamento.** Nada de "preço de cabeça".
   - **Na dúvida técnica, chame o suporte.** Não prometa compatibilidade,
     alcance ou recurso sem confirmação.

### Metodologia "Explicar o porquê" (do `fontes/originais/CONTEXT.txt`, obrigatória)
- **Traduzir "tecniquês" em função prática.** Nunca citar sigla ou recurso
  solto; dizer para que serve. Exemplos canônicos: RS232 = liga **dois**
  equipamentos ponto a ponto; RS485 = **vários** equipamentos na mesma rede,
  **até 32 (1 mestre + 31 escravos)**; meio físico = "linha telefônica", protocolo =
  "idioma"; sinal analógico (0–10 V, 4–20 mA) = **0 a 100 %** da grandeza
  física (o CLP não sabe o que é "litro", lê a porcentagem).
- **Regra de bolso comercial:** cada etapa ensina **quais perguntas fazer ao
  cliente** para escolher o produto certo.
- **Apoio visual:** diagrama (SVG inline, classe `.diagrama`) ou foto do
  produto sempre que o texto falar de um equipamento ou arquitetura.
- **Pouca profundidade técnica (Gabriel, 05/11/2026).** O público não é
  técnico; o foco é o que cada equipamento faz e o ecossistema da HI.
  Conceitos gerais com número entram (ex.: RS485 = até 32 equipamentos);
  detalhe de funcionamento não (como o mestre pergunta e o escravo responde,
  "zero vivo" do 4–20 mA, A/D, OPC por dentro, linguagem de script, código
  de modelo de fonte, resolução de tela, tipo de touch, efeito Hall, chip Nano
  SIM, conector SMA, DigiMesh, XBee, TS35, completação dupla...). Na dúvida,
  perguntar: "o vendedor precisa disso para indicar o produto ou para não
  prometer errado?" Se não, sai.
- **Não afunilar.** Frases categóricas que um aprendiz leva como regra
  (ex.: "rádio é para campo aberto") só com fonte e quando forem verdade
  sempre. Rádio funciona de distâncias curtas (inclusive ambiente fechado) a
  longas; visada é exigência das longas distâncias.
- **Alimentação:** escrever "alimentado pela rede elétrica" (ou "direto da
  rede"), nunca "ligar o CLP na tomada". "Tomada" só em analogia.

## 3. Decisões tomadas por Gabriel (histórico)

**29/10/2026 — Fase 1 (diagnóstico) e escolhas iniciais**
- Aplicação **mista**: autoestudo + encontros com instrutor (casos, role-play).
- Duração: **2 semanas, ~2 h/dia (~20 h)**.
- Conceitos gerais podem vir de conhecimento geral (ver regra 1).
- O formato inicial (Markdown + player HTML com voz do navegador) foi
  **abandonado**: "a narração ficou horrível".

**29/10/2026 — formato atual**
- **Site separado com a mesma estrutura do site do suporte** (home com cards de
  etapa, busca, progresso, modo escuro, login, painel ADM). Motivo: manter um
  padrão no programa de formação. Juntar as duas trilhas no mesmo site
  misturaria o progresso.
- **Só texto por enquanto** (sem vídeo nem áudio).
- **Mesmo Supabase do suporte, tabela nova** `progresso_vendas`.
- **Quiz na própria página**, com correção na hora e explicação; o estudo de
  caso fica para o encontro com o instrutor.
- A pasta `saida/` prevista no prompt original foi **substituída pelo site**.

**29/10/2026 — revisão da Etapa 1**
- **IHM:** Weintek e Veichi **seguem na revenda**, mas a preferência é ofertar a
  **GTI5** (linha própria).
- **"Startup", não "turnkey"**: é o dialeto interno para projeto entregue
  completo e funcionando. O glossário explica que o catálogo usa "turnkey".
- **Quiz sem perguntas que sugiram que a HI não atende um setor.** Exemplo que
  saiu: "qual setor NÃO aparece no catálogo? → Mineração" (a HI tem clientes de
  mineração, só não estão no catálogo). Segmentos do catálogo = "em destaque,
  não todos".
- **Quiz não pode cruzar com as regras de ouro** (Gabriel achou que a Q7 dava
  "preço de cabeça" como certo; o gabarito já era o certo, a confusão era
  visual). Daí as etiquetas explícitas na correção ("✓ Resposta certa",
  "✓ Sua resposta está certa", "✗ Sua resposta").

**Entre 29/10 e 04/11/2026 — correção da GTI5 (segunda revisão da Etapa 1)**
- O software da GTI5 é o **SmartManagerPro**, **muito parecido** com o
  EasyBuilderPro da Weintek (**não é o mesmo** software). Argumento de venda:
  quem já programa Weintek se adapta rápido.
- Recursos da Weintek: **não existe lista fixa** do que a GTI5 tem ou não. O
  vendedor **pergunta ao cliente** quais recursos ele usa e **confirma com o
  suporte interno** se a GTI5 atende. Não prometer compatibilidade antes.

**04/11/2026 — Etapa 1 aprovada; trabalho passa para a nuvem**
- Gabriel retestou a Etapa 1 depois da correção da GTI5 e **aprovou**.
- As duas pendências cobradas (clientes de referência de Energia, Indústria
  4.0, Meio Ambiente, Hospitalar e Predial; região de cada representante)
  **ainda não chegaram**: seguem como `[CONFIRMAR]`. Continuar cobrando.
- Fluxo de publicação: cada etapa numa **branch** com **pull request**;
  Gabriel revisa, aprova e faz o merge; depois do merge, conferir a Action
  "Publicar site" e mandar o link da etapa publicada.

**04/11/2026 — Etapa 2 aprovada**
- Gabriel aprovou a Etapa 2 sem correções ("se pegarmos algum erro
  posteriormente, alteramos"). Ele faz o merge do PR; liberou a Etapa 3.

**05/11/2026 — Etapa 3 aprovada**
- Gabriel respondeu "pode continuar" (mesmo sentido da Etapa 2: aprovada; ele
  faz o merge). Os pontos abertos no PR #2 ficaram como estavam: a tabela de
  distâncias de referência geral fica, o rádio segue sem número de alcance e
  o fabricante do CLP do exercício 18 fica anônimo.

**05/11/2026 — Etapa 4 aprovada; produção em sequência**
- Gabriel aprovou a Etapa 4 ("pode continuar") e pediu para **seguir
  produzindo as próximas etapas em sequência, sem esperar aprovação entre
  elas**, usando os créditos disponíveis; correções virão depois, numa revisão
  geral. Continua valendo uma branch e um PR por etapa.
- Respostas sobre a Etapa 5:
  - **R9X307: a HI recomenda até 60 km** (o 105 km da tabela do Treinamento é
    valor técnico de referência; ensinar 60 km).
  - **ESC717/ESC713 não são o "Plug Telemetria"** (o `CONTEXT.txt` estava
    errado). Entram na formação só para explicar que **os ESC são os
    antecessores dos GTON**.
  - **"GTON C SET" e "GTON-C" são o mesmo equipamento**; SET = Serial
    Ethernet. Outros equipamentos seguem o mesmo padrão, por exemplo
    **S4E = Serial 485 Ethernet**.

**05/11/2026 — revisão de Gabriel lendo as Etapas 2 a 9 (no VS Code)**
- **IHM também está na supervisão**, não só no controle: aparece nos dois
  níveis da pirâmide (Etapa 2) e no mapa de camadas da Etapa 1. A diferença
  para o supervisório é o alcance (a máquina × a planta inteira), não "operar
  × supervisionar".
- **RS485: até 32 equipamentos (1 mestre + 31 escravos).** Sem explicar como
  o mestre funciona.
- **Estudo de altimetria/visada do rádio: suporte técnico ou engenharia de
  aplicação**, não a Engenharia de Produto (o Treinamento p. 16 diz
  Engenharia de Produto; vale o que Gabriel disse). A Engenharia de Produto
  desenvolve os produtos e atende demandas internas; **demanda técnica
  externa (de cliente) vai ao suporte técnico ou à engenharia de aplicação.**
- Mais as três regras de redação acrescentadas à metodologia (seção 2):
  pouca profundidade técnica, não afunilar, "alimentado pela rede elétrica".
- Aplicado em todas as etapas, cada correção na branch da sua etapa e
  levada adiante por merge (2 → 3 → … → 9), para cada PR continuar certo
  sozinho. A Etapa 1 (que está no `main`) foi corrigida na branch da Etapa 2.
  Gabriel ainda não terminou de ler; pode haver mais correções.

**Vídeos (ideia de Gabriel, ainda NÃO é pedido):** ele pensa em gravar vídeos e
colocar em cada etapa uma escolha que expande para baixo: "Ler o conteúdo" ou
"Assistir ao vídeo". Proposta já apresentada a ele: dois painéis expansíveis,
quiz e caso abaixo dos dois (comuns aos dois caminhos), conteúdo escrito sempre
no DOM (a busca da home depende dele), player + link para YouTube/OneDrive.
Oferecido também: preparar slides e roteiro de cada vídeo a partir do texto.
**Não implementar sem ele decidir.**

## 4. Estado atual (05/11/2026)

| Etapa | Arquivo | Estado |
|---:|---|---|
| 1 A HI Tecnologia | `Assets/hi_tecnologia.html` | **Aprovada** por Gabriel em 04/11/2026 (reteste depois da correção da GTI5/SmartManagerPro). |
| 2 Fundamentos da Automação | `Assets/fundamentos.html` | **Aprovada** por Gabriel em 04/11/2026 (PR #1, branch `etapa-2-fundamentos`; ele faz o merge). Erros achados depois serão corrigidos depois. |
| 3 Comunicação Industrial | `Assets/comunicacao.html` | **Aprovada** por Gabriel em 05/11/2026 (PR #2, branch `etapa-3-comunicacao`; ele faz o merge, depois do #1). |
| 4 Linha de CLPs | `Assets/clps.html` | **Aprovada** ("pode continuar", 05/11/2026). PR #3, branch `etapa-4-clps`. |
| 5 Gateways, Modem e Rádios | `Assets/conectividade.html` | **Pronta, aguardando revisão.** Branch `etapa-5-conectividade` (a partir de `etapa-4-clps`), PR #4. |
| 6 IHMs, Sensores e Acessórios | `Assets/ihm_sensores.html` | **Pronta, aguardando revisão.** Branch `etapa-6-ihm-sensores` (a partir da 5), PR #5. |
| 7 Supervisão Local e em Nuvem | `Assets/supervisao.html` | **Pronta, aguardando revisão.** Branch `etapa-7-supervisao` (a partir da 6), PR #6. |
| 8 Soluções e Programas | `Assets/solucoes.html` | **Pronta, aguardando revisão.** Branch `etapa-8-solucoes` (a partir da 7), PR #7. Testada (quiz, conclusão, escuro, 360 px, busca). |
| 9 A Conversa de Venda | `Assets/conversa_venda.html` | **Pronta, aguardando revisão.** Branch `etapa-9-conversa` (a partir da 8), feita no VS Code em 05/11/2026. Testada (quiz, conclusão, escuro, 360 px, busca). PR ainda não aberto (ver "Onde parei"). |
| 10 Avaliação Final | `Assets/avaliacao_final.html` | Página "em produção": selo, objetivos, tempo, caixa "Conteúdo em produção" e fontes previstas. |

### ONDE PAREI (05/11/2026, de volta ao VS Code)
- **11/11/2026: Etapas 1 a 9 PUBLICADAS** a pedido de Gabriel (um colega dele vai
  conferir o conteúdo no site). O `main` foi avançado até `etapa-9-conversa`
  (fast-forward, sem merge novo) e a Action "Publicar site" passou. Com isso o
  PR #1 fica como mergeado; os PRs #2 a #7 (base = branch da etapa anterior)
  continuam abertos e podem ser fechados, pois o conteúdo já está no `main`. A
  Etapa 9 nunca teve PR. Daqui em diante: trabalho novo em branch a partir do
  `main`, e só vai ao `main` com o ok de Gabriel.
- Os créditos da nuvem acabaram em 05/11/2026 e o trabalho voltou ao VS Code de
  Gabriel. As Etapas 2 a 8 estão em branches encadeadas com PR aberto:
  #1 (Etapa 2) → #2 (3) → #3 (4) → #4 (5) → #5 (6) → #6 (7) → #7 (8).
  **Merge nessa ordem**; nada foi para o `main`, nada foi publicado.
- **Etapa 9** feita no VS Code na branch `etapa-9-conversa`, criada a partir de
  `etapa-8-solucoes`. O `gh` não está instalado nessa máquina: o PR é aberto
  pelo link que o `git push` mostra (ou pela página do repositório), com base
  `etapa-8-solucoes`.
- Gabriel aprovou até a Etapa 4; as Etapas 5 a 9 foram feitas em sequência
  sem revisão (ele pediu) e serão revisadas depois.
- **Revisão geral em andamento (05/11/2026):** Gabriel está lendo as Etapas 2
  a 9 e mandou o primeiro lote de correções (seção 3, "revisão de Gabriel").
  Corrigir **na branch da etapa** e levar adiante com merge, nunca só na
  última branch: senão o PR de uma etapa vai ao ar com o texto antigo.
- **Próximo passo:** terminar a revisão com Gabriel; depois a **Etapa 10
  (Avaliação Final)** numa branch `etapa-10-avaliacao` a partir da 9, e a
  Fase 4.
- Ferramentas de teste: na nuvem havia um teste com Playwright (não está no
  repositório). No VS Code os testes rodam no Edge sem interface
  (`msedge --headless=new --dump-dom` e `--screenshot`), sobre uma **cópia** do
  site no scratchpad com o login desligado (`url` e `anonKey` vazios), servida
  por `python -m http.server`. As páginas de teste de `ferramentas/testes/`
  foram copiadas com o nome da etapa trocado, mais três novas (marcar a etapa,
  os SVGs nos dois temas lado a lado, a busca da home). Tabelas em imagem dos
  PDFs foram lidas na nuvem com `pdftoppm -f N -l N -r 200`.
- **Links do catálogo:** os botões "Clique" do PDF interativo apontam para o
  site (`www.hitecnologia.com.br/produto/...`, uma página por produto), a
  Sympla, o YouTube e as redes da HI. Dá para listar com
  `grep -a -o "https\?://[^)> ]*" fontes/originais/Catalogo-HI-Interativo.pdf`.
  Foi a base do exercício 9 na Etapa 9.

**Etapa 9, o que foi feito (para não refazer):** 10 seções (a conversa em
cinco momentos: abrir, entender o problema, qualificar, desenhar a solução,
encaminhar; perguntas abertas; roteiro de qualificação juntando as perguntas
de bolso das Etapas 1–8 por assunto, com a etapa de origem; arquiteturas
típicas A–F (máquina com IHM, planta com supervisório local, integrar
equipamentos existentes, pontos remotos por rádio, nuvem pelo 4G, solução
pronta) com diagrama de um exemplo de saneamento que combina D, A, B e E;
conversa de exemplo fictícia, momento a momento, sobre esse mesmo exemplo;
tabela "não prometa → diga no lugar → quem confirma"; quem responde cada
assunto (setor de vendas, suporte, Engenharia de Produto, engenharia de
aplicação), sinais de que é hora de acionar e a ficha a levar; onde consultar
(exercício 9); na venda; glossário), 2 diagramas, quiz de 10 e caso com 5 itens
para o role-play do Encontro 2. Cinco `[CONFIRMAR]` novos (prazo e garantia;
canal e regras para acionar suporte/engenharia; visita técnica; manuais e
fichas técnicas no site; materiais que podem ir ao cliente). Decisões de
redação: o momento 1 e as perguntas abertas são conceito geral de vendas,
dito no `.fonte`; "concorrente mais barato" é tratado sem dizer que a HI é
mais barata (mostrar o que a solução inclui e mandar ao orçamento); o exemplo
de saneamento e a conversa são marcados como fictícios.

**Etapa 8, o que foi feito (para não refazer):** 10 seções (DAP5 com a tabela
do catálogo p. 35; óleo e gás com os 4 métodos de elevação, números e recursos
do bombeio mecânico, clientes do catálogo; HI OilTools; tabela "o cliente diz
→ programa"; HI OEM com produtos elegíveis; HI Partner; HI University;
representantes; na venda; glossário), 1 diagrama, quiz de 10 e caso com 3
itens. Três `[CONFIRMAR]` novos: sinais/CLP/comunicação do DAP5; critérios para
entrar no HI Partner; representante por região (repete o da Etapa 1).

**Etapa 7, o que foi feito (para não refazer):** 10 seções (por que
supervisionar; HIscada Pro com recursos do catálogo p. 33 e OPC; licença do
HIscada com a **tabela Teste/L1–L7/LDev lida da imagem do Treinamento p. 19**
— tags OPC, tags locais, viewers, sessão, servidor OPC "MPL Server" ou
"qualquer", sem valores; MPL Server e a regra da licença para Modbus de
terceiros; Portal com recursos, segurança AWS e white label; planos
Free/Basic/Plus/Enterprise com a **tabela de recursos lida da imagem da p. 22,
sem os valores**; HIscada × Portal; solução IoT completa com HI Connect; na
venda; glossário), 2 diagramas, fotos `Files/HIscadaPRO.png` e
`Files/portal.png`, quiz de 10 e caso com 5 itens. Nenhum `[CONFIRMAR]` novo.
Decisões de redação: a frase do Treinamento p. 20 sobre "baixo custo das
licenças comparado aos concorrentes" **não foi usada** (comparação de preço
com concorrente); "Free" aparece só como nome de plano, sem dizer que é
gratuito nem limites de dados; o conceito Conector/Dispositivo do
`CONTEXT.txt` não foi usado (o arquivo já teve erro sobre os ESC).

**Etapa 6, o que foi feito (para não refazer):** 11 seções (IHM × supervisório
em tabela; GTI5 com modelos, portas, IP65, SmartManagerPro e a regra da
Weintek; revenda Weintek/Veichi e MMI700; perguntas para escolher a IHM e como
tratar "IHM econômica"; THT863 e HPS850; fontes Mean Well por potência, SBC513
e BPU508; GEM100; RTK510 com os recursos lidos do quadro em imagem do catálogo
p. 14; checklist "pedido completo"; na venda; glossário), 1 diagrama, foto
`Files/IHM_GTI5.png`, quiz de 10 e caso com 5 itens. Quatro `[CONFIRMAR]`
novos na página: SmartManagerPro gratuito?, MMI700 ainda vendida?, BPU508 ainda
vendida?, perfil de cliente da GEM100. Exercícios: 6, 11, 13 e 20.

**Etapa 5, o que foi feito (para não refazer):** 10 seções (linha GTON com
tabela do Treinamento p. 12, nomenclatura SET/S4E e os ESC como antecessores;
GTON-C nos modos transparente e bridge; GTON-P com interfaces A/B, HIstudio e
protocolos; GTON-M com Nano SIM, SMA, Anatel e HI Connect; USB721; rádios
WSC720 × R9X307; venda de rádio em 4 passos com diagrama; tabela "o cliente diz
→ produto"; na venda; glossário), 2 diagramas, fotos `Files/GTON-C.png`,
`GTON-P.jpg`, `GTON-M.png`, `radio.png`, quiz de 10 e caso com 5 itens. Um
`[CONFIRMAR]` novo: equivalência ESC → GTON e se os ESC ainda são vendidos.
Dados lidos da **imagem** da p. 15 do Treinamento (renderizada com
`pdftoppm`): WSC720 = XBee-PRO 900HP, 3 km ao ar livre / 150 m interno; R9X307
18 km urbano, 105 km rural na tabela, mas a recomendação é 60 km. Aviso
reforçado: gateway não lê sensor.

**Etapa 4, o que foi feito (para não refazer):** 10 seções (tabela
comparativa; RION5; NEON5 com as combinações de conectividade do slide 6; P7C
302 com diagrama dos bastidores; RION5 como I/O remoto do NEON5, até 14 e 240
pontos, sem programar o RION5; módulos de I/O por tipo, sem códigos, com o
aviso de canais excludentes e famílias separadas; HIstudio com a foto
`Files/HIstudio.png`; as quatro perguntas de escolha com tabela "o cliente diz
→ CLP"; na venda; glossário), 4 diagramas, quiz de 10 e caso com 5 itens.
Nenhum `[CONFIRMAR]` novo. Decisões de redação: "CLP mais econômico da HI"
para o RION5 aparece **uma vez**, atribuído ao Treinamento (p. 9), sem valor e
com "valores, só pelo orçamento"; "baixo custo" da narração do slide 7 não foi
usado; "o P7C não tem rádio, Wi-Fi nem 4G" vem da lista de conectividade do
Treinamento p. 7. Fontes: Treinamento p. 4–9; slides 4–7; Catálogo p. 5–10,
14, 32 e 40. CSS novo: `.step .foto`.

**Etapa 3, o que foi feito (para não refazer):** 8 seções (linha e idioma;
RS232/RS485/Ethernet com tabela de distâncias **de referência geral**, marcada
como tal; Wi-Fi/rádio/4G com visada, KML e estudo de altimetria e HI Connect;
as três perguntas com árvore de decisão e tabela "o cliente diz → caminho";
protocolos Modbus RTU/TCP, SCP-HI, ASCII, MQTT, mais OPC e HTTP de passagem,
mestre e escravo; os quatro sinais de que falta conversor/gateway, com os
produtos só como prévia da Etapa 5; na venda; glossário), 4 diagramas, quiz de
10 e caso com 4 itens. Um `[CONFIRMAR]` novo: onde o SCP-HI aparece na venda.
Decisões de redação: alcance de rádio **sem número** (a inconsistência 60 ×
105 km fica para a Etapa 5); conversor chamado de "GTON-C" (nome do catálogo,
como na Etapa 1). Fontes: Treinamento p. 4, 11–16, 19–21; slide 3; Catálogo
p. 5, 7, 8, 16–22, 30, 32 e 38.

**Etapa 2, o que foi feito (para não refazer):** 8 seções (automação e
processo; sensor, CLP e atuador com THT863/HPS850 e IHM × supervisório; os três
pilares do CLP; AC × DC com a tabela de alimentação dos produtos; digital ×
analógico com a régua 0–100 %, os quatro tipos de ponto e os sinais especiais
PT100/célula de carga/contador rápido; pirâmide em 4 níveis com a comunicação
como "elevador"; na venda; glossário), 4 diagramas SVG, quiz de 10 e caso com 4
itens. **Nenhum `[CONFIRMAR]` novo**: tudo saiu do Treinamento p. 2–5, 10,
17–19, 21–23, dos slides 1–2 e do Catálogo p. 7–10, 24, 26, 30–33, 38; o que é
conceito geral (pirâmide, "zero vivo" de 4 mA, analogias) está dito no `.fonte`.
Decisões de redação: não usar "economia" para AC (a narração do slide 2 usa;
regra 4); não citar a BPU508 (inconsistência da Etapa 6), só Mean Well e
SBC513; a pirâmide tem 4 níveis (campo, controle, supervisão local, nuvem),
como na grade, e o texto explica a diferença para o mapa de 5 camadas da
Etapa 1. CSS novo em `etapa.css`: `.diagrama-corpo`, `d-cheio`, `d-linha`,
`d-texto-claro` (com variante escura onde precisa).

**Antes de começar cada nova etapa, cobrar de Gabriel** (ele pediu: "me cobre
mais para a frente"):
1. **Clientes de referência** de Energia, Indústria 4.0, Meio Ambiente,
   Hospitalar e Predial (ele vai levantar com a equipe). Hoje com
   `[CONFIRMAR]` na Etapa 1, item 4.
2. **Qual representante** (TBC Automação, 4Sys Sistemas) **cobre cada região**.
   `[CONFIRMAR]` na Etapa 1, item 5.

Quando ele passar os dados: atualizar `Assets/hi_tecnologia.html`, tirar o
`[CONFIRMAR]` e a linha da tabela do `README.md`.

**Também ofereceram e não chegaram (pode lembrar quando fizer sentido):**
- **Cases reais** (problema → solução → resultado): Gabriel disse que pode
  compartilhar. São o que mais falta, principalmente para a Etapa 9.
- **Print das páginas impressas 3 e 4 do catálogo** (segmentos Indústria 4.0,
  Meio Ambiente, Hospitalar, Energia), que não puderam ser extraídas do PDF.
- **Processo comercial e regras de escalonamento** (orçamento, prazo, garantia,
  quando acionar suporte/engenharia) para a Etapa 9.
- **Lista dos vídeos/tutoriais do suporte** para a Fase 4 (dá para começar
  pelos links do site do suporte).

## 5. A grade (Fase 2, aceita) e o plano de cada etapa

~20 h em 2 semanas. Semana 1: Etapas 1–4 + **Encontro 1** com o instrutor
(casos das Etapas 1–4). Semana 2: Etapas 5–9 + **Encontro 2** (role-play e
Avaliação Final). A agenda está na home (`index.html`).

| Etapa | Arquivo | Tempo | Ao final, o vendedor consegue… | Fontes principais |
|---:|---|---|---|---|
| 1 A HI Tecnologia | `hi_tecnologia.html` | 1h30 | apresentar a empresa em 1 min, citar segmentos e clientes, explicar o que a HI fabrica, revende e presta como serviço | Catálogo p. 2–6, 39–44 (impressas) |
| 2 Fundamentos da Automação | `fundamentos.html` | 2h30 | explicar processo, sensor, atuador e CLP com analogias; AC × DC e por que escolher cada uma; digital (liga/desliga) × analógico (0–100 %); situar cada produto HI na pirâmide (campo → controle → supervisão → nuvem) | Treinamento p. 3–5; `introducao_automacao...html` slides 1–2; conceitos gerais |
| 3 Comunicação Industrial | `comunicacao.html` | 2h | escolher RS232, RS485, Ethernet, Wi-Fi, rádio ou 4G por três perguntas (quantos equipamentos, a que distância, tem internet?); Modbus, MQTT, ASCII e SCP-HI como "idiomas"; perceber quando o cliente precisa de conversor/gateway | Treinamento p. 4; HTML slide 3 |
| 4 Linha de CLPs | `clps.html` | 2h30 | indicar RION5, NEON5 ou P7C por pontos de I/O, alimentação, SD Card e conectividade; RION5 como I/O remoto do NEON5; módulos de I/O sem ficha técnica; HIstudio gratuito | Treinamento p. 5–9; Catálogo p. 6–10 e 32; HTML slides 4–7 |
| 5 Gateways, Modem e Rádios | `conectividade.html` | 2h30 | GTON-C (traduzir rede / bridge Modbus RTU↔TCP), GTON-P (inteligência programável), GTON-M (modem 4G), USB721 (ligar o PC); rádio integrado (WSC720) × R9X307; venda de rádio com visada, KML e estudo de altimetria pela Engenharia | Treinamento p. 11–16; Catálogo p. 15–22 |
| 6 IHMs, Sensores e Acessórios | `ihm_sensores.html` | 1h30 | IHM (operar no painel) × supervisório; GTI5 (SmartManagerPro, ver seção 3); THT863 e HPS850; fontes, caixa GEM100, kit RTK510 como complemento do pedido | Treinamento p. 10, 17–18; Catálogo p. 11–14, 23–28 |
| 7 Supervisão Local e em Nuvem | `supervisao.html` | 2h30 | HIscada Pro + MPL Server (rede local, licença por tags e viewers) × Portal de Telemetria (navegador, plano por quantidade de dados); MPL Server para equipamento de terceiros; vender o HI Connect junto | Treinamento p. 19–23; Catálogo p. 29–33, 38 |
| 8 Soluções e Programas | `solucoes.html` | 1h30 | DAP5 e solução Óleo e Gás (HI OilTools); quando o cliente é candidato a HI OEM, HI Partner ou HI University; encaminhar ao representante | Catálogo p. 34–42 |
| 9 A Conversa de Venda | `conversa_venda.html` | 2h30 | roteiro de qualificação; arquiteturas típicas "do sensor à nuvem"; lista do que não prometer; quando acionar suporte/engenharia | transversal + respostas de Gabriel (`[CONFIRMAR]` processo comercial) |
| 10 Avaliação Final | `avaliacao_final.html` | 1h | atender um cliente simulado do primeiro contato até a indicação da solução (role-play no Encontro 2) | todas |

Os objetivos exatos de cada etapa já estão na página "em produção" dela e em
`ferramentas/gerar_etapas.py`. As páginas do catálogo da tabela (impressas) são
as que essas páginas anunciam, mas foram levantadas no diagnóstico: **conferir
no `fontes/texto/catalogo_hi.txt` antes de citar** e corrigir a página "em
produção" se mudar.

**Exercícios já usados:** Etapa 2 usou o **1** (quatro tipos de ponto), o
**2** só na parte conceitual (os três pilares; a escolha de modelo fica para a
Etapa 4) e, no caso para o instrutor, o **10**, o **11**, o **12** e o **20**
apenas para montar a lista de sinais, a alimentação e as perguntas (sem
escolher produto). Esses quatro voltam na Etapa 4 para a escolha do CLP e dos
módulos. O pedido de IHM "econômica" (11 e 20) virou pergunta do caso: como
tratar sem falar de preço.
Etapa 3 usou o **4** e o **8** (conceitos, no caso) e, só para diagnosticar
meio, idioma e falta de tradutor (sem escolher produto), o **14**, o **15**, o
**17**, o **18** e o **19**. Esses cinco voltam na Etapa 5 para a escolha do
GTON-C, GTON-M etc.
Etapa 4 usou o **2**, o **3** e o **7** (conceitos, no caso) e, para escolher a
família de CLP, o **10**, o **12**, o **13** e o **16**. Ainda não usados: **5**,
**6**, **9** e **21**; o **11** e o **20** só apareceram na Etapa 2 (lista de
sinais) e voltam com a IHM na Etapa 6 e na oferta completa (Encontro 2,
Avaliação Final).
Etapa 5 usou o **5** e retomou, agora com produto, o **14**, o **15**, o
**17**, o **18**, o **19** e o **21**.
Etapa 6 usou o **6** e, com a IHM e o pedido completo, o **11**, o **13** e o
**20**.
Etapa 9 usou o **9** (seção "Onde consultar", quiz e caso) e, no role-play do
caso, o **15** e o **16** reescritos como clientes que só revelam a
necessidade se o vendedor perguntar. Todos os 21 já apareceram; a Avaliação
Final pode reaproveitar qualquer um como caso completo (os de oferta, 10–13,
16, 20 e 21, são os melhores).

**Os 21 exercícios** de `fontes/texto/exercicios_treinamento_de_produto.txt`
mapeiam assim (sugestão, ainda não discutida com Gabriel): 1 → Etapa 2;
4, 8 → Etapa 3; 2, 3, 7 → Etapa 4; 5, 14, 15, 17, 18, 19 → Etapa 5; 6 →
Etapa 6; 9 → Etapa 1/9; os casos 10–13, 16, 20, 21 (montar a oferta a partir
da necessidade) → Etapas 4–6, Encontro 2 e Avaliação Final. **Sem gabarito**:
resposta só com fonte. Atenção: o 11 e o 20 pedem "IHM de baixo custo /
econômica" — tratar sem citar preço (regra 4).

### Fase 4 (depois da Etapa 10)
- Glossário geral consolidado (juntar os `.glossario` das etapas).
- Avaliação final (Etapa 10) com gabarito no guia do instrutor.
- **Guia do instrutor/gestor**: como aplicar, roteiro dos dois encontros,
  gabaritos e critérios dos casos e do role-play.
- **Mapa de vídeos do suporte reaproveitáveis** por etapa (a partir dos links
  do site `Forma-o-HI`).

### Inconsistências entre fontes (perguntar a Gabriel quando chegar a etapa)
| Etapa | Ponto |
|---|---|
| 5 | ~~R9X307 60 × 105 km; ESC717/ESC713; GTON C SET × GTON-C~~ **resolvidas em 05/11/2026** (ver seção 3) |
| 6 | MMI700 (IHM alfanumérica, no Treinamento e no site do suporte) ainda é vendida? (`[CONFIRMAR]` na Etapa 6) |
| 6 | Fonte própria: BPU508 (Treinamento, no-break 13,8 V) × SBC513 (catálogo, LiFePO4). A BPU508 ainda é vendida? (`[CONFIRMAR]` na Etapa 6) |
| 7 | Preços do Portal no Treinamento (print com R$): **não usar** (regra 4); ensinar só a lógica dos planos (Free/Basic/Plus/Enterprise, por quantidade de dados) |
| 1 | Catálogo p. 12 escreve "Smart Manager Pro"; Gabriel escreve "SmartManagerPro". Usar a grafia dele. |

## 6. Como o site funciona

Estrutura completa e guia de componentes no **`README.md`** (seções 1, 3 e 5).
O essencial:

- HTML/CSS/JS puros, sem build. Publicação prevista no **GitHub Pages**
  (diferencia maiúsculas/minúsculas nos nomes de arquivo).
- **Supabase** (login + progresso): mesmo projeto do suporte
  (`Assets/config-conta.js`, chave pública anon, já pública no site do
  suporte). Tabela `progresso_vendas` criada por `supabase/configuracao.sql`,
  que **ainda não foi rodado** (alguém com acesso precisa rodar uma vez). A
  tabela `admins` e a função `eh_admin()` são as do suporte.
- **localStorage:** os dois sites ficam no mesmo domínio `github.io` e
  dividem o armazenamento. O de vendas usa as chaves `formacaoVendasHI.*` (o
  suporte usa `formacaoHI.*`). A chave do tema `hi-tema` é compartilhada de
  propósito.
- **Busca da home** (`Assets/busca-conteudo.js`): baixa cada página de etapa e
  indexa os blocos `.step` com `<h3>`. **Não funciona aberta como `file://`**;
  testar sempre com servidor.
- **Total de etapas = 10**, fixo em `progresso.js` (`TOTAL`), `conta.js`
  (lista `ETAPAS`), `admin.html` (`TOTAL` e `ETAPAS`) e no SQL
  (`check between 1 and 10`). Mudar o número exige mexer nos quatro.
- **Modo escuro:** `html[data-theme="dark"]` com os tokens `--esc-*` do
  `responsive.css`. Todo componente novo precisa da variante escura em
  `etapa.css`.

### Como escrever uma etapa (padrão de qualidade da Etapa 1)
Copiar o esqueleto de `Assets/hi_tecnologia.html` e manter:
- `<head>`: `etapa.css` → `responsive.css` → `tema.js`; scripts no fim:
  `progresso.js`, `config-conta.js`, `conta.js`, `quiz.js`.
- Hero com diagrama SVG da etapa; caixa `.objetivos` ("Ao final desta etapa
  você consegue" + tempo); `.sumario` com âncoras.
- Seções numeradas em `.step` + `<h3>` (é o que a busca indexa). Em cada uma:
  texto curto e concreto, caixa `.analogia` ("Pense assim") onde houver
  conceito abstrato, `.na-venda` com o uso na conversa, `.atencao` com o que
  não prometer, `.fonte` com as páginas.
- Uma seção **"Na venda"** com perguntas típicas de clientes (tabela pergunta →
  como responder), argumentos e erros a evitar.
- **Glossário** (`.glossario`, `<dl>`) dos termos da etapa.
- **Quiz de 10 questões** (`.quiz-bloco` + `form.quiz`; marcação no topo de
  `Assets/quiz.js`): `data-certa` em cada `fieldset.quiz-q`, explicação em
  `p.quiz-explica` que diz **por que** a certa é certa. Aprovação em 80 %
  (o resultado não é salvo). Conferir que nenhuma alternativa "certa" fere as
  regras de ouro e que nenhuma pergunta sugere que a HI não atende um setor.
- Caixa `.caso` com o caso para o encontro com o instrutor.
- Navegação no fim: "Marcar etapa como concluída", Voltar, ← anterior,
  próxima →.
- Atualizar o status da etapa no `README.md` e as pendências `[CONFIRMAR]`.

### Como testar
1. Servidor local na raiz: `python3 -m http.server 8000` → `http://localhost:8000`.
   Abre uma tela de login (Supabase). Para testar sem login, numa **cópia**
   temporária, deixe `url` e `anonKey` vazios em `Assets/config-conta.js`
   (nunca commitar assim).
2. Testes já usados (em `ferramentas/testes/`, abrir pelo servidor, ex.:
   `http://localhost:8000/ferramentas/testes/teste_quiz.html`):
   - `teste_quiz.html`: responde o quiz da Etapa 1 (uma errada, uma em
     branco), corrige, confere as etiquetas e o "Refazer". Adaptar o `src` do
     iframe para a etapa nova.
   - `overflow.html`: carrega a etapa num iframe de **360 px** e lista
     elementos que estouram a largura (fora de `.tabela`, que tem rolagem).
   - `escuro.html`: liga o modo escuro e abre a etapa.
   - `largura.html`: mostra a largura útil da janela.
   No computador de Gabriel isso rodava no Edge sem interface
   (`--headless --dump-dom` e `--screenshot`); o Edge headless não desce de
   ~492 px de largura, por isso o teste de celular é pelo iframe. Na nuvem, use
   o navegador headless disponível (Chromium/Playwright), se houver.
3. Conferir: quiz (corrigir, etiquetas, refazer), "Marcar etapa como
   concluída" grava em `formacaoVendasHI.etapasConcluidas`, modo escuro, 360 px
   sem estouro, busca da home encontrando os `<h3>` novos.
4. Dizer a Gabriel **o que ele deve olhar** ao revisar a etapa.

## 7. Ferramentas

| Arquivo | Uso |
|---|---|
| `ferramentas/pdf_texto.py` | Texto de todas as páginas de um PDF, linha a linha. `python3 -I ferramentas/pdf_texto.py fontes/originais/Catalogo-HI-Interativo.pdf 1 > saida.txt` (o `1` acrescenta a página impressa). Só biblioteca padrão. |
| `ferramentas/pdfpos.py` | Texto de **uma** página com a posição (x, y) de cada trecho. Foi assim que a linha do tempo do catálogo (ano × evento) foi pareada. |
| `ferramentas/gerar_etapas.py` | Gera as páginas "em produção" das Etapas 2–10 a partir de uma lista com objetivos, tempo e fontes. Não sobrescreve página existente. Já foi rodado; serve de referência dos objetivos. |
| `ferramentas/testes/` | Testes de navegador descritos acima. |

Se o ambiente tiver `pypdf`/`pdftotext`, podem ser usados também; o catálogo
tem fontes com kerning e trechos sem mapa de caracteres (p. 4–5 ilegíveis em
qualquer extrator testado aqui).

## 8. Repositório

`gbroccol0/ProgramaFormacaoVendas`, **público** (04/11/2026). Gabriel e a
equipe decidiram hospedar o site neste mesmo repositório, cientes de que
`fontes/` (Treinamento de Produto, Exercícios, Catálogo), este arquivo e o
histórico ficam visíveis para qualquer pessoa. Mesmo assim, **não acrescentar
dado sensível novo** (preço, contato pessoal, dado de cliente que não esteja
nas fontes) sem Gabriel pedir.

**Publicação:** o site vai ao ar em
https://gbroccol0.github.io/ProgramaFormacaoVendas/ pelo GitHub Pages deste
repositório (Source: GitHub Actions). A Action
`.github/workflows/publicar-site.yml` publica só `index.html` e `Assets/`, a
cada push no `main` que mexa neles. Consequências:
- **Push no `main` publica.** Etapa ainda não aprovada por Gabriel vai ao ar
  assim que for para o `main`; para trabalho em andamento, usar outra branch
  e só levar ao `main` com a aprovação dele (ou quando ele pedir).
- Depois de publicar, conferir em Actions que o "Publicar site" passou e dar
  a Gabriel o link da etapa no site publicado.

## 9. Fluxo com Gabriel

- Ele revisa cada etapa no navegador e devolve correções por texto (às vezes
  com print). Aplicar, testar, explicar o que mudou e por quê, e **esperar a
  aprovação** antes da próxima etapa.
- Respostas em português, diretas; quando algo ficou como `[CONFIRMAR]`, dizer
  o que falta e quem pode responder.
- Commit e push só quando ele pedir, ou ao fim de uma entrega combinada.
- Manter este `CLAUDE.md` e o `README.md` em dia a cada mudança de estado
  (decisão nova, etapa aprovada, pendência resolvida).
