#sana:10.07.2025
#dars:13
#mavzu:lug'at elementlari bilan ishlash
talaba={
    "ismi":"Alisher",
    "yosh":"14",
    "tug'ulgan yili":"2011"
    }

for key,qiymat in talaba.items():
    print(f"key:{key}")
    print(f"qiymat:{qiymat}")


cars={
    "Alisher":"BMW m5",
    "Asliddin":"bmw m8"
    }
for key,value in cars.items():
    print(f"{key}ning mashinasi {value}")



#.key()
odamlar={
    "Asliddin":"1999",
    "Fazliddin":"2002",
    "Zairna":"2004",
    "Alisher":"2011"
    }
print(odamlar.keys())

print("Uydagi insonlar:")
for odam in odamlar.keys():
    print(odam)



ishchilar={
    "Robot":"8",
    "Suvchi":"7",
    "Tozalovchi":"9",
    "Bog'bon":"11"
    }

ruyxat=["Suvchi","elektrik","Bog'bon","ustoz","Robot","ximik"]
for ishchi in ishchilar:
    if ishchi in ruyxat:
        print(f"{ishchi.title()} uchun {ishchilar[ishchi]} da ish boshlanadi ")



for ishchi in ruyxat:
    if ishchi not in ishchilar:
        print(f"Iltimos bu maktabga {ishchi} kerak")