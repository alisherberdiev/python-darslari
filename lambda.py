#sana:12.08.2025
import math
uzunlik=lambda pi,r:2*pi*r
print(uzunlik(math.pi,10))

kvadrat=lambda x,y:x**y
print(kvadrat(3,2))


def daraja(n):
    return lambda x:x**n
kvadrat=daraja(2)
kub=daraja(3)
kv=f"3 ning kvadrati {kvadrat(3)} ga"
kb=f"kubi {kub(3)} ga teng"
print(f"{kv}, {kb}")