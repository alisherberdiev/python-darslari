#sana:11.07.2011
#dars:14
#mavzu:nesting

human0={
    "name":"Alisher",
    "surname":"Berdiyev",
    "old":"14",
    "height":"170",
    "weight":"70"
    }

human1={
    "name":"Asliddin",
    "surname":"Berdiyev",
    "old":"26",
    "height":"175",
    "weight":"85"
    }

human2={
    "name":"Umar",
    "surname":"Eshqobilov",
    "old":"78",
    "height":"160",
    "weight":"75"
    }

humans=[human0,human1,human2]
for human in humans:
    print(f"ismi:{human['name'].title()}, "
          f"familyasi:{human['surname'].title()},"
          f"yoshi-{human['old']}, "
          f"bo'yi-{human['height']}sm, "
          f"vazni-{human['weight']}kg")


#--------------------------------------------------------------------------------------------------
print(human0["name"])



#-----------------------------------------------------------------------------------------------------
malibus=[]
for n in range(10):
    new_car={
        "model":"BMW",
        "rang":None,
        "yili":None,
        "narh":None,
        "turi":None
    }
    malibus.append(new_car)

for malibu in malibus[:2]:
    malibu['rang']="yashil"
    malibu['yili']="2022"
    malibu['narh']="225k$"
    malibu['turi']="M3"

for malibu in malibus[2:5]:
    malibu['rang']="sariq"
    malibu['yili']="2025"
    malibu['narh']="220k$"
    malibu['turi']="M4 Competition"

for malibu in malibus[5:]:
    malibu['rang']="qora"
    malibu['yili']="2024"
    malibu['narh']="250k$"
    malibu['turi']="M5 CS"

#for malibu in malibus:
#print(malibu)

for malibu in malibus:
    if malibu['yili']==2025:
        malibu['narh']="280k$"
    else:
        malibu['narh']="230k$"
for malibu in malibus:
    print(malibu)
#-----------------------------------------------------------------------------------------------------------
dasturchilar={
    "Alisher":["python","css"],
    "Asliddin":["python","go","JS"],
    }
for ism,tillar in dasturchilar.items():
    print(f"\n{ism.title()} quyidagi dasturlash tillarini biladi: ")
    for til in tillar:
        print(til.upper())


for ism,tillar in dasturchilar.items():
    print(f"\n{ism.title()} quyidagi dasturlash tillarini biladi: ")
    for til in tillar:
        print(f"{til.upper()} ", end="")

#-----------------------------------------------------------------------------------------------------------




