#Imagina que tienes una lista de alumnos y sus calificaciones en un curso. Cada alumno está representado por una tupla con su nombre y su calificación.
#
#
#El objetivo del desafío es escribir una función que calcule la calificación promedio del curso y devuelva una tupla con el nombre del alumno con la 
#calificación más alta y el nombre del alumno con la calificación más baja.

def calificaciones(alumnos):
    # Calcular la calificación promedio
    suma = 0
    for alumno in alumnos:
        suma += alumno[1]
    promedio = suma / len(alumnos)
    
    # Encontrar al alumno con la calificación más alta y más baja
    mejor_alumno = alumnos[0]
    peor_alumno = alumnos[0]
    for alumno in alumnos:
        if alumno[1] > mejor_alumno[1]:
            mejor_alumno = alumno
        if alumno[1] < peor_alumno[1]:
            peor_alumno = alumno
    
    # Devolver la tupla con el resultado
    return (promedio, mejor_alumno[0], peor_alumno[0])

# Prueba de la función
alumnos = [("Juan", 80), ("Ana", 90), ("Pedro", 70), ("Laura", 85)]
resultado = calificaciones(alumnos)
print(resultado)  # Imprime (81.25, "Ana", "Pedro")
