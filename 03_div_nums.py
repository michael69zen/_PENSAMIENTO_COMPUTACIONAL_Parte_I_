#_________PENSAMIENTO___COMPUTACIONAL_________
#___Ing._ACEITUNO_ROJO_Miguel_Romilio___
#___Est._JALLO_PAREDES_Cristhian_Michael___
#___Codigo:_236543___
#___Nro:03___
#___Escriba_un_codigo_para_resolver_la_division_de_dos_numeros___

numero_1 = input("DIVIDENDO: ")
numero_2 = input("DIVISOR: ")

if int(numero_2) == 0:
    print("INDETERMINADO / PERTENECE A LOS NUMEROS COMPLEJOS i ")
else:
    resultado = int(numero_1) / int(numero_2)
    print(f"RESULTADO: {resultado}")