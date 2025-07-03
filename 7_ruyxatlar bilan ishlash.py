#sana:20.06.2025
#7-dars
#mavzu:ruyxatlar bilan ishlash
#tartiblash
humans=["Alisher","Asliddin","Fazliddin","Zarina"]
#sort funksiya matnlarni alifbo buyicha yozi keladi
humans.sort()
print(humans)


#teskari tartibda joylashtirish
humans=["Fazliddin","Asliddin","Zarina","Alisher"]
humans.sort(reverse=True)
print(humans)


 #ruyxatni teskari qilish ya'ni matn oxiridai suzlarni matn boshidan boshlab yozish
ranglar=["yashil","oq","sariq","qora"]
ranglar.reverse()
print(ranglar)

#ruyxat uzunligini bilish
#bu len funksiyasi bilan yasaladi
len(ranglar)

#range funksiyasi bu ma'lum bir oraliqdagi ma'lumotlarni qaytaradi
alisher=list(range(2000,2011))
print(alisher)

#qadamlar
toq_sonlar=list(range(11,25,2))
print(toq_sonlar)


juft_sonlar=list(range(0,35,2))
print(juft_sonlar)

max_qiymat=max(toq_sonlar)
print(max_qiymat)

min_qiymat=min(juft_sonlar)
print(min_qiymat)

jami=sum(toq_sonlar)
print(jami)

print(toq_sonlar[2])

print(toq_sonlar[0:3])

my_number=toq_sonlar[:]
print(my_number)


my_number.remove(15)
print(my_number)
print(toq_sonlar)

#tuple funksiyasi uzgarmas uzgaruvchi bunga ma'lumot qushib bulmaydi
meva=("olma","banan","shaftoli")
meva=list(meva)
meva.append("xurmo")
meva=tuple(meva)
print(meva)