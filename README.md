# Backend-Bautista

Este es un proyecto de backend hecho para un colegio.

El backend se estara desarollando con python y el framework de fastapi 
https://fastapi.tiangolo.com/

El gestor de base datos sera postgresql
https://www.postgresql.org/

Una ves tengan instalado esas herramientas puedes importar la base datos con el archivo DB_Bautista
Video de ejemplo de como importar la DB a postgresql link -> https://www.youtube.com/watch?v=icEvkyIXqug 

En el archivo requirements.txt se puede ver todas las dependencias usadas en este proyecto para poder importarlas ejecute el siguiente comando
pip install -r requirements.txt

Para poder levantar el backend deben de ejecutar el siguiente comando en la termina ubicados ya en el proyecto
uvicorn app.main:app --reload

