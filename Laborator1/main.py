from math import sqrt
# numarul meu - 13
from queue import Queue
"""
    functie de teste 
"""
def teste():
    assert pr2(1, 5, 4, 1) == 5.0
    assert pr2(0, 0, 0, 0) == 0.0
    assert pr2(5, 2, 11, 10) == 10.0
    assert pr2(-1, 5, -4, 1) == 5.0
    assert pr2(5, 2, -11, -10) == 20.0
    assert pr2(5, 6, 9, 10) == 5.656854249492381

    assert pr10([[0, 0, 0, 1, 1], [0, 1, 1, 1, 1], [0, 0, 1, 1, 1]], 3, 5) == 2
    assert pr10([[0, 0, 1, 1], [0, 0, 0, 1], [0, 0, 1, 1]], 3, 4) == 1
    assert pr10([], 0, 0) == False
    assert pr10([[1, 1, 1, 1], [0, 0, 1, 1], [1, 1, 1, 1], [0, 1, 1, 1]], 4, 4) == 1
    assert pr10([[0, 0, 1, 1], [0, 1, 1, 1]], 0, 5) == False

    assert pr10brut([[0, 0, 0, 1, 1], [0, 1, 1, 1, 1], [0, 0, 1, 1, 1]], 3, 5) == 2
    assert pr10brut([[0, 0, 1, 1], [0, 0, 0, 1], [0, 0, 1, 1]], 3, 4) == 1
    assert pr10brut([], 0, 0) == False
    assert pr10brut([[1, 1, 1, 1], [0, 0, 1, 1], [1, 1, 1, 1], [0, 1, 1, 1]], 4, 4) == 1
    assert pr10brut([[1, 1, 1, 1], [0, 1, 1, 1]], 2, 0) == False

    assert pr1(['ana', 'are', 'mere', 'si', 'are', 'pere']) == 'si'
    assert pr1([]) == False

    assert pr4(['ana', 'are', 'mere', 'si', 'are', 'pere']) == ['ana', 'mere', 'pere', 'si']
    assert pr4([]) == False
    assert pr4(['ana']) == ['ana']
    assert pr4(['ana', 'ana']) == []
    assert pr4(['ana', 'are', 'ana']) == ['are']
    assert pr4(['ana', 'are']) == ['ana', 'are']

    assert pr3brut([1,0,2,0,3],[1,2,0,3,1]) == 4
    assert pr3brut([1,2,3,4,5],[1,2,3]) == False

    assert pr5([1,2,3,4,2]) == 2
    assert pr5([1,3,4,2,5,3]) == 3
    assert pr5([1,1,2]) == 1

    assert pr6([2,8,7,2,2,5,2,3,1,2,2]) ==  2
    assert pr6([1,9,1]) == 1
    assert pr6([1,2,3]) == False
    assert pr6([]) == False

    assert pr7([7,4,6,3,9,1],2) == 7
    assert pr7([1,3,5,2],3) == 2
    assert pr7([9,8,5,10,3,2],6) == 2

    assert pr8(4) == ["1","10","11","100"]
    assert pr8(1) == ["1"]
    assert pr8(10) == ["1","10","11","100","101","110","111","1000","1001","1010"]

"""
    problema 2
    in : 4 intregi , de tipul : prima coordonata a primului punct , a doua coordonata a primului punct 
                                prima coordonata a punctului secund , a doua coordonata a punctului secund
    out : un numar real , reprezentand valoarea distantei dintre cele doua puncte 
    complexitate : O(1)
    folosim formula distantei in plan
"""
def pr2(xa, ya, xb, yb):
    lungime = sqrt((xb - xa) * (xb - xa) + (yb - ya) * (yb - ya))
    return lungime
"""
    in : matrice , numarul de linii , numarul de coloane 
    out : intreg, numarul liniei care are cele mai multe valori de 1 
    complexitate : O(1) - best case , O(n) - worst case 
    parcurgem matricea mai intai pe fiecare coloana , si daca gasim o linie care are valoare de 1 , inseamna ca ea 
        va avea cele mai multe valori 
"""
def pr10(matrice, linii, coloane):
    if matrice == [] or linii == 0 or coloane == 0:
        return False
    for j in range(0, coloane):
        for i in range(0, linii):
            if matrice[i][j] == 1:
                return i + 1
