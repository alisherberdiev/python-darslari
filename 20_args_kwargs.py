#sana:07.08.2025
def summa(*sonlar):
    """Kiritilgan sonlar yig'indisini hisoblaydi"""
    yigindi = 0
    for son in sonlar:
        yigindi += son
    return yigindi

print(summa(1,5))
print(summa(1,2,3,4,5,6,7,8,9))
print(summa(9,15))

#----------------------------------------------------

def avto_info(kompaniya,model,**malumotlar):
    """Avto haqidagi ma'lumotlar qaytaruvchi funksiya"""
    malumotlar['kompaniya']=kompaniya
    malumotlar['model']=model
    return malumotlar

avto1=avto_info("GM","camaro",rang="qora",yili=2025,holati="yangi")
avto2=avto_info("BMW","M5 cs",rang="yashil",yili=2022)
print(avto1)
print(avto2)