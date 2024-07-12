# -*- coding: utf-8 -*-
import pyautogui
import time


def quitar_tildes(texto):
    """Reemplaza vocales acentuadas por vocales sin acento."""
    reemplazos = {'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u',
                  'Á': 'A', 'É': 'E', 'Í': 'I', 'Ó': 'O', 'Ú': 'U'}
    for vocal_acentuada, vocal_sin_acento in reemplazos.items():
        texto = texto.replace(vocal_acentuada, vocal_sin_acento)
    return texto


time.sleep(5)  # Pausa de 5 segundos

with open("text.txt", 'r', encoding='utf-8') as f:  # Abrir archivo con codificación UTF-8
    for word in f:
        palabra_sin_acentos = quitar_tildes(word)  # Eliminar tildes de cada palabra
        pyautogui.typewrite(palabra_sin_acentos)  # Escribir palabra sin tildes
        pyautogui.press("enter")  # Presionar Enter
