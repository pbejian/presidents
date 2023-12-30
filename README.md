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



Pour lancer l'application vous pouvez ouvrir un navifateur à l'URL suivante :

```
http://localhost:8001
```

Ou bien vous pouvez aller voir l'image et le conteneur dans l'application **Docker desktop** et lancer le conteneur d'un simple clic.





