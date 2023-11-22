Desarrollo de la herramienta para Juego de Roles. El proyecto ha sido desarrollado mediante el framework Django. 



1. Clonar el repositorio 
2. cd taller (En este se encuentra la imagen tree.png donde se encuentra el arbol del proyecto).
3. Se recomienda el uso de un ambiente virtual. En este, realizar la instalación de los paquetes encontrados en requeriments.txt.
4. Para correr la herramienta en localhost, usar el comando python manage.py runserver (por default se corre en el puerto 8000). 


La herramienta cuenta con 7 apps:


1. taller: contiene las configuraciones basicas para poder correr la herramienta. Settings.py determina las caracteristicas basicas como la zona horaria y el uso de base de datos (en este caso se utiliza sqlite pero a Django se pueden integrar facilmente las bases de datos PostreSQL,MariaDB,MySQL y Oracle).
2. homepage: aplicación para la pagina de inicio. 
3. consultas: aplicación que simula una busqueda en una base de datos de la cual se obtiene información financiera de una persona.Se puede modificar o agregar información de las posibles personas a buscar mediante el admin de Django.
4. polls: aplicación para el desarrollo de un cuestionario. Este cuenta con 3 tipos de preguntas posibles: unica, multiple y abierta y se debe enviar el quiz junto al nombre del que lo realiza. Estas preguntas pueden ser modificas y creadas mediante el admin de Django.
5. results: aplicación para el procesamiento y visualización de los resultados de los cuestionario.s
6. ros: aplicación para la visualización de los ROS que se muestran mediante un visualizador de PDF.
7. solicitud: aplicación para la simulación de un requerimiento de mayor información.#   j r u b u n t u  
 