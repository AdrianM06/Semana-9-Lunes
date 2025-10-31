
def main():
    lista = [1,3,5,7,4,8,9,2,6]
    for i in range(len(lista)):
        min_idx = i
        for j in range(i+1, len(lista)):
            if lista[min_idx] > lista[j]:
                min_idx = j
        temp = lista[min_idx]
        lista[min_idx] = lista[i]
        lista[i] = temp
    
    print(lista)

main()