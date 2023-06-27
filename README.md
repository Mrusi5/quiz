
<br>Этот проект делает запросы к публичному API https://jservice.io/api/random?count=1 указанное количество раз.
<br>Сохраняет информацию в таблице questions(id, question_id, question_text, answer_text, created_at)
<br>Как запустить проект:
<br>
<br>    0) Создать базу данных postgresql через docker: docker run -p 5432:5432 --name nameapp -e POSTGRES_USER=username -e POSTGRES_PASSWORD=password -e POSTGRES_DB=namedb -d postgres:13.3
<br>        
<br>    1) В файле .env изменить переменные DB_USER, DB_PASS, DB_NAME, DB_PORT на используемые.
<br>
<br>    2) Для активации работы необходимо зайти в папку проекта, через консоль.
<br>
<br>    3) Прописать docker-compose build. 
<br>
<br>    4) После создания контейнеров, прописать docker-compose up.
<br>
<br>    5) Вышеперечисленные действия запустили проект. Для пользования функционалом необходимо перейти на http://127.0.0.1:8000/docs
<br>
<br>   6) Развернуть вкладку "/quiz".
<br>
<br>   7) Нажать "Try it out" в правом верхнем углу и прописать в строке "questions_num" число необходимых вопросов.
<br>
<br>Проект проверяет вопрос на уникальность и делает запросы пока вопрос не окажется уникальным.
<br>Выводит последний вопрос в БД.
    
