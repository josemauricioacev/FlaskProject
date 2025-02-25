#SO y imagen base
FROM python:3.12-slim

#Directorio de trabajo
WORKDIR /app

#Copia de archivos #git clone
COPY . /app

#Instalación de dependencias
RUN pip install --no-cache-dir -r requirements.txt

#Puerto de la aplicación
EXPOSE 5000

CMD ["python","app.py"]