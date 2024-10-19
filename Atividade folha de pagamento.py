import os
from sqlalchemy import create_engine, Column, String, Integer, Float
from sqlalchemy.orm import sessionmaker, declarative_base

db = create_engine("sqlite:///meubanco.db")

Session = sessionmaker(bind=db)
session = Session()

Base = declarative_base()

class Funcionario(Base):
    __tablename__ = "funcionario"

    matricula = Column(String, primary_key=True)
    senha = Column(String)
    nome = Column(String)
    salario = Column(Float)
    dependentes = Column(Integer)

    def __init__(self, matricula: str, senha:str, nome:str, salario:float, dependentes:int):
        self.matricula = matricula
        self.senha = senha
        self.nome = nome
        self.salario = salario
        self.dependentes = dependentes

Base.metadata.create_all(bind=db)



def menu():
    print("="*40)
    print(f"{'Sistema de Folha de Pagamento':^40}")
    print("="*40)
    print("""
    1 - Adicionar funcionário
    2 - Consultar funcionário
    3 - Calcular folha de pagamento
    0 - Sair
    """)

def solicitando_dados():
    funcionario = Funcionario(
        matricula = input("Digite sua matricula: "),
        senha = input("Digite sua senha:"),
        nome = input("Digite seu nome: "),
        salario = float(input("Digite seu salario:")),
        dependentes = int(input("Digite quantos dependentes você tem: "))

    )   
    session.add(funcionario)
    session.commit()


def consultando_funcionario():
    matricula = input("Digite sua matricula: ")
    senha = input("Digite sua senha: ")

    funcionario = session.query(Funcionario).filter_by(matricula = matricula, senha = senha).first()

    if funcionario:
        print(f"Nome: {funcionario.nome}, Salário: R$ {funcionario.salario}, Dependentes: {funcionario.dependentes}")       
    else:
        print("Funcionario não encontrado.")

def calcular_inss(salario):
    if salario <= 1100:
        return salario * 0.075
    elif salario <= 2203.48:
        return salario * 0.09
    elif salario <= 3305.22:
        return salario * 0.12
    elif salario <= 6433.57:
        return salario * 0.14
    else:
        return 854.36

def calcular_irrf(salario, dependentes):
    if salario <= 2259.20:
        return 0
    elif salario <= 2826.65:
        return salario * 0.075
    elif salario <= 3751.05:
        return salario * 0.15
    elif salario <= 4664.68:
        return salario * 0.225
    else:
        return salario * 0.275 - (dependentes * 189.59)

def calcular_vale_transporte(salario, vale_transporte):
    if vale_transporte == 's':
        return salario * 0.06   
    else :
        return 0

def calcular_vale_refeicao(valor_vale_refeicao):
    return valor_vale_refeicao * 0.20

def calcular_plano_saude(dependentes):
    return dependentes * 150.00

def calcular_salario_liquido(salario, desconto_inss, desconto_irrf, desconto_vale_transporte, desconto_vale_refeicao, desconto_plano_saude):
    return salario - (desconto_inss + desconto_irrf + desconto_vale_transporte + desconto_vale_refeicao + desconto_plano_saude)

def calcular_folha(funcionario):
    salario_base = funcionario.salario
    dependentes = funcionario.dependentes
    
    vale_transporte = input("Deseja receber vale transporte? (s/n): ").lower()
    valor_vale_refeicao = float(input("Digite o valor do vale refeição fornecido pela empresa: R$ "))

    desconto_inss = calcular_inss(salario_base)
    desconto_irrf = calcular_irrf(salario_base, dependentes)
    desconto_vale_transporte = calcular_vale_transporte(salario_base, vale_transporte)
    desconto_vale_refeicao = calcular_vale_refeicao(valor_vale_refeicao)
    desconto_plano_saude = calcular_plano_saude(dependentes)

    salario_liquido = calcular_salario_liquido(
        salario_base, 
        desconto_inss, 
        desconto_irrf, 
        desconto_vale_transporte, 
        desconto_vale_refeicao, 
        desconto_plano_saude
    )
    print(f"""\nInformações do funcionário {funcionario.nome}: 
          Salário Base: R$ {salario_base:.2f}
          Dependentes: {dependentes}
          Vale Transporte: {vale_transporte}
          Vale Refeição: {valor_vale_refeicao}
          Salário Líquido: R$ {salario_liquido:.2f}
""")

while True:
    menu()
    opcao = input("Escolha uma opção: ")

    match opcao:
        case "1":
            solicitando_dados()
        case "2":
            consultando_funcionario()
        case "3":
            matricula = input("Digite sua matricula: ")
            senha = input("Digite sua senha: ")

            funcionario = session.query(Funcionario).filter_by(matricula = matricula, senha = senha).first()

            if funcionario:
                calcular_folha(funcionario)
            else:
                print("Funcionario não encontrado.")

        case "0":
            break

        case _:
            print("opção invalida.")
            continue


