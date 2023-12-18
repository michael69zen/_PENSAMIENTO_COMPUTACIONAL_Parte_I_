#_________PENSAMIENTO___COMPUTACIONAL_________
#___Ing._ACEITUNO_ROJO_Miguel_Romilio___
#___Est._JALLO_PAREDES_Cristhian_Michael___
#___Codigo:_236543___
#___Nro:05___
#___Escriba_un_codigo_para_determinar_el_promedio_de_edad_de_5_estudiantes___

comp_1 = input("EDAD DEL ESTUDIANTE NRO_1: ")
comp_2 = input("EDAD DEL ESTUDIANTE NRO_2: ")
comp_3 = input("EDAD DEL ESTUDIANTE NRO_3: ")
comp_4 = input("EDAD DEL ESTUDIANTE NRO_4: ")
comp_5 = input("EDAD DEL ESTUDIANTE NRO_5: ")

suma = int(comp_1)+int(comp_2)+int(comp_3)+int(comp_4)+int(comp_5)
promedio = suma / 5

print(f"PROMEDIO DE EDAD DE LOS ESTUDIANTES: {promedio}")