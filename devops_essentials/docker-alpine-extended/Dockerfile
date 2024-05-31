# Utilisation de l'image de base Alpine
FROM alpine:latest

# Installation du paquet curl
RUN apk add --no-cache curl

# Ajout du fichier de configuration au conteneur
COPY config.txt /app/config.txt

# Commande par défaut lors de l'exécution du conteneur
CMD [ "echo", "Hello, World!" ]
