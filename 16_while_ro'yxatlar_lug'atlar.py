#sana:26.07.2025
#ismlar=[]
#n=1
#while True:
#    savol=f"{n}-do'stingizni ismini kiritng:"
#    ism=input(savol)
#    ismlar.append(ism)
#    takrorlash=input("Yana ism qo'shmoqchimisiz?  (ha/yo'q)")
#    n+=1
#    if takrorlash != "ha":
#        break


#---------------------------------------------------------------
#print("do'stlaringiz yoshini saqlaymiz")
#dostlar={}
#ishora=True
#while ishora:
#    ism=input("Do'stingizning ismini kiritng:")
#    yosh= input((f"{ism.title()}ning yoshini kiriting:"))
#    dostlar[ism]=int(yosh)

#    javob=input("Yana ma'lumot kiritmoqchimisiz? (ha/yoq)")
#    if javob=="yoq":
#        ishora =False

#for ism,yosh in dostlar.items():
#    print(f"{ism.title()} {yosh} yoshda")

#----------------------------------------------------------------

#cars=["lacetti","nexia","toyota","nexia","malibu"]
#car="nexia"
#while car in cars:
#    cars.remove(car)
#print(cars)

#-----------------------------------------------------------------

talabalar=["Alisher",'Asliddin','Zarina','Fazliddin']
baholangan_talabalar={}
while talabalar:
    talaba=talabalar.pop()
    baho=input(f"{talaba.title()}ning bahosini kiriting:")
    print(f"{talaba.title()} baholandi")
    baholangan_talabalar[talaba]=int(baho)