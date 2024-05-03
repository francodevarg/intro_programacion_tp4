''' Pre: nota number 9 8 6
    Post: lo traduzco a "Bueno", "Excelente", "Regular"
'''
def a_nomenclatura_de_primaria(nota):
    switcher = {
        10: "Excelente",
        9: "Sobresaliente",
        8: "Sobresaliente",
        7: "Aprobado",
        6: "Regular",
        5: "Regular",
        4: "Regular",
        3: "Desaprobado",
        2: "Desaprobado",
        1: "Desaprobado"
    }
    return switcher.get(nota, "Nota inválida")

def obtener_datos_por_consola():
    nombre = input("Ingrese el NOMBRE del estudiante: ")
    materia = input("Ingrese la MATERIA: ")
    nota = int(input("Ingrese la NOTA: "))
    return nombre, materia, nota

def mostrar_mensaje_final_por_consola(nombre,materia,nota_en_formato_primaria):
    print("Alumno " + nombre + 
          " , su nota de " + materia + 
          " es " + nota_en_formato_primaria)

'''
=========================== Programa PRINCIPAL ===============================
'''
nombre, materia, nota_numerica = obtener_datos_por_consola()
nota_en_formato_primaria = a_nomenclatura_de_primaria(nota_numerica);
mostrar_mensaje_final_por_consola(nombre,materia,nota_en_formato_primaria);

     
    
    