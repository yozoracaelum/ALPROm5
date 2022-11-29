# Percobaan 3: List 2 dimensi
# alpro503.py

list_all=[[10,20,30,40,20],["kata",1,'A',3],[1.0,2.0,'string2',1E-20]]

for i in list_all:
    for j in i:
        print(str(j) + " adalah anggota himpunan " + str(i))
    print("\n")