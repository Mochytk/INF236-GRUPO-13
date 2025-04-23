# INF236-GRUPO-13

Este es el repositorio del *Grupo 13*, cuyos integrantes son:
* Rodrigo Ariel Cáceres Gaete - 202273616-k
* Martin Ignacio Ferrera Borquez - 202273552-K
* Sergio Roberto Rojas Gutiérrez - 202273619-4
* José Andrés Yáñez Chávez - 202273508-2
* **Tutor**: Javiera Osorio

## Wiki
Puede acceder a la Wiki mediante el siguiente [enlace](https://github.com/Mochytk/INF236-GRUPO-13/wiki)

## Videos (Apartado en Construcción)
* [Video Presentación Cliente]()
* [Video Presentación Avance 1]()
* []()

## Aspectos técnicos relevantes
### Configuración inicial
El primer paso para hacer funcionar la página es clonar el repositorio. Para ello, se puede hacer uso de GitHub Desktop o del siguiente comando:

`git clone https://github.com/Mochytk/INF236-GRUPO-13.git`

Además, se deben instalar las siguientes aplicaciones:
- Python 3.12 o posterior
- Node.js 22 o posterior
- npm 10.9.2 o posterior

Una vez cumplidos estos requisitos, se deberán ejecutar los siguientes comandos para instalar las librerías de Python necesarias:

- `python -m pip install Django==5.2`
- `pip install djangorestframework`
- `pip install django-cors-headers`
- `pip install djangorestframework-simplejwt`

### Desplegar el proyecto
Una vez finalizada la configuración inicial, debemos hacer funcionar la página. Para ello, lo primero será inicializar el backend (Django), para lo cual abrimos la terminal desde la carpeta "paes" y ejecutamos el siguiente comando:

`python manage.py runserver`

Luego, debemos iniciar el frontend (Vue), para lo cual abrimos una terminal en la carpeta "vue" y ejecutamos los siguientes comandos:

`npm install`

`npm run dev`

El proyecto está basado en la documentación disponible en:
*apartado en construcción*
