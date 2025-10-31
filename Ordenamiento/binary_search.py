from quicksort import quicksort 

def search(lista, opt):
    if len(lista) == 0:
        return None
    mid = len(lista) // 2
    if opt == lista[mid]:
        return opt
    elif opt < lista[mid]:
        return search(lista[0:mid], opt)
    else:
        return search<(lista[mid+1:], opt)


def main():
    opt = int(input("Valor: "))
    lista = [1,3,5,7,4,8,9,2,6]
    lista = quicksort(lista)
    print(search(lista, opt))


main()