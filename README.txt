*$*$* ps aux a CSV *$*$*

# Requisitos previos:
Se debe tener instalado python3 para poder ejecutarlo.
Verificar permisos de ejecución en caso de error al ejecutar (sudo chmod +x ps_aux.py)

# Modo de ejecución:
python3 ps_aux.py

# Funcionamiento:
Al ser ejecutado, el archivo lanzará un "ps aux" y su resultado será redirigido a un archivo llamado "data.raw"
Luego, sobre este "data.raw" se ejecutarán acciones para dejar el resultado del "ps aux" en un archivo llamado
"psaux.csv"
Nota: el delimitador de campos es por "|". Esto es Customizable editando la línea del .py que corresponda al comando sed
de inserción del delimitador de campos.

# CONSEJO: Mejor manera de ingresar a la BBDD para incluir encabezados y formato de columnas amigable:
sqlite3 -header -column psaux.db

# Luego se puede ejecutar un "select * from psaux;" y obtener un buen formato de la tabla completa.
