# Emotion Detection — IBM Watson NLP

Proyecto Python/Flask para IBM Skills Network. El código usa el servicio de laboratorio Watson NLP que requiere conectividad desde el entorno de IBM.

## Ejecutar

```bash
python -m pip install -r requirements.txt
python -c "from EmotionDetection import emotion_detector; print('Import successful')"
python -m unittest -v test_emotion_detection.py
python -m pylint server.py
python server.py
```

Abre http://127.0.0.1:5000/ en el navegador. Introduce una frase en **inglés**, por ejemplo `I am very happy today`.

El servicio remoto de IBM puede no estar disponible desde algunos entornos: las pruebas unitarias usan respuestas simuladas, por lo que comprueban la lógica sin depender de la red.

## Qué capturar para Mark

1. **Repositorio:** abre el árbol de archivos en el IDE, incluyendo `EmotionDetection/`, `server.py`, `templates/` y `test_emotion_detection.py`. Clona por separado el repositorio original de la actividad si el instructor exige evidenciar un `git clone` real.
2. **Detector:** muestra la función `emotion_detector` y el comando de importación ejecutado sin errores.
3. **Formato:** muestra el diccionario generado por una frase válida, con las seis claves esperadas.
4. **Paquete:** muestra `EmotionDetection/__init__.py` y un `from EmotionDetection import emotion_detector` correcto.
5. **Pruebas:** ejecuta `python -m unittest -v test_emotion_detection.py` y captura el resumen de pruebas correctas.
6. **Flask:** muestra `server.py`, ejecuta `python server.py` y captura la página con el resultado real.
7. **Errores:** muestra `status_code == 400` en el detector y prueba el campo vacío en la web.
8. **Pylint:** ejecuta `python -m pylint server.py` y captura la puntuación final; si no es 10/10, revisa la salida en el entorno del curso.

**No uses imágenes inventadas como evidencia.** Las capturas deben mostrar la ejecución real de tu proyecto en el entorno donde lo entregarás.
