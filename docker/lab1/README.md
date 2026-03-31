🧪 ЗАДАЧА 1

**Собери образ:**

базовый: nginx
положить свой index.html

чтобы при запуске:

docker run -p 8080:80 my-nginx

👉 страница открывалась в браузере


**Dockerfile**
FROM nginx:latest
COPY index.html /usr/share/nginx/html/index.html #index.html береться из папки где сейчас находишься

**Замечания**
👍 Что ты сделал правильно
✔️ 1. Использовал nginx как базу

👉 отлично, не изобретаешь велосипед

✔️ 2. Правильный путь
/usr/share/nginx/html/index.html

👉 это дефолтная папка nginx — прям в точку

✔️ 3. Не трогал CMD

👉 и поэтому nginx запустится сам — красавчик

⚠️ Что можно улучшить (вот тут рост 🚀)
🔸 1. НЕ используй latest

❌

FROM nginx:latest

👉 проблема:

сегодня работает
завтра обновился образ → всё сломалось

✅ лучше:

FROM nginx:1.25
🔸 2. Можно писать проще

❌

COPY index.html /usr/share/nginx/html/index.html

✅

COPY index.html /usr/share/nginx/html/

👉 nginx сам найдёт index.html

🔸 3. (опционально, но красиво)

Добавь метаданные:

LABEL maintainer="you"

**💥 Финальная версия (как у норм DevOps)**

*FROM nginx:1.25*
*COPY index.html /usr/share/nginx/html/*

**🚀 Как проверить**
docker build -t my-nginx .
docker run -p 8080:80 my-nginx

👉 открыть:

http://localhost:8080
