# sana:28.08.2025

class oquvchi:
    def __init__(self,ism,familiya,tyil):
        self.ism = ism
        self.familiya = familiya
        self.tyil = int(tyil)

    def get_name(self):
            return self.ism

    def get_age(self,yil):
            return yil - self.tyil


    def tanishtir(self):
        return f"Ism:{self.ism}{self.familiya}\ntug'ilgan yil:{self.tyil}"
oquvchi1 = oquvchi("Alisher","Berdiyev","2011")
oquvchi2 = oquvchi("Asliddin","Berdiyev","1999")
oquvchi3 = oquvchi("Fazliddin","Berdiyev","2002")
print(oquvchi1.tanishtir())
print(f"Yosh:{oquvchi1.get_age(2025)}")