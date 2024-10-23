## Дорожная карта работы над проектом.

1. Подготовка к работе: 
   - Создал проект в Pycharm
   - Сформировал файл .gitignore для исключения передачи не нужных файлов на ГитХаб
   - Сформировал файл readme.md с описанием задания
   - Сформировал файл road_map.md для ведения дорожной карты проекта
   - Установил Django в папку с проектом командой pip install django
   - Создал проект командой django-admin startproject zsvsite 
   - Переименовал zsvsite в settings для удобства
   - Установил библиотеку pillow для работы с файлами
   - Установил базовые миграции - python manage.py migrate
   - Создал суперпользователя - python manage.py createsuperuser 
   - Запустил сервер для проверки работы - python manage.py runserver

2. Разработка:
   - *Функционал регистрации, авторизации и выхода пользователя* 
   - Регистрация:
       - Создал приложение для работы с пользователями - python manage.py startapp regapp
       - Подключил приложение в файле settings.py проекта - INSTALLED_APPS = ['regapp']
       - Создал файл urls.py в regapp и подключил его в файле urls.py в settings - path('', include('regapp.urls'))
       - В regapp создал папку с шаблонами - templates/regapp
       - Создал базовый шаблон (пока пустой) для тестирования работы - base.html
       - Создал шаблон регистрации нового пользователя - reg-page.html
       - В regapp создал файл form.py для работы с формами 
       - В forms.py создал класс CustomUserForm расширяющий UserCreationForm для добавления
       поля email при регистрации
       - В views.py создал класс BaseView(TemplateView) для отображения базового шаблона
       - В views.py создал класс RegisterView(CreateView) в котором прописана логика
       добавления нового пользователя при регистрации с последующей авторизацией
       - В urls.py прописал путь для базового шаблона - path("", BaseView.as_view(), name="base-page")
       - В urls.py прописал путь для шаблона регистрации - path("reg/", RegisterView.as_view(), name="registration")
       - Проверил функционал регистрации пользователя
     - Авторизация:
       - Создал шаблон для авторизации пользователя - authorisation.html
       - В views.py создал класс MyLoginView(LoginView) для отображения формы авторизации
       - В urls.py прописал путь для формы авторизации - path("login/", MyLoginView.as_view(), name="login")
       - Создал шаблон который вид авторизованный пользователь - registered.html
       - В views.py создал класс RegisteredView(TemplateView) для отображения страницы авторизованного пользователя
       - В urls.py прописал путь для формы авторизации - path("lk/", RegisteredView.as_view(), name="registered")
       - Проверил функционал авторизации пользователя
     - Выход:
       - В views.py создал класс MyLogoutView(LogoutView) для выполнения выхода пользователя
       - В шаблоне registered.html добавил блок: 
      <form action="{% url 'zsvapp:logout' %}" method="post">
      {% csrf_token %}
      <button type="submit">Выход</button>
      </form>
      Это необходимо для правильной отработки выхода в классе MyLogoutView
       - В urls.py прописал путь для выполнения выхода - path("logout/", MyLogoutView.as_view(), name="logout")
       - Проверил функционал выхода пользователя
   - *Создание моделей*
     - Создание модели Ингридиентов




