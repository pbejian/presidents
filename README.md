## Projet Présidents

Pour construire l'image Docker :

```bash
docker build -t presidents .
```

Pour construirte l'image lorsqu'on est sur un Mac Apple Silicon et que l'on veut partager avec du x86 :

```
docker build --platform linux/amd64 -t presidents .
```

Pour lancer le conteneur :

```bash
docker run -d --name presidents-container -p 8001:8001 presidents
```
