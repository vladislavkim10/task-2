from flask import Flask
import redis
# Создаётся объект flask
app = Flask(__name__)
# Параметры подключения к redis
r = redis.Redis(host="redis", port=6379)
# Маршрут ping, возвращает ok
@app.route("/ping")
def ping():
    return {"status": "ok"}
# Маршрут count,использует redis для сохранения значения счётчика
@app.route("/count")
def count():
    new_value = r.incr("visit_count")
    return {"count": new_value}
# Приложение доступно со всех интерфейсов внутри контейнера, слушает на 5000 порту
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
