#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 15:29:37 2026

@author: maia
"""

def registrar_habitos (): 
    '''
    

    Returns
    -------
    habitos : lista
        lista que contiene las actividades realizadas por los usuarios

    '''
 
    habitos = []

    while True:
        actividad = input("Ingresa una actividad: ")
        habitos.append(actividad)

        seguir = input("¿Querés agregar otro hábito? (si/no): ")

        if seguir == "no":
            break

    return habitos


def  analizar_habitos (habitos):
    '''
    

    Parameters
    ----------
    habitos : lista
     lista que contiene las actividades realizadas por los usuarios

    Returns
    -------
    conteo : diccionario
        Ddiccionario que muestra cuantas veces aparece cada actividad 

    '''
    conteo = {}
    
    for actividad in habitos:
        if actividad in conteo:
            conteo[actividad] += 1
        else:
            conteo[actividad] = 1

    return conteo
    