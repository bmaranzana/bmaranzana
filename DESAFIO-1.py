import random

def generar_matriz(num_estudiantes, num_materias):

    return [[random.randint(1, 10) for _ in range(num_materias)] for _ in range(num_estudiantes)]

def mostrar_matriz(matriz, estudiantes, materias):
    
    encabezado = ' ' * 12 + ' '.join([f'Materia {i+1}' for i in range(materias)])
    print(encabezado)
    print('-' * len(encabezado))
    for i, fila in enumerate(matriz):
        print(f'Estudiante {i+1:2d}: ' + ' '.join(map(str, fila)))

def calcular_promedio_estudiantes(matriz):
    
    promedios = [sum(fila) / len(fila) for fila in matriz]
    for i, promedio in enumerate(promedios):
        print(f"Promedio del estudiante {i + 1}: {promedio:.2f}")

def calcular_promedio_materias(matriz):

    num_materias = len(matriz[0]) if matriz else 0
    promedios = []
    for j in range(num_materias):
        suma = sum(fila[j] for fila in matriz)
        promedio = suma / len(matriz)
        promedios.append(promedio)
    
    for i, promedio in enumerate(promedios):
        print(f"Promedio de la materia {i + 1}: {promedio:.2f}")

def main():
    num_estudiantes = 5
    num_materias = 4
    
    matriz = generar_matriz(num_estudiantes, num_materias)

    print("Matriz de calificaciones:")
    mostrar_matriz(matriz, num_estudiantes, num_materias)
    
    print("\nPromedios de los estudiantes:")
    calcular_promedio_estudiantes(matriz)
    
    print("\nPromedios de las materias:")
    calcular_promedio_materias(matriz)

if __name__ == "__main__":
    main()
