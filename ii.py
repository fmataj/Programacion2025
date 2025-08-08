# --- DESAFÍO 1: Reporte de Enfermedades Tratadas ---
import json
from collections import Counter
import matplotlib.pyplot as plt

# 1. Cargar datos del archivo JSON
with open("clinica_intermedio.json", "r", encoding="utf-8") as f:
    datos = json.load(f)

# 2. Extraer las enfermedades de cada paciente
lista_enfermedades = [paciente[4] for paciente in datos]  # índice 4 es la enfermedad

# 3. Contar cuántas veces aparece cada enfermedad
conteo_enfermedades = Counter(lista_enfermedades)

# 4. Mostrar en tabla
print("📋 REPORTE DE ENFERMEDADES TRATADAS EN LA CLÍNICA\n")
print(f"{'Enfermedad':<20}{'Pacientes':<10}")
print("-" * 30)
for enfermedad, cantidad in conteo_enfermedades.items():
    print(f"{enfermedad:<20}{cantidad:<10}")

# 5. Visualizar con gráfico
plt.figure(figsize=(10,6))
plt.bar(conteo_enfermedades.keys(), conteo_enfermedades.values(), color='skyblue', edgecolor='black')
plt.title("Cantidad de Pacientes por Enfermedad", fontsize=16)
plt.xlabel("Enfermedad", fontsize=12)
plt.ylabel("Número de Pacientes", fontsize=12)
plt.xticks(rotation=45, ha="right")
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()
