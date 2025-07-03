#sana:23.06.2025
#8-dars
#mavzu:FOR LOOP
#cars=["camaro","bmw","lacetti"]

#for-bu sikl

#for car in cars:
#    print('Mana',car)
#    print("Ana",car)

#cars=["bmw",'byd','kia']
#for car in cars:
#    print(f"Hurmatli haydovchi {car},mashinangizni oling")
#    print("beruvchi: Qashqadaryo viloyat IIV ")


#sonlar=list(range(1,100))
#for son in sonlar:
#    print(f"{son}ning kvadrati {son**2}")


#sonlar=list(range(99))
#sonlar_kvadrati=[]
#for son in sonlar:
#    sonlar_kvadrati.append(son**2)
#print(sonlar)
#print(sonlar_kvadrati)

#dostlar=[]
#print("5ta eng yaqin dustingiz kim?")
#for n in range(5):
#    dostlar.append(input(f"{n+1}-dustingizni ismini kiriting"))
#print(dostlar)



#AMALIYOT
       #Kamida 5 elementdan iborat ismlar degan ro'yxat tuzing, va ro'yxatdagi har bir ismga takrorlanuvchi xabar yozing
#ismlar=["Alisher","Asliddin",'Fazliddin','Zarina','Asliddin']
#for ism in ismlar:
#    print(f"Salom {ism}")
#n=5
#print(f"kod {n} marta takrorlandi")


    #10 dan 100 gacha bo'lgan toq sonlar ro'yxatini tuzing. Ro'yxatning xar bir elementining kubini yangi qatordan konsolga chiqaring.
#toq_sonlar=list(range(10,100,2))
#toq_sonlar_kvadrati=[]
#for son in toq_sonlar:
#    toq_sonlar_kvadrati.append(son**3)
#print(toq_sonlar)
#print(toq_sonlar_kvadrati)

    #Foydalanuvchidan 5 ta eng sevimli kinolarini kiritshni so'rang, va kinolar degan ro'yxatga saqlab oling. Natijani konsolga chiqaring.
#kinolar=[]
#print("5ta eng sevimli kinongiz nomini kiritng?")
#for n in range(5):
#    kinolar.append(input(f"{n+1}-kinoni nomini kiriting"))
#print(kinolar)


    #Foydalanuvchidan bugun nechta odam bilan uchrashganini (suhbatlashganini) so'rang, va har bir suhbatlashgan odamning ismini birma-bir so'rab ro'yxatga yozing. Ro'yxatni konsolga chiqaring
odamlar=[]
suhbatlar_soni = int(input(f"Bugun nechi kishi bn suhbatlashdingiz\n>>> "))
for n in range(suhbatlar_soni):
    odamlar.append(input(f"{n+1}-suhbatlashgan odamingiz kim edi?"))
print(odamlar)