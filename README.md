# Truy vấn SQL với Django
 ->  python manage.py shell
 ->  from <folder>.models import <class>
 -> a = <class>()
 -> Nhập thông tin -> a.save()
 -> <class>.objects.all()
 -> a = <class>.objects.get(id=#)
 
 # Tạo App
 -> python manage.py startapp <folder_name>
 # Tạo Database
 -> python manage.py makemigrations <folder_name>
 -> python manage.py migrate
 # Tạo tài khoản admin
 -> python manage.py createsuperuser
 # Chạy test
 -> python manage.py test <folder>
 # Add folder 'static/home' to folder 'home' to run code
 
