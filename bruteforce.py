import itertools

def possibilities(n,m):
    arrSolusi = [x for x in range(m)]
    return [p for p in itertools.product(arrSolusi, repeat=n)]

def evaluate(solusi, arrData, arrMemori):
    memAlloc = []
    for m in arrMemori:
        memAlloc.append(m)
    nZero = 0

    for i in range(len(solusi)):
        memAlloc[solusi[i]] -= arrData[i]
        if memAlloc[solusi[i]] < 0 :
            return False, -1

    for i in range(len(memAlloc)):
        if memAlloc[i]==0:
            nZero += 1
    
    return True, nZero

def main():
    print("Masukkan nilai n nam m")
    n = int(input()) 
    m = int(input())

    arrData = []
    arrMemori = []
    solusi = []

    print("Masukkan array ukuran program:")
    for i in range(n):
        x = int(input())
        arrData.append(x)

    print("Masukkan array ukuran ruang memori:")
    for i in range(m):
        y = int(input())
        arrMemori.append(y)
    
    unsuitable = 0
    arrSolution = possibilities(n, m)
    chosen, maxZero = evaluate(arrSolution[0], arrData, arrMemori)
    if chosen:
        solusi.append(arrSolution[0])
    for i in range(1,len(arrSolution)):
        chosen, nZero = evaluate(arrSolution[i], arrData, arrMemori)
        if chosen :
            solusi.append(arrSolution[i])
            maxZero = nZero
        else:
            unsuitable+=1

    print(solusi)
    print("Unsuitable: ", unsuitable)
    

if __name__=="__main__":
    main()