"""
    acelasi input si output , doar ca varianta aceasta calculeaza suma pe fiecare linie si returneaza indicele liniei
    cu suma maxima 
    complexitate : O(n^2) in timp , plus ca folosim un vector auxiliar
"""
def pr10brut(matrice, linii, coloane):
    if matrice == [] or linii == 0 or coloane == 0:
        return False
    aparitii = [0] * linii
    for i in range(0, linii):
        s = 0
        for j in range(0, coloane):
            s = s + matrice[i][j]
        aparitii[i] = s
    maxim = 0
    poz = 0
    for i in range(0, len(aparitii)):
        if aparitii[i] > maxim:
            maxim = aparitii[i]
            poz = i
    return poz + 1
"""clasic merge sort"""
def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        mergeSort(left)
        mergeSort(right)
        i = j = k = 0
        # interclasare
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        # daca ramane in stanga
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        # daca ramane in dreapta
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
"""
    in: lista de stringuri - propozitia data 
    output : lista de stringuri , cele ce apar doar o data 
    complexitate : O(n log n )
"""
def pr4(sentence):
    mergeSort(sentence)
    if not sentence:
        return False
    rezultat = []
    if len(sentence) == 1:
        rezultat.append(sentence[0])
        return rezultat
    if sentence[0] != sentence[1]:
        rezultat.append(sentence[0])
    for i in range(1, len(sentence) - 1):
        if sentence[i] != sentence[i + 1] and sentence[i] != sentence[i - 1]:
            rezultat.append(sentence[i])
    if sentence[len(sentence) - 1] != sentence[len(sentence) - 2]:
        rezultat.append(sentence[len(sentence) - 1])
    return rezultat
"""
    in: lista de stringuri
    output : ultimul string 
    complexitate : O( n log n )
"""
def pr1(sentence):
    mergeSort(sentence)
    if not sentence:
        return False
    return sentence[-1]

#pana aici am prezentat in primul lab : 4 probleme din care o problema(10) in 2 feluri




"""in:vectorii de numere
   out:produsul scalar al vectorilor , intreg
   complexitate : O(n)"""
def pr3brut(a,b):
    produs = 0
    if len(a) != len(b):
        return False
    for i in range(0,len(a)):
        produs = produs + a[i]*b[i]
    return produs

"""
    in: vector de numere, cu valori de la 1 la n-1  
    out: intreg , valoarea ce apare de 2 ori 
    complexitate : O(n) ,calculam sumele """
def pr5(sir):
    n = len(sir) - 1
    sumaTeoretica = n*(n+1)/2
    sumaActuala = 0
    for i in range(0,len(sir)):
        sumaActuala = sumaActuala + sir[i]
    return sumaActuala - sumaTeoretica
"""
    in: vector de numere
    out: intreg-element majoritar sau valoare False
    complexitate : O(n^2)"""
def pr6(lista):
    n = len(lista)
    maxim = 0
    index = -1
    for i in range(n):
        count = 0
        for j in range(n):
            if(lista[i] == lista[j]):
                #de cate ori apare un element in vector
                count = count + 1
        #daca e maxim , actualizam
        if(count > maxim):
            maxim = count
            index = i
    #daca e majoritar, returnam
    if(maxim > n//2):
        return lista[index]
    else:
        return False
"""
    in: vector de numere, k-intreg, al catalea element se doreste
    out: intreg , elementul dorit 
    complexitate : O(n log n)"""
def pr7(lista,k):
    n = len(lista)
    mergeSort(lista)
    return lista[n-k]

"""
    in: intreg, valoarea maxima pana la care mergem
    out: vector de valori binare
    complexitate : O(n)"""
def pr8(n):
    q = Queue()
    #incepem cu valoarea 1
    q.put("1")
    #lista rezultat
    lista = []
    #pt fiecare iteratie de la 1 la n
    while n>0 :
        n = n-1
        #scoatem valoarea din coada
        front = q.get()
        #punem valorea in lista rezultat
        lista.append(front)
        store = front
        q.put(front+"0")
        q.put(store+"1")
    return lista


"""functie main"""
def main():
    print("incepem teste")
    teste()
    #print(pr8brut(10))
    print("terminam teste ")
main()
