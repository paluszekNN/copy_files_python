import os
import shutil
import time
tab = []
plik = open('foldery.txt')
tab = plik.readlines()
for i in range(tab.__len__()-1):
    tab[i]=tab[i][:len(tab[i])-1]
print(tab)

czas=time.localtime()
test = str(czas[0])+'.'+str(czas[1])+'.'+str(czas[2])

try:
    os.makedirs(test)

except WindowsError:
    print("jest już taki folder")

for i in tab:
    listf = os.listdir(i)
    for j in listf:
        shutil.copyfile(i+"\\"+j, test+"\\"+j)
