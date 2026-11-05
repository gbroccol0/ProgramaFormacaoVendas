# Fontes do programa

Material que Gabriel entregou para a construção do programa. **Só leitura**: os
originais não são alterados nem apagados (regra do pedido). A pasta de origem,
no computador dele, é `C:\Users\gabriel_monteiro\Documents\Programa de formação vendas`.

## `originais/` — os arquivos como vieram

| Arquivo | O que é | Como usar |
|---|---|---|
| `Catalogo-HI-Interativo.pdf` | Catálogo Geral da HI (44 p., 29 MB) | Fonte comercial: empresa, linha do tempo, segmentos, clientes, produtos, programas. **Citar a página impressa** (página do PDF menos 1). |
| `Treinamento de produto.pdf` | Treinamento que o suporte aplica a novos técnicos (23 p.) | Fonte principal de conteúdo, mas escrita para técnicos: **traduzir para linguagem comercial**, não copiar. Citar a página do PDF. |
| `Exercícios do treinamento de produto.odt` | 21 exercícios do Treinamento de Produto (chegou em 30/10/2026; a Etapa 2 usou o 1, o 2 e partes do 10, 11, 12 e 20; a Etapa 3, o 4, o 8 e partes do 14, 15, 17, 18 e 19; a Etapa 4, o 2, o 3, o 7 e partes do 10, 12, 13 e 16; ver `CLAUDE.md`) | Ótima base para quizzes e casos das Etapas 2 a 6 e da Avaliação Final. **Não tem gabarito**: a resposta tem que sair das fontes; o que não sair vira `[CONFIRMAR]`. |
| `introducao_automacao_e_clps_hi_tecnologia.html` | O "Módulo 01" antigo: 7 slides narrados sobre automação e CLPs | Conteúdo útil para as Etapas 2 a 4. O formato (player com voz do navegador) foi **rejeitado** por Gabriel. |
| `CONTEXT.txt` | Metodologia "Explicar o porquê" e roadmap dos módulos antigos | **Vale a metodologia** (ver o `CLAUDE.md` da raiz). O arquivo parece cortado no Módulo 04. |
| `SKILLS.txt`, `DICIONARIO_FONETICO.txt`, `PROMPT_CONTINUIDADE.txt` | Padrão técnico do player narrado e regras de pronúncia para voz sintética | Superados (formato rejeitado). Só servem se algum dia voltar narração por voz sintética. |
| `prompt utilizado.txt` | Primeiro pedido de Gabriel, antes do prompt de fases | Contexto. |

## `texto/` — texto extraído (para consulta rápida e busca)

Gerado com `ferramentas/pdf_texto.py` (biblioteca padrão do Python, sem instalar
nada) e com um extrator de `.odt` de poucas linhas.

| Arquivo | Origem | Observações |
|---|---|---|
| `catalogo_hi.txt` | Catálogo | Cabeçalho de página `===== PDF p. N (impressa N-1) =====`. Algumas fontes do PDF têm kerning e o extrator às vezes junta ou separa letras ("Smar t Manager Pr o"). **As descrições dos segmentos Indústria 4.0, Meio Ambiente, Hospitalar e Energia (PDF p. 4–5) saem ilegíveis** (fonte sem mapa de caracteres); ficaram como `[CONFIRMAR]`. Na dúvida sobre um trecho, abrir o PDF. |
| `treinamento_de_produto.txt` | Treinamento | Cabeçalho `===== PDF p. N =====`. Bem legível. Tabelas saem linha a linha. |
| `exercicios_treinamento_de_produto.txt` | Exercícios (.odt) | Texto completo dos 21 exercícios. |

Para a posição exata de cada trecho numa página (útil para parear coluna de
ano com evento, por exemplo), use `ferramentas/pdfpos.py arquivo.pdf <página do PDF>`.

## Fora desta pasta

- **Site do suporte (modelo de estrutura e visual):** repositório
  `Otavio7w7/Forma-o-HI` no GitHub, publicado em
  https://otavio7w7.github.io/Forma-o-HI/. **Não alterar.** As etapas dele
  linkam os vídeos e tutoriais do suporte (YouTube/OneDrive), base para o
  mapeamento de vídeos reaproveitáveis da Fase 4.
