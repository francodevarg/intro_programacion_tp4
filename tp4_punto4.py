# Pre: nota number 9 8 6
# Post: lo traduzco a "Bueno", "Excelente", "Regular"
def a_nomenclatura_de_primaria(nota):
    if nota == 10:
        nota = "Excelente"
    elif nota == 8 or nota == 9:
        nota = "Sobresaliente"
    elif nota == 7:
        nota = "Aprobado"
    elif nota >= 4 and nota <= 6:
        nota = "Regular"
    elif nota >= 1 and nota <= 3:
        nota = "Desaprobado"
    else:
        nota = "Nota inválida"
    return nota

def obtener_datos():
    nombre = input("Ingrese el nombre del estudiante: ")
    materia = input("Ingrese el nombre de la materia: ")
    nota = int(input("Ingrese la nota del estudiante en la materia: "))
    return nombre, materia, nota

def mostrar_mensaje_final(nombre,materia,nota_en_formato_primaria):
    print("Alumno " + nombre + " , su nota de " + materia + " es " + nota_en_formato_primaria)



def es_mayor_de_edad(edad):
    if(edad >=18):
        return True
    else:
        return False   
    


nombre, materia, nota_numerica = obtener_datos()


nota_en_formato_primaria = a_nomenclatura_de_primaria(nota_numerica);
mostrar_mensaje_final(nombre,materia,nota_en_formato_primaria);

     
    
    