from sys import flags


class Popularidad:
    def __init__(self, mes, estrellas, cant_proy):
        self.mes = mes
        self.estrellas = estrellas
        self.cant_proy = cant_proy

    def __str__(self):
        return "{:^6} | {:>10.2f}k | {:>10}".format(self.mes, self.estrellas, self.cant_proy)


def cabera_popularidad():
    return "{:^6} | {:>11} | {:>10}".format("Mes", "Estrellas", "Proyectos") + "\n" + "-" * 34

class Proyecto:
    def __init__(self, nombre_usuario, repositorio, fecha_actualizacion, lenguaje, likes, tags, url):
        self.nombre_usuario = nombre_usuario
        self.repositorio = repositorio
        self.fecha_actualizacion = fecha_actualizacion
        self.lenguaje = lenguaje
        self.likes = likes
        self.tags = tags
        self.url = url

    def formato_archivo(self):
        return f"{self.nombre_usuario}|{self.repositorio}|{self.fecha_actualizacion}|{self.lenguaje}|{self.likes}|{self.tags}|{self.url}"

    def __str__(self):
      return "{:<16} | {:<20} | {:<20} | {:<11} | {:<10.2f}k | {:<15} | {:<20}".format(self.nombre_usuario, self.repositorio, self.fecha_actualizacion, self.lenguaje, self.likes, self.tags, self.url)


def cabezera_proyectos():
    return "{:^16} | {:^20} | {:^20} | {:^11} | {:^10} | {:^15} | {:^20}".format("Nombre usuario", "Repositorio", "Fecha actualizacion", "Lenguaje", "Likes", "Tags", "URL") + "\n" + "-" * 140


def convertir_a_proyecto(cadena):
    campos = cadena.split("|")
    return Proyecto(
        campos[0],
        campos[1],
        campos[3],
        campos[4],
        float(campos[5].replace("k", "")),
        campos[6],
        campos[7]
    )


def asignar_posicion_proyecto(proyecto, vec_proyectos):
    """
    campos: [1]= nombre_usuario
            [2]= repositorio
            [3]= fecha_actualizacion
            [4]= lenguaje
            [5]= likes
            [6]= tags
            [7]= url
    """
    long_proyect = len(vec_proyectos)
    if long_proyect != 0:
        for i in range(long_proyect):
            if proyecto.repositorio == vec_proyectos[i].repositorio:
                for j in range(len(proyecto.repositorio)):

                    if proyecto.repositorio[j] < (vec_proyectos[i].repositorio)[j]:
                        vec_proyectos.insert(i, proyecto)
                        break

                    else:
                        pass

            elif proyecto.repositorio < vec_proyectos[i].repositorio:
                # el registro se añade en la poscicion asignada segun orden de repositorio
                vec_proyectos.insert(i, proyecto)
                break

            elif proyecto.repositorio > vec_proyectos[i].repositorio:
                pass

    elif long_proyect == 0:
        vec_proyectos.append(proyecto)


def comprobar_linea(linea, vec_proyectos):
    procesar = False
    campos = linea.split("|")
    
    # lenguaje en blanco
    if campos[4] == "":
        return procesar

    else:
        # repositorio repetido
        long_proyect = len(vec_proyectos)

        for i in range(long_proyect):
            if campos[2] == vec_proyectos[i].repositorio:
                return procesar

        # success
        return True


def discriminar_lenguajes(vec_proyectos):
    # [  [lenguaje, cantidad]  ]
    lenguajes_cantidad = []

    for i in range(len(vec_proyectos)):
        linea = vec_proyectos[i].lenguaje
        exist = False

        for j in range(len(lenguajes_cantidad)):
            # si se encuentra en la lista lo suma
            if linea == lenguajes_cantidad[j][0]:
                exist = True
                lenguajes_cantidad[j][1] += 1

        # si no lo encuentra lo añade
        if exist == False:
            box = [linea, 1]
            lenguajes_cantidad.append(box)

    return lenguajes_cantidad


def find_tag(tag, vec_proyectos):
    from funciones import mostrar_por_tags
    flag_primera = True
    flag_mostrar = False
    for i in range(len(vec_proyectos)):
        if tag  in vec_proyectos[i].tags:
            # determinar si desea guardar los resultados
            if flag_primera:
                from funciones import validar_entre
                print("\nDesea almacenar los resultados en un archivo de texto?[ 0 = No ; 1 = Si ]")
                opcion = validar_entre(0, 1)
                if opcion == 1:
                    saving = True
                else:
                    saving = False
                

            # determinar resultados

            if int(vec_proyectos[i].likes) <= 10000: # estrellas
                estrellas = 1
            elif 10001 <= int(vec_proyectos[i].likes) <= 20000:
                estrellas = 2
            elif 20001 <= int(vec_proyectos[i].likes) <= 30000:
                estrellas = 3
            elif 30001 <= int(vec_proyectos[i].likes) <= 40000:
                estrellas = 4
            else:
                estrellas = 5

            # imprimir resultados
            
            flag_mostrar = mostrar_por_tags(vec_proyectos[i], estrellas, saving, flag_primera)
            flag_primera = False

    return flag_mostrar


if __name__ == "__main__":
    popularidad = Popularidad(1, 100, 10)
    print(cabera_popularidad())
    print(popularidad)

    proyecto = Proyecto("usuario", "repositorio", "fecha", "lenguaje", 100, "tags", "url")
    print(cabezera_proyectos())
    print(proyecto)
