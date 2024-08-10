# 19.2 Знакомство с Django - Домашняя работа

Ключевые слова:
- 19.2 Знакомство с Django
- skypro_python41.0
- Урок 19.2
- django
- startproject
- startapp

### Критерии выполнения заданий
- [x] Всё итоговое решение залили в github.com и сдали в виде ссылки на репозиторий.
- [x] Создали отдельное приложение.
- [x] Реализовали два контроллера homepage и contacts.
- [x] Адреса описали не внутри главного URL-файла urls.py, а вынесли в пространства имен.
- [x] Добавили папку с шаблонами, в которой лежат два шаблона templates/catalog/homepage.html и templates/catalog/contacts.html.


### Задание 1
Для начала работы над задачей выполните первые шаги:

- Настройте виртуальное окружение.
- Создайте новый Django-проект.

```bash
 export PY_PROJECT=skypro_homework_19.2 #наименование проекта
 mkdir $PY_PROJECT  #создаем директорию проекта
 cd $PY_PROJECT #переходим в рабочую директорию
 django-admin startproject config . #инициализируем проект
 python3 -m venv env #создаем виртуальное окружение
 source env/bin/activate #переходим в виртуальное окружение
 pip3 install django #устанавливаем в виртуальном окружении django
 pip install --upgrade pip
 pip3 freeze > requirements.txt #записываем зависимости
```

Создание Git-репозитория
```bash
git config --global user.name "Valeev Azamat"
git config --global user.email vazamat@gmail.com
git config --global init.defaultBranch main

git init
touch .gitignore
```
и записываем в .gitignore стандартные настройки для игнорирования

### Задание 2
После успешного создания проекта сделайте первую настройку. Для этого:

 - Создайте первое приложение с названием  catalog.
 - Внесите начальные настройки проекта.
 - Сделайте настройку урлов (URL-файлов) для нового приложения.

```bash
python3 manage.py startapp catalog
touch catalog/urls.py
mkdir -p catalog/templates/catalog
mkdir -p static/css static/js static/images
```

### Задание 3
- Подготовьте два шаблона для домашней страницы и страницы с контактной информацией.


### Задание 4
В приложении в контроллере реализуйте два контроллера:

- Контроллер, который отвечает за отображение домашней страницы.
- Контроллер, который отвечает за отображение контактной информации.
 
### Дополнительное задание

- Реализуйте обработку сбора обратной связи от пользователя, который зашел на страницу контактов и отправил свои данные для обратной связи.