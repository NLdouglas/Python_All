frutas = ["maçã", "banana", "maçã", "laranja", "banana", "banana"]

grupo = {}
for fruta in frutas:
    if fruta not in grupo:
        grupo[fruta] = 0
    grupo[fruta] += 1

print(grupo)