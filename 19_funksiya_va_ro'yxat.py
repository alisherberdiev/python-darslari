#sana:07.08.2025
def bahola(ismlar):
    baholar = {}
    while ismlar:
        ism =ismlar.pop()
        baho=input(f"Talaba {ism.title()}ning bahosini kiriting:")
        baholar[ism]=int(baho)
    return baholar

talabalar =['ali','zafar','qosim','aziz']
baholar =bahola(talabalar[ : ])
print(baholar)
print(talabalar)