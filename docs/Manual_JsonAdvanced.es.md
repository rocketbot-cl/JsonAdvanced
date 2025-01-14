



# JsonAdvanced
  
Este módulo te permite trabajar con la API de inteligencia artificial de Google Gemini  

*Read this in other languages: [English](Manual_JsonAdvanced.md), [Português](Manual_JsonAdvanced.pr.md), [Español](Manual_JsonAdvanced.es.md)*
  
![banner](imgs/Banner_JsonAdvanced.png o jpg)
## Como instalar este módulo
  
Para instalar el módulo en Rocketbot Studio, se puede hacer de dos formas:
1. Manual: __Descargar__ el archivo .zip y descomprimirlo en la carpeta modules. El nombre de la carpeta debe ser el mismo al del módulo y dentro debe tener los siguientes archivos y carpetas: \__init__.py, package.json, docs, example y libs. Si tiene abierta la aplicación, refresca el navegador para poder utilizar el nuevo modulo.
2. Automática: Al ingresar a Rocketbot Studio sobre el margen derecho encontrara la sección de **Addons**, seleccionar **Install Mods**, buscar el modulo deseado y presionar install.  


## Descripción de los comandos

### Agregar a Json
  
Agrega un par clave-valor a un Json en un camino específico
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Archivo Json|Selecciona el archivo Json donde se agregará la clave-valor|Selecciona el archivo Json|
|Ruta en archivo Json|Ruta en el archivo Json donde se agregará la clave-valor|ruta en archivo Json|
|Asignar resultado a variable|Variable donde se almacenará el resultado de la conexión|result|
|Clave|Escribe la clave que se agregará al archivo Json|Escribe la clave a agregar|
|Valor|Escribe el valor que se agregará al archivo Json|Escribe el valor a agregar|
|Ruta del nuevo archivo Json|Selecciona la ruta donde se guardará el nuevo archivo Json|Selecciona la ruta del nuevo archivo Json|

### Elimina desde Json
  
Elimina un par clave-valor a un Json en un camino específico
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Archivo Json|Selecciona el archivo Json donde se agregará la clave-valor|Selecciona el archivo Json|
|Ruta en archivo Json|Ruta en el archivo Json donde se agregará la clave-valor|ruta en archivo Json|
|Clave|Escribe la clave que se eliminará del archivo Json|Escribe la clave a eliminar|
|Asignar resultado a variable|Variable donde se almacenará el resultado de la conexión|result|
|Ruta del nuevo archivo Json|Selecciona la ruta donde se guardará el nuevo archivo Json|Selecciona la ruta del nuevo archivo Json|

### Crear Json
  
Crea un archivo Json
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Json|Escribe el Json que se creará|Json a crear|
|Asignar resultado a variable|Variable donde se almacenará el resultado de la conexión|result|
|Ruta del nuevo archivo Json|Selecciona la ruta donde se guardará el nuevo archivo Json|Selecciona la ruta del nuevo archivo Json|
