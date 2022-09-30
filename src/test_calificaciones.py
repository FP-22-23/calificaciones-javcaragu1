from calificaciones import *


def test_solicita_datos():
    print("Calculemos la nota de tu cuestionario.")
    a, e, t_r = solicita_datos()
    return a, e, t_r



def test_calcula_nota_cuestionario(a, e, t_r):
    print("Su nota en el cuestionario es: ", calcula_nota_cuestionario(a, e, t_r))

def test_solicita_cuestionarios():
    print("Notas de los cuestionarios.")
    tupla = solicita_notas_cuestionarios()
    return tupla


def test_solicita_examenes():
    print("Notas de los examenes.")
    tupla = solicita_examenes()
    return tupla


def test_solicita_proyectos():
    print("Notas de los proyectos.")
    tupla = solicita_proyectos()
    return tupla


def test_calcula_nota_cuatrimestre(cuestionarios, examen, proyecto):
    print("Su nota del cuatrimestre es: ", calcula_nota_cuatrimestre(cuestionarios, examen, proyecto))


def test_calcula_nota_continua(cuestionarios, examenes, proyectos):
    print("Tu nota en la evaluacion continua es: ", calcula_nota_continua(cuestionarios, examenes, proyectos))

if __name__ == "__main__":
    

    a, e, t_r = test_solicita_datos()
    test_calcula_nota_cuestionario(a, e, t_r)


    c = test_solicita_cuestionarios()
    e = test_solicita_examenes()
    p = test_solicita_proyectos()
    test_calcula_nota_cuatrimestre((c[0], c[1], c[2]), e[0], p[0])
    test_calcula_nota_cuatrimestre((c[3], c[4], c[5]), e[1], p[1])
    test_calcula_nota_continua(c, e, p)


