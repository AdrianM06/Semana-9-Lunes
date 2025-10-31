def partition(lista):
    menor = []
    mayor= []
    pivote = lista[0]
    for i in range(len(lista)):
        if lista[i] < pivote:
            menor.append(lista[i])
        elif lista[i] > pivote:
            mayor.append(lista[i])
    return menor, pivote, mayor


def quicksort(lista):
    if len(lista) < 2:
        return lista
    menores, pivote, mayores = partition(lista)
    return quicksort(menores) + [pivote] + quicksort(mayores)


def main():
    lista = [1,3,5,7,4,8,9,2,6]
    lista = quicksort(lista)
    print(lista)


main()