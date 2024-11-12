
# Identificador de Mutantes

Este proyecto identifica si un humano es mutante o no basándose en su secuencia de ADN. Se buscan secuencias de cuatro letras idénticas consecutivas en direcciones horizontal, vertical o diagonal dentro de una matriz de ADN.

## Requisitos

Este proyecto está desarrollado en **Python 3.12**. Asegúrate de tener instalada una versión compatible de Python en tu máquina.

## Clonar el repositorio

1. Abre tu terminal o línea de comandos.
2. Ejecuta el siguiente comando para clonar el repositorio:

   ```bash
   https://github.com/hanz-saenz/mutantes.git
   ```

3. Cambia al directorio del repositorio clonado:

   ```bash
   cd mutantes
   ```

## Ejecutar el archivo `identificar_mutantes.py`

Para ejecutar el archivo principal que contiene la lógica para identificar mutantes, sigue estos pasos:

1. Asegúrate de estar en el directorio del proyecto.
2. Ejecuta el script con el siguiente comando:

   ```bash
   python identificar_mutantes.py
   ```

### Ejemplo de entrada

El archivo `identificar_mutantes.py` espera un array de secuencias de ADN como entrada. Un ejemplo de cómo utilizarlo en código puede verse dentro del archivo, con matrices de ADN de mutantes y no mutantes.

### Salida esperada

- Si el ADN corresponde a un mutante, el programa devolverá `True`.
- Si el ADN corresponde a un humano no mutante, el programa devolverá `False`.

