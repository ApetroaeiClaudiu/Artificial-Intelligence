from math import sqrt

#O(1)
def pr2():
    xa = int(input("prima coordonata, primul punct :"))
    ya = int(input("a doua coordonata, al doilea punct :"))
    xb = int(input("prima coordonata, al doilea punct :"))
    yb = int(input("a doua coordonata, al doilea punct :"))
    distanta = sqrt((yb-ya)*(yb-ya) + (xb-xa)*(xb-xa))
    print(distanta)

#O(n log n)
def pr4():
    sentence = input("da string: ")
    words = sentence.split()
    words.sort()

    if words[0] != words[1]:
        print(words[0])

    for i in range(1,len(words)-1):
        if words[i] != words[i+1] and words[i] != words[i-1]:
            print(words[i])

    if words[len(words)-1] != words[len(words) - 2]:
        print(words[len(words)-1])

#O(n)
def pr5():
    sir = []
    lungime = int(input("da numarul de elemente: "))
    for i in range(0,lungime):
        ele = int(input("element: "))
        sir.append(ele)

    aparitii = [0]*(lungime)

    for i in range(0,len(sir)):
        if aparitii[sir[i]] != 0 :
            print(sir[i])
            break
        else:
            aparitii[sir[i]] = aparitii[sir[i]] + 1

#O(1) catre O(n)
def pr10():
    #creare matrice
    matrice = []
    n = int(input("nr de linii : "))
    m = int(input("nr de coloane : "))
    for i in range(0,n):
        linie = []
        for j in range(0,m):
            ceva = int(input("valoare"))
            linie.append(ceva)
        matrice.append(linie)
    #rezolvare
    for j in range(0,m):
        for i in range(0,n):
            if matrice[i][j] == 1:
                print(j+1)
                break
        else:
            continue
        break

pr10()
