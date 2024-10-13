# API project

Это учебный проект для начала работы с фреймворком FastAPI

### Роуты

- `/sum1n` - принимает GET запросы.

Возвращает сумму от 1 до n.

Пример запроса.

```bash
$ curl http://localhost:8000/sum1n/10
{"result": 55}
```

- `/fibo`- принимает GET запросы.

Возвращает n-ное число из последовательности Фибоначчи.

Пример запроса.

```bash
$ curl http://localhost:8000/fibo?n=5
{"result": 3}
```

---

- `/reverse` - принимает POST запросы.

Возвращает перевернутую строку (переданную через Header) задом наперед.

Пример запроса.

```bash
$ curl -X POST -H "string: hello" http://localhost:8000/reverse
{"result": "olleh"}
```

---

- `/list` - пинимает PUT запросы.

Принимает строку `element` через JSON тело запроса и сохраняет ее в глобальный массив.

Пример запроса.

```bash
$ curl -X PUT -d '{"element":"Apple"}' -H 'Content-Type: application/json' http://localhost:8000/list
$ curl -X PUT -d '{"element":"Microsoft"}' -H 'Content-Type: application/json' http://localhost:8000/list
$ curl http://localhost:8000/list
{"result": ["Apple", "Microsoft"]}
```

---

- `/list` - принимает GET запросы.

Возвращает глобальный массив.


```bash
$ curl http://localhost:8000/list
{"result": []}
$ curl -X PUT -d '{"element":"Apple"}' -H 'Content-Type: application/json' http://localhost:8000/list
$ curl -X PUT -d '{"element":"Microsoft"}' -H 'Content-Type: application/json' http://localhost:8000/list
$ curl http://localhost:8000/list
{"result": ["Apple", "Microsoft"]}
```

---

- `/calculator`, принимающий POST запросы.

Принимает строку в формате: `num1,operator,num2`.

- `num1` и `num2` - числа
- `operator` - математическая операция: +,-,/,\*

Возвращает результат математического выражения.

Пример запроса.

```bash
$ curl -X POST -d '{"expr": "1,+,1"}' -H 'Content-Type: application/json' http://localhost:8000/calculator
{"result": 2}
```

### Требования

- Python3.6+, т.е. версия языка Python от 3.6 и выше
- pip, менеджер пакетов Python

### Запуск

Для начала работы с проектом, форкните и склонируйте репозиторий на свой компьютер. В командной строке перейдите в директорию проекта. Чтобы установить необходимые зависимости, запустите следующую команду:

```bash
pip install requirements.txt
```
Чтобы проверить корректность установки, наберите команду:

```bash
uvicorn main:app
```
