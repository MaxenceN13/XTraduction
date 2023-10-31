# Description
Bot Twitter qui publie les messages traduits, dans la langue de notre choix, d'un compte Twitter.

# Installation
1. Clonez le dépôt
```
git clone github.com/maxencen/TradInstant
```
2. Installez les dépendances
```
pip3 install -r requirements.txt
```
3. Créez un fichier config.py à la racine du projet et ajoutez-y les variables suivantes :
```
# Twitter API KEYS
API_KEY = ""
API_SECRET = ""

ACCESS_TOKEN = ""
ACCESS_TOKEN_SECRET = ""

BEARER_TOKEN = ""

# Deepl API KEY
DEEPL_AUTH_KEY = ""

# Twitter Bot Account Infos
BOT_TWITTER_ACCOUNT_ID = ""
BOT_TWITTER_ACCOUNT_NAME = ""
```

# Usage 

Sans Docker :
```
python3 main.py
```

Avec Docker :
```
docker build -t nom_de_votre_image .
docker run -d --name nom_de_votre_conteneur nom_de_votre_image
```