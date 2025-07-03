#sana:24.06.2025
#9-dars
#mavzu:if-else-tarmoqlanish
#cars=['spark','bmw','byd','cherry']
#for car in cars:#mashinalar ichidagi har bitta mashina olish uchun
#    if car=='byd':#agar moshin 'byd'ga teng bo'lsa
#        print(car.upper())#moshinni hamma harflarini kattartirish
#    if car=='bmw':
#        print(car.upper())#bu ham hamma harflarni kattartirish
#    else:#aks holda
#        print(car.title())#moshin nomini faqat 1-harfini katta yozish


#ism=input("ismingiz nima?\n>>>")
#if ism.lower() !="alisher":
#    print(f"Uzr,{ism.title()} biz Alisherni chaqiryapmiz.")
#else :
#    print("Alisher kel")


#javob=float(input("125-25 nechiga teng\n>>>"))
#if javob!=100:
#    print("javob xato")

#yosh=int(input("Yoshingiz nechida?\n>>>"))
#if yosh>=15:
#    msg="Xush kelibsiz"
#else:
#    msg="kirish taqiqlanadi"
#print(msg)


#login=input("Yangi login tanlang\n>>>")
#if len(login)<=5:
#    print("Login 5ta  harfdan ko'p bulishi shart!")


yil=int(input("Tug'ilgan yilingizni kiriting\n>>>"))
if 2025-yil<=14:
    print(f"Yoshingiz {2025-yil}da ekan")
    print("kirish mumkin emas")
else:
    print("Xush kelibsiz")
