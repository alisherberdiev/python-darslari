from math import sqrt#------------>>>sqrt- ildiz hisoblaydi

sonlar=list(range(11))
#ildizlar=list(map(sqrt,sonlar))
#print(ildizlar)

#def daraja2(x):
#    """Berilgan sonning kvadratini hisoblovchi funksiya"""
#    return x*x
#print(list(map(daraja2,sonlar)))

#kvadratlar = list(map(lambda x:x*x,sonlar))
#print(kvadratlar)

a=[1,2,3,4,5]
b=[6,7,8,9,0]
a_plus_b=list(map(lambda x,y:x+y,a,b))
print(a_plus_b)