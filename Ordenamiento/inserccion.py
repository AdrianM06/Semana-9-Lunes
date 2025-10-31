
def main():
    lista = [1,3,5,7,4,8,9,2,6]
    for i in range(len(lista)):
        aux = lista[i]
        j = i-1
        while j >= 0 and aux < lista[j]:
            lista[j+1] = lista[j]
            j -= 1
        lista[j+1] = aux
    
    print(lista)

main()