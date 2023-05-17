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
## Creación de Dockers
> Los siguientes comandos seran para los sitemas operativos de Linux

En primer instancia tendremos que abrir una Terminal en Linux

Luego revisaremos que tengamos el programa de Docker en nuestro sistema operativo, en caso que no lo tengamos, aqui les dejo la instalacion de Docker Engine desde la pagina de documentacion de [Docker](https://docs.docker.com/engine/install/ubuntu/)

Luego realizamos teniendo Docker, los siguientes comandos:
```sh
sudo apt update
sudo docker pull ubuntu
sudo docker run -it -p 8080:80 ubuntu
```
Luego de esto, ya tendriamos que estar en la Terminal del contenedor que creamos.
> Una vez que estemos dentro del contenedor estaremos en todo momento en el modo SuperUsuario

El objetivo ya sera la automatización de descarga de las librerias necesarias y iniciar nuestra pagina web, para eso primero vamos a tener que descargar un editor de texto de Terminal, ya que nuestro contenedor vendrá sin esta, lo descargamos poniendo
```sh
apt install nano
```

## Automatización en la creación de Dockers

## Elaboracion de la página web
Más que todo en este apartado se buscar mostrar y explicar la importancia de algunos factores del codigo compartido
> Podrás encontrar la elaboración de esta pagina en los archivos adjuntos de este trabajo llamado "pagina.py".
> Tambien se puede elaborar la pagina con herramientas como lo es HTML y CSS pero en el apartado de la graficacion con estos datos resulta bastante tedioso

La pagina funciona de la siguiente forma, siempre cuando se quiera tener acceso a la pagina, tendra que verificar que tenga nombre y usuario, ingresando sus datos en los apartados correspondientes.

Cuando el sistema verifique estos datos le dara acceso a la informacion de SIATA, para la graficación de este componente podriamos haber utilizado otro codigo pero se me ha perdido el codigo y no recuerdo perfectamente como es la incorporacion de este, pero el otra forma de implementar la graficacion de los datos del archivo json es con platly.ghaph_objets de la siguiente forma:
```sh
url = "Ingresar el Url de SIATA"

data = pd.read_json(url.convert_dates='True')
latr = []
lonr = []
zr = []

for i in range(0,100):
	zr.append(data['datos'][i]['pocentajeNivel'])
	latr.append(data['datos'][i]['coordenadas'][0]['latitud'])
	lonr.append(data['datos'][i]['coordenadas'][0]['longitud'])

fig = go.Figure(go.Densitymapbox(lat=latr,lon=lonr,z=zr,radius=20,opacity=0.9, zmin=0, zmax=100))
fig.update_layout(mapbox_style="stamen-terrain",mapbox_center_lon=-75.589,mapbox_center_lat=6.2429)
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
```

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
