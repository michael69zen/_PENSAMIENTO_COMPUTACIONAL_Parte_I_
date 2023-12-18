#_________PENSAMIENTO___COMPUTACIONAL_________
#___Ing._ACEITUNO_ROJO_Miguel_Romilio___
#___Est._JALLO_PAREDES_Cristhian_Michael___
#___Codigo:_236543___
#___Nro:13___
#___Escriba_un_programa_que_permita_determinar_en_que_etapa_de_la_vida_se_encuentra___
#___Respecto_a_su_edad___

print ("INTRODUZCA SU EDAD")
edad = int(input("AÑOS: "))

if edad > 60:
    print("Ud.está en la etapa de la VEJEZ")
elif edad > 25:
    print("Ud.está en la etapa de la ADULTEZ")
elif edad > 20:
    print("Ud.está en la etapa de la JUVENTUD")
elif edad > 12:
    print("Ud.está en la etapa de la ADOLESCENCIA")
elif edad > 6:
    print("Ud.está en la etapa de la NIÑEZ")
elif edad > 0:
    print("Ud.está en la etapa de la INFANCIA")
else:
    print("FASE PRENATAL"),