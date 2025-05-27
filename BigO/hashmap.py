class hashmap:
    def __init__(self, size=10):
        self.size = size
        self.table =[[] for _ in range(size)] # lista de listas

    def hash(self, key):
        return hash(key) % self.size # garante que o hash caia dentro do tamanho do array
    
    def insert(self, key, value):
        index = self.hash(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, value) # atualiza o valor se a chave já existir
                return
        self.table[index].append((key, value)) # adiciona nova chave-valor

    def get(self, key):
        index =self.hash(key)
        for k, v in self.table[index]:  # percorre a lista de chaves-valor ( evitar colisão)
            if k == key:   
                return v # se encontrar a chave, retorna o valor 
        return print("cannot find key")  

    def remove(self, key):
        index = self.hash(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                del self.table[index][i]
                return True, print("chave removida com sucesso")  # retorna True se a chave for removida
        return False  # retorna False se a chave não for encontrada
    


h = hashmap() # chamada a classe

h.insert("name", "Douglas")
h.insert("age", 30)
h.insert("city", "São Paulo")   

print(h.remove("name"))
print(h.get("name")) # deve retornar None ou mensagem de erro