ОДИН РАЗ (в Termux):
  pkg update && pkg install git openssh
  git config --global user.name "Rootya"
  git config --global user.email "you@example.com"
Создай пустой репозиторий на github.com, затем:
  cd проект
  git init -b main && git add . && git commit -m init
  git remote add origin https://github.com/ЛОГИН/РЕПО.git
  git push -u origin main   (вместо пароля - Personal Access Token)

КАЖДЫЙ РАЗ:
  правишь main.py -> git add . && git commit -m up && git push
GitHub сам соберёт APK (первый раз ~20-30 мин, потом быстрее).
Скачать: репозиторий -> Actions -> последний запуск -> Artifacts -> apk.
