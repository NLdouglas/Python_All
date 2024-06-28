nome=input("digite um nome: ")
idade=int(input("Digite sua idade: "))
doenca=input("suspeita doenca: ").upper()
if idade >=65:
    print("O paciente " + nome + "deve ser direcionado para sala de espera reservada.")
elif doenca == "SIM":
    print("O paciente " + nome + " deve ser direcionado para sala de espera reservada.")
else:
    print("O paciente " + nome + "Não possui atendimento prioritário e pode aguardar a sala comum")