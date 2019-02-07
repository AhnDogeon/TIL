mkdir DG1

cd DG1

pyenv virtualenv 3.6.8 DG1

pyenv local DG1

pip list

pip install django django-extensions ipython





(DG1) dogeonzzang:~/workspace/DG1 $ django-admin startproject dg1
(DG1) dogeonzzang:~/workspace/DG1 $ django-admin startproject dg1 .
(DG1) dogeonzzang:~/workspace/DG1 $ django-admin startapp menu
(DG1) dogeonzzang:~/workspace/DG1 $ mkdir -p dg1/templates/dg1