v=[-9,2,-5,-4,6]
v

def sumaSubMax1(v:list): #-> number:int
    n=len(v) #5
    sumaMax=0 #0

    for i in range(0,n): #0...4
        estaSuma = 0
        for j in range(i,n): #0...4
            estaSuma += v[j]
            if estaSuma > sumaMax:
                sumaMax=estaSuma
    return sumaMax
            

def sumaSubMax2(v:list):
    n=len(v)
    estaSuma=0
    sumaMax=0

    for j in range(0,n):
        estaSuma+=v[j]
        if estaSuma > sumaMax:
            sumaMax=estaSuma
        elif estaSuma < 0:
            estaSuma=0
    return sumaMax




#Comprobar con ejemplo dado
def test1():
    v=[[-9,2,-5,-4,6],[4,0,9,2,5],[-2,-1,-9,-7,-1],[9,-2,1,-7,-8],[15,-2,-5,-4,16],[7,-5,6,7,-7]]

    for i in range(0,len(v)):
        a = sumaSubMax1(v[i])
        b = sumaSubMax2(v[i])
        print(v[i], a, b, a == b )
        




#Comprobar con números aleatorios
def aleatorio(n):
    import random
    v=list(range(n))
    for i in v:
        v[i] = random.randint(-n, n)
    return v

def test2():
    l=[]
    for i in range(0,9):
        n=aleatorio(9)
        l.append(n)

    for i in range(0,len(l)):
        a = sumaSubMax1(l[i])
        b = sumaSubMax2(l[i])
        print(l[i], a, b, a == b )

    


test2()
