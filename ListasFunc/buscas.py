equipamentos=[]
valores=[]
serial=[]
departamento=[]
resposta = "S"
while resposta =="S":
    equipamentos.append(input("\nEquipamento: "))
    valores.append(float(input("Valor: ")))
    serial.append(input("SN: "))
    departamento.append(input("Departamento: "))
    print("------------------------")
    resposta = input("Digite \"S\" para continuar: ").upper()
busca=input("\nDigite o nome do equipamento que deseja buscar: ")
for indice in range(0, len(equipamentos)):
    if busca==equipamentos[indice]:
        print("Valor...", valores[indice])
        print("Serial...", serial[indice])
        print("Departamento...", departamento[indice])







