import csv
import random
import re
from transformers import pipeline

# Función para generar oraciones sobre un tema específico
def generar_oraciones_sobre_tema(tema, num_oraciones):
    generador = pipeline('text-generation', model='datificate/gpt2-small-spanish')
    oraciones = []
    for _ in range(num_oraciones):
        oracion = generador(f"{tema}: ", max_length=50, num_return_sequences=1)[0]['generated_text']
        oraciones.append(oracion)
    return oraciones

# Función para combinar oraciones en un párrafo
def combinar_oraciones_en_parrafo(oraciones):
    return " ".join(oraciones)

# Función para agregar caracteres especiales y números a una oración
def agregar_caracteres_especiales_y_numeros(oracion):
    caracteres_especiales = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '[', ']', '{', '}', '|', ';', ':', '"', "'", '<', '>', ',', '.', '?', '/']
    palabras = oracion.split()
    for i in range(len(palabras)):
        if random.choice([True, False]):
            palabras[i] += random.choice(caracteres_especiales)
        if random.choice([True, False]):
            palabras[i] += str(random.randint(0, 9))
    return " ".join(palabras)

# Función para limpiar caracteres especiales y números de una oración
def limpiar_caracteres_especiales_y_numeros(oracion):
    return re.sub(r'[^A-Za-z\s]', '', oracion)

# Función para guardar oraciones y párrafos en un archivo CSV
def guardar_en_csv(oraciones_con_caracteres, oraciones_limpias, parrafo, filename="oraciones.csv"):
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Oración con Caracteres", "Oración Limpia"])
        for con_caracteres, limpia in zip(oraciones_con_caracteres, oraciones_limpias):
            writer.writerow([con_caracteres, limpia])
        writer.writerow([])
        writer.writerow(["Párrafo"])
        writer.writerow([parrafo])
    print(f"Se han generado {len(oraciones_con_caracteres)} oraciones y se ha guardado el párrafo en '{filename}'.")

# Función principal para generar y guardar oraciones y párrafos
def main():
    tema = "programación"
    num_oraciones = 5
    oraciones = generar_oraciones_sobre_tema(tema, num_oraciones)
    oraciones_con_caracteres = [agregar_caracteres_especiales_y_numeros(oracion) for oracion in oraciones]
    oraciones_limpias = [limpiar_caracteres_especiales_y_numeros(oracion) for oracion in oraciones_con_caracteres]
    parrafo = combinar_oraciones_en_parrafo(oraciones)
    guardar_en_csv(oraciones_con_caracteres, oraciones_limpias, parrafo)

if __name__ == "__main__":
    main()
