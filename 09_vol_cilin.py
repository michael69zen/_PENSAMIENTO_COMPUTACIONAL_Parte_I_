#_________PENSAMIENTO___COMPUTACIONAL_________
#___Ing._ACEITUNO_ROJO_Miguel_Romilio___
#___Est._JALLO_PAREDES_Cristhian_Michael___
#___Codigo:_236543___
#___Nro:09___
#___Escriba_un_programa_que_permita_hallar_volumen_del_cilindro___

radio = int(input("RADIO DEL CILINDRO = "))
altura = int(input("ALTURA DEL CILINDRO = "))
pi = 3.1416

vol_cilindro = pi*altura*(radio**2)

print(f"VOLUMEN DEL CILINDRO = {vol_cilindro} mts3")