from calificaciones import *



def test_solicita_datos_cuestionario():
    print("Calculemos tu nota en el cuestionario.")
    a, e, t_r = solicita_datos_cuestionario()
    return a, e, t_r


def test_calcula_notas(a, e, t_r):
    print("Tu nota en el cuestionario es: ", calcula_nota_cuestionario(a, e, t_r))






def test_solicita_notas_cuestionario():
    print("Las notas de los cuestionarios:")
    c1, c2, c3, c4, c5, c6 = solicita_notas_cuestionarios()
    return c1, c2, c3, c4, c5, c6

def test_solicita_notas_proyectos():
    print("Las notas de los proyectos:")
    p1, p2 = solicita_notas_proyectos()
    return p1, p2

def test_solicita_notas_examenes():
    print("Las notas de los examenes:")
    e1, e2 = solicita_notas_examenes()
    return e1, e2


def test_calcula_notas_cuatrimestre(cuestionarios, proyectos, examenes):
    print("Nota del primer cuatrimestre: ", calcula_nota_cuatrimestre((c[0], c[1], c[2]), p[0], e[0]))
    print("Nota del segundo cuatrimestre: ", calcula_nota_cuatrimestre((c[3], c[4], c[5]), p[1], e[1]))


def test_calcula_notas_continua(cuestionarios, proyectos, examenes):
    print("Nota de evaluacion continua: ", calcula_nota_continua(cuestionarios, proyectos, examenes))



if __name__ == "__main__":
    a, e, t_r = test_solicita_datos_cuestionario()
    test_calcula_notas(a, e, t_r)


    c = (c1, c2, c3, c4, c5, c6) = test_solicita_notas_cuestionario()
    p = (p1, p2) = test_solicita_notas_proyectos()
    e = (e1, e2) = test_solicita_notas_examenes()
    test_calcula_notas_cuatrimestre(c, p, e)
    test_calcula_notas_continua(c, p, e)


