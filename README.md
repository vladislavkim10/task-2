# Задание 2

## 🚀 Flask + Redis Counter
Мини-проект на Flask, который использует Redis для хранения счётчика посещений

---

## 🧾 Функциональность

- `GET /ping` — проверка доступности API
- `GET /count` — увеличивает Redis-счётчик и возвращает его значение

---

## 📍 Результаты работы:
```
    task2 docker compose up -d   
[+] Running 2/2
 ✔ Container flask-app-1  Started                                                                                                                                                     0.5s 
 ✔ Container redis        Started                                                                                                                                                     0.2s 
➜  task2 docker ps                
CONTAINER ID   IMAGE          COMMAND                  CREATED          STATUS         PORTS                                         NAMES
39701a42d047   task2-web      "python app.py"          4 seconds ago    Up 3 seconds   0.0.0.0:5000->5000/tcp, [::]:5000->5000/tcp   flask-app-1
db8aec8591a4   redis:alpine   "docker-entrypoint.s…"   42 seconds ago   Up 4 seconds   0.0.0.0:6379->6379/tcp, [::]:6379->6379/tcp   redis
➜  task2 curl http://localhost:5000/count
{"count":1}
➜  task2 curl http://localhost:5000/count
{"count":2}
➜  curl http://localhost:5000/ping 
{"status":"ok"}
```
