import os
import json
import sqlite3

os.system("ps aux > data.raw")
# Primero dejamos patrón solo un espacio en blanco, excepto la parte de "Command":
os.system("sed 's/ \+/ /g' data.raw > psaux.csv")
# Acomodo de campos para que el último quede aparte con sus espacios ("Command"):
os.system("sed -i 's/ /|/10' psaux.csv")
os.system("sed -i 's/ /|/9' psaux.csv")
os.system("sed -i 's/ /|/8' psaux.csv")
os.system("sed -i 's/ /|/7' psaux.csv")
os.system("sed -i 's/ /|/6' psaux.csv")
os.system("sed -i 's/ /|/5' psaux.csv")
os.system("sed -i 's/ /|/4' psaux.csv")
os.system("sed -i 's/ /|/3' psaux.csv")
os.system("sed -i 's/ /|/2' psaux.csv")
os.system("sed -i 's/ /|/1' psaux.csv")

# Montando la DB e importando el csv a una tabla a crear:
os.system("sqlite3 psaux.db -cmd '.import psaux.csv psaux' '.exit'")

# Se intentó con un ciclo for pero daba errores relacionados a las comillas y al llamado de la variable iteradora.
