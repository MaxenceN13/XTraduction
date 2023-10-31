# Description
Permet de traduire les tweets sur demande. Il suffit de mentionner le bot en réponse au tweet à traduire, et le bot vous répondra avec la traduction du tweet. 

# Installation
1. Créez un compte développeur Twitter et récupérez les clés d'API
2. Clonez le dépôt
```
git clone https://github.com/MaxenceN13/TradInstant.git
```
3. Installez les dépendances
```
pip3 install -r requirements.txt
```
4. Créez un fichier config.py à la racine du projet et ajoutez-y les variables suivantes :
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