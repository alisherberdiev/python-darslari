# sana:29.08.2025
class oquvchi:
    """Oquvchi nomli klass yaratamiz"""
    def __init__(self,ism,familiya,tyil):
        """Oquvching xususiyatlari"""
        self.ism = ism
        self.familiya = familiya
        self.tyil = int(tyil)
        self.sinf = 1

    def get_info(self):
        """oquvchi haqida ma'lumat beradi"""
        return f"{self.ism} {self.familiya} . {self.sinf}-oquvchisi"

    def get_name(self):
        """Oquvchining ismini qaytaradi"""
        return self.ism

    def get_lastname(self):
        """oquvchining familiyasini qaytaradi"""
        return self.familiya
    def get_age(self):
        """Oquvchining yoshini qaytaradi"""
        return self.tyil
    def set_sinf(self,yangi_sinf):
        """oquvchining sinfini ozgartiradi"""
        self.sinf = yangi_sinf
    def update_sinf(self):
        """Oquvchining sinfini 1taga kopaytiradi"""
        self.sinf += 1

# oquvchi1 = oquvchi("Alisher","Berdiyev","2011")
# oquvchi2 = oquvchi("Asliddin","Berdiyev","1999")
# oquvchi3 = oquvchi("Fazliddin","Berdiyev","2002")


class Fan():
    """Fan nomli klass"""

    def __init__(self,nomi):
        self.nomi = nomi
        self.oquvchilar_soni = 0
        self.oquvchilar = []

    def add_oquvchi(self,oquvchi):
        """Fanga oquvchilar qoshish"""
        self.oquvchilar.append(oquvchi)
        self.oquvchilar_soni += 1

    def get_oquvchilar(self):
        """Fanga yozilgan oquvchilar haqida ma'lumot"""
        return [oquvchi.get_info() for oquvchi in self.oquvchilar]

def see_methods(klass):
    return [method for method in dir(klass) if method.startswith('__')]

matematika = Fan("Oliy matematika")
oquvchi1 = oquvchi("Alisher","Berdiyev","2011")
oquvchi2 = oquvchi("Asliddin","Berdiyev","1999")
oquvchi3 = oquvchi("Fazliddin","Berdiyev","2002")
matematika.add_oquvchi(oquvchi1)
matematika.add_oquvchi(oquvchi2)
matematika.add_oquvchi(oquvchi3)