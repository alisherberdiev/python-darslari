#4-dars
#mavzu:strings
#sana:17.06.2025
from msilib.schema import Billboard

ism="Alisher"
print("Mening ismim "+ism)

ism="Asliddin"
familiya="Berdiyev"
print(ism+familiya)

#orasini ochib yozish
print(ism+" "+familiya)

  #f-string
ism="john"
familiya='tom'
ism_sharif=f"{ism}  {familiya}"
print(ism_sharif)

belgi="qizil"
narsa="satil"
buyum=(f"Salom bu bizning {belgi} {narsa}imiz")
print(buyum)

#maxsus belgilar
print("Salom Alisher")
   #uzun joy tashlash
print("Salom \tAlisher")
   #qatorni bulish
print("Salom \nAlisher")

#string metodlar

  #.upper-so'zni katta harflarda yozad
ism ='john'
familiya ="tom"
ism_sharif=f"{ism} {familiya}"
print(ism_sharif)
print(ism_sharif.upper())
  #.lower-so'zni kichik harflarda yozadi
ism="Alisher"
familiya="Beriyev"
ism_sharif=f"{ism} {familiya}"
print(ism_sharif)
print(ism_sharif.lower())
  #.title-matndagi so'zni 1-harfini katta harf bilan yozadi
ism="Alisher"
familiya="berdiyev"
ism_sharif=f"{ism} {familiya}"
print(ism_sharif)
print(ism_sharif.title())
  #.capitalize-matnning 1-harfini katta harfda yozadi
ism="alisher"
familiya="Berdiyev"
ism_sharif=f"{ism} {familiya}"
print(ism_sharif)
print(ism_sharif.capitalize())

meva="     banan       "
print(meva)
#chap tomonda bushliq qoldirmaslik
print("U "+meva.lstrip()+"yoqtiradi")
#ung tomonda bushliq qoldirmaslik
print("U "+meva.rstrip()+" yoqtiradi")
#ikkala tomonda ham bushliq qoldirmaslik
print("U "+meva.strip()+" yoqtiradi")


#Input-foydalanuvchi kiritadigan matn
ism=input("yoshing nechida")
print("Salom "+ism+"daman")

ism=input("yoshingiz nechida\n>>>")
print("Salom "+ism.title())
