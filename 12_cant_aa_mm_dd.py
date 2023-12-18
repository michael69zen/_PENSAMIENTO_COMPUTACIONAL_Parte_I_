#_________PENSAMIENTO___COMPUTACIONAL_________
#___Ing._ACEITUNO_ROJO_Miguel_Romilio___
#___Est._JALLO_PAREDES_Cristhian_Michael___
#___Codigo:_236543___
#___Nro:12___
#___Escriba_un_programa_que_permita_determinar_la_cantidad_de_anios_meses_dias___
#___Respecto_a_su_fecha_de_nacimiento___

print("INTRODUZCA LA FECHA ACTUAL")
a = int(input("AÑO: "))
m = int(input("MES: "))
d = int(input("DIA: "))

print("FECHA DE NACIMIENTO")
a1 = int(input("AÑO: "))
m1 = int(input("MES: "))
d1 = int(input("DIA: "))

anios = a - a1
meses = m - m1
dias = d - d1

if meses < 0:
    anios = anios - 1
    meses = 12 + meses
else:
    meses

if dias < 0:
    meses = meses - 1
    dias = 30 + dias
    
else:
    dias
    
print(f"USTED TIENE {anios} AÑOS, {meses} MESES Y {dias} DIAS")
