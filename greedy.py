def main():
    print("Masukkan nilai n nam m")
    n = int(input()) 
    m = int(input())

    arrData = []
    arrMemori = []
    solusi = []

    print("Masukkan array ukuran program: (Terurut mengecil)")
    for i in range(n):
        x = int(input())
        arrData.append(x)

    print("Masukkan array ukuran ruang memori:")
    for i in range(m):
        y = int(input())
        arrMemori.append(y)

    for i in range(n):
        closest = arrMemori[0] - arrData[i]
        choice = 0
        for j in range(1,m):
            if arrMemori[j]-arrData[i] < closest and arrMemori[j]-arrData[i]>=0:
                closest = arrMemori[j] - arrData[i]
                choice = j
        solusi.append(choice)
        arrMemori[choice]-=arrData[i]
        print(arrMemori)
            
    print(solusi)


if __name__=="__main__":
    main()