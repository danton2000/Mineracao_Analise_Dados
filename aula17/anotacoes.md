# Árvore de Decisão

- Representação gráfica
- Ajudar a identificar dados contínuos de forma booleana
- Existem perguntas boas e perguntas ruins (optar pelas boas)
- Existem algoritmos
- Ganho de Informação
- Intropia
- GINI
- 'preparar folinha para a prova'

## Calculo Gini
n = elementos
0 = 2 (2 eram 0)

1 = 2 (2 eram 1)

n = linhas

n = 3
0 = 2
1 = 1

G = 1 - [ (2/3)² 2 + (1/3)² ]

G = 1 - [ 0,666² + 0,333² ]

G = 1 - [0,443 + 0,111]

G = 1 - 0,554

G = 0,446

boa pergunta tende a 0

--

N = 2
0 = 2
1 = 2

(VALOR/QUANTIDADE)

GINI = 1 - [ (0/2)² + (2/2)² ]

GINI = 1 - [ (0/2)² + (2/2)² ]

GINI = 1 - [ 0 + 1 ]

GINI = 1 - 1 

GINI = 0, BOA PERGUNTA

Arvore de Decisão, raiz fica no topo.
As informações são os nodo, a ponta as folhas
separados por nivel, nivel 1, nivel 2 e etc...

### Olhar slide 10

1) Folha: < 4000 ?
G = 1 - [(2/5)² + (3/5)²]

G = 1 - [(0,16 + 0,36)]

2) Folha: Solteiro, sim
G = 1 - [(2/2)² + (0/2)²]

G = 1 - [1+0]

G = 0

2) Folha: Solteiro, não
G = 1 - [(0/1)² + (1/1)²]

G = 1 - 1

G = 0

Obs: Sei quando conceder credito
