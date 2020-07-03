# Trabajo Fin de Grado

En este repositorio puede consultarse el código desarrollado para el Trabajo Fin de Grado.

## Estructura

### gt

Este directorio contiene las ground truth de cada vídeo del conjunto de test para realizar el cálculo de las distintas métricas.

### tracking_wo_bnw

En este directorio encontramos la implementación del algoritmo de tracking [_Tracking without bells and whistles_](https://github.com/phil-bergmann/tracking_wo_bnw) con las modificaciones necesarias para usar nuestro dataset propio.

### anomaly_detections.py

Este archivo contiene las funciones que se encargan de detectar las trayectorias anormales y dibujar los cuadros delimitadores correspondientes en los vídeos del dataset.

### create_test_folder.py

Este script construye el directorio con los datos de las trayectorias anómalas detectadas por el algoritmo para compararlos con las ground truth.

### create_tracking_results.py

Este script construye el directorio con las trayectorias obtenidas por el algoritmo de tracking.

### metrics.py

Este script se encarga de computar las métricas tomando como entradas el directorio _gt_ y el directorio creado por _create_test_folder.py_.

### run.py

Script de ejecución.

### test.py

Este archivo contiene funciones que únicamente se ejecutan con los vídeos de test.

### train.py

Este archivo contiene funciones que se ejecutan durante el entrenamiento, para realizar el descubrimiento de zonas.

### utils.py

Este archivo contiene diversas funciones auxiliares, así como variables y constantes globales.

### zones.py

Este archivo contiene funciones que se encargan de actualizar la información sobre las zonas descubiertas durante el entrenamiento.

## Instrucciones para la reproducción de resultados

Para generar los mismos resultados mostrados en el trabajo, los pasos a seguir son los siguientes:

1.  Descargar el contenido del repositorio y descomprimirlo.
2.  Descargar el [conjunto de datos](https://drive.google.com/file/d/1l1XBHSr_XLlmGJRs_UrvZ0ExcGDDjzKI/view?usp=sharing) y descomprimirlo en la carpeta **data** del directorio **tracking_wo_bnw**.
3.  Descargar el siguiente [zip](https://drive.google.com/file/d/1PjTDHht_sftphKLiuxjFCIhN72vS3X_m/view?usp=sharing) necesario para realizar el tracking y descomprimirlo en la carpeta **output** del directorio **tracking_wo_bnw**. La estructura final debe ser la siguiente:
  - output
    - faster_rcnn_fpn_training_mot_17
    - tracktor
    - .DS_Store
    - .gitignore
4.  Entrar en el repositorio y descargar tracktor:
    `cd repositorio_clonado`
    `pip3 install -e .`
5.  Indicar en el archivo **/tracking_wo_bnw/experiments/cfgs/tracktor.yaml**, en el parámetro _dataset_ si queremos trackear el conjunto de entrenamiento (dataset: peds1_train) o el de test (dataset: peds1_test).
6.  Realizar el tracking: `python tracking_wo_bnw/experiments/scripts/test_tracktor.py` 
7.  Ejecutar el script **create_tracking_results.py** para crear la carpeta **tracking_results**, que se usa como entrada en el algoritmo de detección de anomalías: `python create_tracking_results.py`
8.  Ejecutar el algoritmo: `python run.py`
9.  Ejecutar el script **create_test_folder.py** para crear la carpeta **test_wo_bnw**, necesaria para calcular las métricas: `python create_test_folder.py`
10. Ejecutar el script **metrics.py**: `python metrics.py ./gt/ ./test_wo_bnw/`
