import random as r

sonlar = r.sample(range(1010),15)
print(sonlar)
def juftmi(x):
    """x juft bo'lsa True,aks holda False qaytaruvchi funksiya"""
    return x%2==0

#juft_sonlar=list(filter(juftmi,sonlar))
#print(juft_sonlar)

juft_sonlar=list(filter(lambda x:x%2==0,sonlar))
print(juft_sonlar)
#----------------------------------------------------------------->>>>>>
mevalar=["olma","anor","shaftoli","nok"]
harf="o"
mevalar_o=list(filter(lambda meva:meva.startswith(harf),mevalar))
print(mevalar_o)



mevalar2=list(filter(lambda meva:len(meva)<=5,mevalar))
print(mevalar2)

mevalar3=list(filter(lambda meva:(meva.startswith("o") and meva.endswith("a")),mevalar))
print(mevalar3)