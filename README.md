# 🚀 Sistema de Gerenciamento de Pouso – MGPEB

## 📌 Descrição do Projeto

Este projeto implementa o **MGPEB (Módulo de Gerenciamento de Pouso e Estabilização de Base)**, responsável por analisar se módulos espaciais estão aptos para realizar um **pouso seguro** em uma base simulada.

O sistema avalia múltiplos parâmetros operacionais e toma decisões baseadas em regras de segurança, classificando os módulos de acordo com sua condição de pouso.

O projeto foi desenvolvido como parte da *Atividade Integradora – Fase 2* do curso de Ciência da Computação da FIAP.

---

## 🧠 Conceitos Aplicados

A solução utiliza conceitos fundamentais de programação:

- Estruturas de dados (listas e dicionários)
- Ordenação de dados
- Lógica booleana para tomada de decisão
- Simulação de cenários
- Leitura de arquivos CSV
- Modularização de código
- Regras de negócio baseadas em limites operacionais

---

## 📊 Dados dos Módulos

Os dados dos módulos são carregados a partir de arquivos CSV simulando diferentes cenários de pouso.

Cada módulo contém informações como:

- `prioridade`
- `ETA`
- `combustivel`
- `risco`

Esses dados são utilizados para determinar a ordem de pouso e a viabilidade da operação.

---

## ⚙️ Regras de Validação

O sistema aplica regras para garantir que o pouso seja seguro.

### ✔️ Um módulo pode pousar se:

- O combustível restante após o pouso for **maior ou igual a 5 unidades**
- O nível de risco estiver dentro do aceitável
- As condições gerais estiverem seguras

### ⚠️ Caso contrário:

O módulo é classificado como **ALERTA** e não recebe autorização imediata para pouso.

---

## 🧠 Funcionamento do Sistema

O fluxo do sistema segue as seguintes etapas:

1. Carrega os dados dos módulos a partir de um CSV
2. Ordena os módulos por:
   - Prioridade
   - ETA
3. Avalia cada módulo com base nas regras de segurança
4. Classifica os módulos em:
   - Autorizados
   - Em alerta
   - Pousados/processados
5. Exibe o resultado da simulação

---

## 🎮 Simulação de Cenários

O arquivo `main.py` funciona como um **simulador**.

Ele pode ser usado para executar o MGPEB com cenários específicos, permitindo testar diferentes situações de pouso.

Também é possível fornecer os dados diretamente ao gerenciador. Para isso, basta adicionar o arquivo CSV no caminho:

```txt
data/data.csv