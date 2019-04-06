# Dentro del directorio root del projecto
git status (ver el estado de tu projecto git)
git log (Historial de todos los commits)
git init (Inicializar projecto git)
git diff (Ver las differencias respecto a el ultimo commit)
git remote -v (Ver que repositiorio de tu projecyto actual es el remoto)

git add <FILE> # Anadir un archivo concreto para tu commit
git add . # Anadir todos los artchiuvos cambiados de la carpeta actual para tu commit
git add  <DIRECTORIO> # Anadir todos los artchiuvos cambiados de la carpeta especificada para tu commit

git commit -m "cualquier commentario"

git pull
git push

git set remote http://remote.com
# Para linkear un projecto link a un repositorio remoto
# git remote add origin https://github.com/Sersovi/demo_github.git

# Para descargar un projecto remote
# git clone https://github.com/Sersovi/demo_github.git

# Configurar git primera vex instalado
# git config --global user.email "@.."
# git config --global user.name "Your Name"