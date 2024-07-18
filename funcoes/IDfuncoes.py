def preencherInventario(lista):
    resp="S"
    while resp == "S":
        equipamento=[input("Equipamento: "),
                int(input("Digite o ID: ")),
                float(input("Valor: ")), 
                (input("Número Serial: ")),
                input("Departamento: ")]   
        lista.append(equipamento)
        resp = input("Digite \"S\" para continuar: ").upper()

def exibirInventario(lista):
    for elemento in lista:
        print("ID......: ", elemento[1])
        print("Nome.....: ", elemento[0])
        print("Valor.....: ", elemento[2])
        print("SN.....: ", elemento[3])
        print("Departamento.....: ", elemento[4])

def localizarPorNome(lista):
    busca=input("Digite o ID do equipamento que deseja buscas: ")
    for elemento in lista:
        if busca == elemento[0]:
            print("Valor: ", elemento[2])
            print("SN: ", elemento[3])