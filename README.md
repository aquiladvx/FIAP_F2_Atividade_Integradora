# Sistema de Gerenciamento de Pouso - MGPEB

## Descrição
Este projeto implementa o protótipo do **MGPEB (Módulo de Gerenciamento de Pouso e Estabilização de Base)** para simular autorizações de pouso de módulos da colônia Aurora Siger.

O foco desta entrega está no código da Sessão 3 da atividade integradora: estruturas lineares, busca, ordenação e regras booleanas de decisão.

## Conceitos aplicados
- Estruturas lineares: lista, fila e pilha
- Busca em lista
- Ordenação com algoritmo clássico (`bubble sort`)
- Regras booleanas
- Função aplicada ao consumo de combustível
- Leitura de dados CSV com `pandas`

## Estruturas de dados usadas
- **Lista**: armazenamento base dos módulos carregados do CSV.
- **[Fila (FIFO)**: fila principal de pouso, usada para processar tentativas de autorização em ordem. (https://www.w3schools.com/python/python_dsa_queues.asp)
- **Pilha (LIFO)**: histórico de pousos autorizados, permitindo consultar o último módulo pousado. (https://www.w3schools.com/python/python_dsa_stacks.asp)

As implementações de `Fila` e `Pilha` estão em `src/utils.py`.

## Dados dos módulos
Os cenários ficam na pasta `data/`:
- `data/data_critico.csv`
- `data/data_positivo.csv`
- `data/data_aleatorio.csv`
- `data/data.csv` (padrão)

Cada módulo contém os principais atributos:
- `id`
- `prioridade`
- `combustivel`
- `massa_kg`
- `criticidade`
- `eta_orbita_min`
- `status`

## Regras de decisão (booleana)
Um módulo só é autorizado quando **todas** as condições são verdadeiras:
- `combustivel_restante >= limites["combustivel"]`
- `eta_orbita_min <= limites["eta"]`
- `massa_kg <= limites["massa"]`

Os limites são definidos em `src/constants.py`.

## Fluxo do sistema
1. Carrega os módulos do cenário escolhido.
2. Separa por prioridade (`Alta`, `Média`, `Baixa`).
3. Ordena cada grupo por `eta_orbita_min` com `bubble sort`.
4. Enfileira os módulos na fila principal.
5. Processa a fila aplicando a regra booleana de segurança.
6. Empilha módulos autorizados no histórico de pouso.
7. Exibe:
- módulos pousados
- módulos em alerta
- último módulo pousado (topo da pilha)

## Como executar
O `main.py` funciona como simulador. Você pode usar cenários específicos para rodar o MGPEB:

```bash
python3 src/main.py
```


Também é possível fornecer os dados diretamente ao gerenciador: basta colocar o arquivo em `data/data.csv` e executar o `MGPEB.py`.

Sem ambiente virtual:

```bash
python3 src/MGPEB.py
```
