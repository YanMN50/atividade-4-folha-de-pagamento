# Atividade: Sistema de Folha de Pagamento

## Contexto

Você faz parte de um time de desenvolvimento de software responsável por criar um sistema para calcular os descontos e acréscimos na folha de pagamento dos funcionários de uma empresa. Seu objetivo é criar um programa em Python que solicite a matrícula e senha de um funcionário para ter acesso aos seus dados e calcular os descontos e acréscimos mais comuns no Brasil.

## Regras de Descontos e Acréscimos

### INSS (Instituto Nacional do Seguro Social)
O desconto do INSS é calculado de acordo com a faixa salarial do funcionário:
- Salário até R$ 1.100,00: 7,5%
- Salário de R$ 1.100,01 até R$ 2.203,48: 9%
- Salário de R$ 2.203,49 até R$ 3.305,22: 12%
- Salário de R$ 3.305,23 até R$ 6.433,57: 14%
- O valor máximo de desconto do INSS é de R$ 854,36.

### IRRF (Imposto de Renda Retido na Fonte)
O desconto do IRRF é calculado de acordo com a faixa salarial do funcionário e com a quantidade de dependentes:
- Isento: Salário até R$ 2.259,20
- 7,5%: Salário de R$ 2.259,21 até R$ 2.826,65
- 15%: Salário de R$ 2.826,66 até R$ 3.751,05
- 22,5%: Salário de R$ 3.751,06 até R$ 4.664,68
- 27,5%: Salário acima de R$ 4.664,68
- Dedução por dependente: R$ 189,59 por dependente.

### Vale Transporte
Desconto de 6% do salário base do funcionário, caso opte pelo benefício.

### Vale Refeição
Desconto de 20% do valor do benefício fornecido pela empresa.

### Plano de Saúde
Desconto fixo de R$ 150,00 por dependente.

## Instruções

1. Solicite a matrícula e senha do funcionário para ter acesso aos seus dados.
2. Solicite o salário base do funcionário.
3. Pergunte se o funcionário deseja receber vale transporte (s/n).
4. Pergunte o valor do vale refeição fornecido pela empresa.
5. Calcule os descontos e acréscimos na folha de pagamento do funcionário.
6. Mostre o salário líquido do funcionário após os descontos e acréscimos.

## Observações

- Considere que o funcionário possui apenas um dependente.
- Considere que o salário base é o salário antes de quaisquer descontos ou acréscimos.
- Considere que o salário base, o vale refeição e o plano de saúde são informados em reais (R$).

## Exemplos de Cálculo

### Exemplo 1: Salário Baixo (R$ 1.412,00) com 0 Dependentes e Vale Transporte

- **Salário Base:** R$ 1.412,00
- **Dependentes:** 0
- **Vale Transporte:** Sim
- **Vale Refeição:** R$ 300,00
  
**Salário Líquido:** R$ 1.161,38

### Exemplo 2: Salário Alto (R$ 10.000,00) com 2 Dependentes e Sem Vale Transporte

- **Salário Base:** R$ 10.000,00
- **Dependentes:** 2
- **Vale Transporte:** Não
- **Vale Refeição:** R$ 500,00
  
**Salário Líquido:** R$ 6.400,92
