
def calcula_nota_cuestionario(aciertos, errores, total_respuestas):
    nota = ((aciertos * 10) / total_respuestas) - ((errores * 10) / (50 - total_respuestas))
    return nota

def solicita_datos():
    a = int(input("Introduzca el numero de aciertos: "))
    e = int(input("Introduzca el numero de errores: "))
    t_r = int(input("Introduzca el total de respuestas: "))
    return a, e, t_r




def calcula_nota_cuatrimestre(cuestionarios, examen, proyecto):
    if proyecto < 5:
        nota = 3
    
    else:
        nota = 0.1 * sum(cuestionarios) + 0.6 * examen + 0.1 * proyecto
    

    return nota



def calcula_nota_continua(cuestionarios, examenes, proyectos):
    if calcula_nota_cuatrimestre((cuestionarios[0], cuestionarios[1], cuestionarios[2]), examenes[0], proyectos[0]) < 4 or calcula_nota_cuatrimestre((cuestionarios[3], cuestionarios[4], cuestionarios[5]), examenes[1], proyectos[1]) < 4:
        nota = 4

    else:
        nota = (calcula_nota_cuatrimestre((cuestionarios[0], cuestionarios[1], cuestionarios[2]), examenes[0], proyectos[0]) + calcula_nota_cuatrimestre((cuestionarios[3], cuestionarios[4], cuestionarios[5]), examenes[1], proyectos[1])) / 2
    

    return nota




def solicita_notas_cuestionarios():
    c1 = float(input("Introduzca la nota del cuestionario 1: "))
    c2 = float(input("Introduzca la nota del cuestionario 2: "))
    c3 = float(input("Introduzca la nota del cuestionario 3: "))
    c4 = float(input("Introduzca la nota del cuestionario 4: "))
    c5 = float(input("Introduzca la nota del cuestionario 5: "))
    c6 = float(input("Introduzca la nota del cuestionario 6: "))

    return (c1, c2, c3, c4, c5, c6)


def solicita_examenes():
    e1 = float(input("Introduzca la nota del primer examen: "))
    e2 = float(input("Introduzca la nota del segundo examen: "))

    return (e1, e2)


def solicita_proyectos():
    p1 = float(input("Introduzca la nota del primer proyecto: "))
    p2 = float(input("Introduzca la nota del segundo proyecto: "))

    return (p1, p2)



