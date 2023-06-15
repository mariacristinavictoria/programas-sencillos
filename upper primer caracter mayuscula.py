# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 19:31:38 2023

@author: Alumno
"""

cadena1 = input(" introduce una cadena de caracteres: ")
ultimo_caracter = cadena1[-1].upper()
cadena_modificada = cadena1[:-1] + ultimo_caracter
print("la cadena con el último carácter en mayúscula:", cadena_modificada)