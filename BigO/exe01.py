import time

def eh_par(numero):
    return numero % 2 == 0



def eh_par_lento(numero):
    for i in range(numero):
        pass
    return numero % 2 == 0

n = 10**7

start = time.time()
eh_par_lento(n)
print("Tempo de execução da função lenta:", time.time() - start)#O(n)



start = time.time()
eh_par(n)
print("Tempo de execução da função rápida:", time.time() - start)#O(1)  