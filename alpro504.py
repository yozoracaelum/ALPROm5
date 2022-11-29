# Percobaan 4: Mengakses string sebagai list
# alpro504.py

abjad = "abcdefghijklmnopqrstuvwxyz"
n = 0

for i in abjad:
    print (str(n) + ". " + i)
    n += 1
    
print(abjad[11].upper() + abjad[0] + abjad[1])