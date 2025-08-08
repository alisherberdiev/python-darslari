import random as r # random modulini r deb chaqirayapmiz

son = r.randint(0,100) # 0 va 100 oralig'ida tasodifiy son
print(son)

#----------------------------------------------------------------------------------|
#choice()--->>>tasodifiy bitta qiymat topib beradi
ismlar=['Alisher','Asliddin','Husan','Zarina','Fazliddin']
ism=r.choice(ismlar)
print(ism)
#endi bu ism o'zgaruvchi ichidan ham tasodifiy bitta harf tanlab oladi
print(r.choice(ism))

x=list(range(1,1000,7))
print(x)
print(r.choice(x))
#----------------------------------------------------------------------------------|
#shuffle()---->>>aralashtirib tashlaydi
x=list(range(25))
print(x)
r.shuffle(x)
print(x)