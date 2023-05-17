# Trabajo Telematica Siata
## _Proyecto Final_

[![UpbLogo.png](https://i.postimg.cc/Hxyrb8kB/UpbLogo.png)](https://postimg.cc/wy9xpvJm)

## Objetivos del trabajo

- Emplear las nuevas tecnologías para desarrollar un proyecto comerciable usando los conocimientos del curso 💻
- Evaluar la capacidad de usar nuevas tecnologias para resolver problemas y ofrecer servicios ⌨🖱
- Demostrar la capacidad de implementar servicios telemáticos en aplicaciones reales👔

## Características del servicio

- Debe ser un servicio escalable que debe brindar un servicio consumible

> Debe tener los siguientes requerimientos
- El servidor que presta la principal aplicación es un servidor web desplegado bajo el concepto de desarrollo continuo
- El desarrollo está almacenado en un repositorio (Este), el nivel de experiencia de usuario y desarrollo gráfico no importa si es simple o elaborado
- El desarrollo debe estar documentado y tener un archivo de instruccion README.MD que explique como desplegar el servicio en el contenedor para un servidor de producción
- El estudiante debe entregar el enlace al repositorio y el mismo debe tener un script o una serie de archivos, que tenga automatizado todo el proceso de construccion de la imagen con el servicio desplegado
- El servicio puede ser escrito en cualquier lenguaje, html o php o python o el lenguaje que usted considere que puede manejar mejor, recuerde que la idea principal del proyecto es usar un despliegue usando contenedores

# Comienzo Al Trabajo
## Automatización en la creación de Dockers

## Elaboracion de la página web
Más que todo en este apartado se buscar mostrar y explicar la importancia de algunos factores del codigo compartido
> Podrás encontrar la elaboración de esta pagina en los archivos adjuntos de este trabajo llamado "pagina.py".

#### ~ Login ~
> En la elaboracion del sistema de Login, no se ha usado ninguna herramienta de base de datos como puede ser perfectamente SQL, solo se ha hecho desde el codigo, la implementación de un usuario y una contraseña, ya que he pensado que puede ser mas optimo para este trabajo.

En la linea n°59 hasta la linea n°62 se encuentra en donde estamos validando revisando si es verdadero o flaso, la informacion que la persona ingresa, lo que tenemos en la ultima linea es lo mismo que tener 

```sh
if username == valid_username and password == valid_password:
        return True
    else:
        return False
```

###### Usuario y contraseña del codigo (Si lo quieres poner a prueba)

`Usuario: admin`

`Contraseña: password`
