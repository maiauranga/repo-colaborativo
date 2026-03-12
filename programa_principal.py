#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 15:30:09 2026

@author: maia
"""

import funciones_habitos

lista = funciones_habitos.registrar_habitos()

resultado = funciones_habitos.analizar_habitos(lista)

print("Resumen de actividades:")
print(resultado)
