import setuptools
with open("README.md","r",encoding="utf_8") as f:
    long_description=f.read() #On importe setuptools et on lit le fichier README.md pour l'utiliser comme description longue du package

__version__="0.0.0"
REPO_NAME="mlops"
AUTHOR_USER_NAME="Merryyori"
SRC_REPO="mlproject"
AUTHOR_EMAIL="meryomelle@gmail.com"
#Définition des métadonnées du projet

setuptools.setup(
  name=SRC_REPO,
  version =__version__,
  author=AUTHOR_USER_NAME,
  author_email=AUTHOR_EMAIL,
  description="A small python package for ml app",
  Long_description=long_description,
  long_description_content_type="text/markdown",  # Corrigez le nom du paramètre !
  url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
  project_urls={
  "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
   },
  package_dir={"": "src"},#Indique que les packages sont dans le dossier "src"
  packages=setuptools.find_packages(where="src") #Trouve automatiquement tous les packages Python dans "src"


)
#Créer un package Python installable avec pip install -e