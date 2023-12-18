## Projet Présidents

Pour construire l'image Docker :

```bash
docker build -t presidents .
```

Pour lancer le conteneur :

```bash
docker run -d --name presidents-container -p 8001:8001 presidents
```
