# notes
## 1. 장고에 있는 모든 class들은 string method를 가지고 있다.
- 파이썬이 class를 발견하면 class를 마치 string 처럼 보여주는데 이 method를 파이썬에서 `__str__` 이라고 표시한다.

## 2. Meta Class란,
- 모델 내의 모든 class들 안에 있는 class이다. 많은 것들을 설정할 수 있다. 

## 3. Relation
- 장고에서는 연결된 object에서 value값을 얻을 수 있다.
- foreign key를 정의하면 foreign key를 정의한 그 object의 값들에 접근할 수 있는 것이다.

## 4. Model 작업
- models.py => admin.py => 마지막으로 settings.py 에서 PROJECT_APPS에 설치한다.
- 위 순서가 중요한 것은 아니고 makemigrations 하기 전에 모두 끝내면 된다.
- 그리고 python manage.py makemigrations => python manage.py migrate 하면 적용된다.

## 5. App 생성
- django-admin startapp [appName]