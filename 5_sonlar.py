#5-dars
#mavzu-sonlar
#sana:18.06.2025
a=15
b=75
yosh=14
#sonning turini qandayligini bilish uchun ishlatamiz
print(type(b))
#sonni qiynalmay o'qishimiz uchun pastki chiziqcha quyib yozsak ham buladi
kucha_soni=758_961_456_789
print("Kuchalar soni: ",kucha_soni)

x,y,z=12,14,16
c=b/a
print(c)
#shuni unli emas butun qism qilib olish uchun "//"  buni ishlatamiz
c=b//a
print(c)

#uzgaruvchini uzgarmas qiymat olishi uchun uzgaruvchi nomini katta harlarda yozamiz
radius=15
PI=3.14
diametr=2*radius
print("Aylana uzunligi ",PI*diametr)

#bu kod terminalda xato chiqadi chunki xabar degan uzgaruvchi ichiga son bilan matn yozyapmiz
ism="Alisher"
yosh=14
   #xabar=ism+" "+yosh+"yoshda"
   #print(xabar)

#shu sonni matnga aylantirish uchun str(uzgaruvchi nomi)deb yozish kerak
xabar=ism+" "+str(yosh)+" "+"yoshda"
print(xabar)

#bu kod xato chiqadi chunki input har qnday narsani matn kurinishida saqlaydi
   #t_yili=input("Tug'ilgan yilingizni kiriting")
   #yosh=2025-t_yili
   #print("siz",yosh,"yoshda ekansiz")

#bu kodni ishlatish uchun int(input(matn)) shuni yozish kerak
t_yili=int(input("Tug'ilgan yilingizni kiriting"))
yosh=2025-t_yili
print("siz",yosh, "yoshda ekansiz")






                          #AMALYOT
#Foydalanuvchi kiritgan sonning kvadrati va kubini konsolga chiqaruvchi dastur
#son=int(input("istalgan soningini yozing\n>>>"))
#print(son,"ning kvadrati",son**2,"ga teng va kubi",son**3,"ga teng")

#Foydalanuvchining yoshini so'rab, uning tug'ilgan yilini hisoblab, konsolga chiqaruvchi dastur
#yosh=int(input("yoshingiz nechida?\n>>>"))
#xabar=2025-yosh
#print("Siz",xabar,"-yil ekansiz")

#Foydalanuvchidan ikki son kiritshni so'rab, kiritilgan sonlarning yig'indisi, ayirmasi, ko'paytmasi va bo'linmasini chiqaruvchi dastur
son1=int(input("1-soningizni kiriting\n>>>"))
son2=int(input("2-soningizni kiriting\n>>>"))
puls=son1+son2
minus=son1-son2
kupaytirish=son1*son2
bulish=son1/son2
print(son1,"+",son2,"=",puls)
print(son1,'-',son2,"=",minus)
print(son1,"*",son2,"=",kupaytirish)
print(son1,"/",son2,"=",bulish)