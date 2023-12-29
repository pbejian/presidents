# Utiliser une image de base Python officielle
FROM python:3.8

# Définir le répertoire de travail dans le conteneur
WORKDIR .

# Copier les fichiers de dépendances et installer les dépendances
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copier le reste des fichiers de l'application
COPY . .

# Exposer le port sur lequel FastAPI s'exécutera
EXPOSE 8001

# Définir la commande pour démarrer l'application
CMD ["uvicorn", "pierre_back:app", "--host", "0.0.0.0", "--port", "8001"]

# 0.0.0.0:8001
# docker build -t presidents .
# docker run -d --name presidents-container -p 8001:8001 presidents
# CMD ["uvicorn", "pierre_back:app", "--host", "0.0.0.0", "--port", "8001"]