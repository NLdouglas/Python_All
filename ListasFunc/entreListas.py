inventario=[]
resposta = "S"

while resposta == "S":
    equipamento=[input("Equipamento: "),
                int(input("Digite o ID: ")),
                float(input("Valor: ")), 
                (input("Número Serial: ")),
                input("Departamento: ")]   
    inventario.append(equipamento)
    resposta = input("Digite \"S\" para continuar: ").upper()

for elemento in inventario:
    print("ID......: ", elemento[1])
    print("Nome.....: ", elemento[0])
    print("Valor.....: ", elemento[2])
    print("SN.....: ", elemento[3])
    print("Departamento.....: ", elemento[4])
print("\n-----------------------------------------------------")

busca=input("Digite o ID do equipamento que deseja buscas: ")
for elemento in inventario:
    if busca == elemento[0]:
        print("Valor: ", elemento[2])
        print("SN: ", elemento[3])
print("--------------------------------------------")

depreciacao=input("\nDigite o ID do equipamento que sera depreciado: ")
for elemento in inventario:
    if depreciacao == elemento[0]:
        print("Valor antigo: ", elemento[2])
        elemento[2] = elemento[2] * 0.9
        print("Novo valor: ", elemento[2])

serial=int(input("\nDigite o SN do equipametno que sera deletado: "))
for elemento in inventario:
    if elemento[3] ==serial:
        inventario.remove(elemento)

print("---------------------------------------------------------")

for elemento in inventario:
    print("ID......: ", elemento[0])
    print("Nome.....: ", elemento[1])
    print("Valor.....: ", elemento[2])
    print("SN.....: ", elemento[3])
    print("Departamento.....: ", elemento[4])   

valores=[]
for elemento in inventario:
    valores.append(elemento[2])
if len(valores)>0:
    print("o equipamento mais caro custa: ", max(valores))
    print("O equipamento mais barato custa: ", min(valores))
    print("O total de equipamentos é de: ", sum(valores))