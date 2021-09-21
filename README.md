# Космический Телеграм

Проект скачивает космические фотографии:

- последнего запуска SpaceX через [SpaceX REST API](https://github.com/r-spacex/SpaceX-API);
- APOD и EPIC фото NASA через [NASA API](https://api.nasa.gov/).

Скачанные фото проект публикует в канал Telegram раз в сутки.

### Как установить

__Настройки параметров окружения.__ Для работы проекта файл `.env`, лежащий в одном каталоге с проектом, должен содержать следующие данные:

- `NASA_API_KEY` — необходим для использования NASA API. Можно получить на [api.nasa.gov/](https://api.nasa.gov/);
- `TG_TOKEN` — токен телеграм-бота, который будет публиковать фото в канал. Создать бота и получить токен можно через телеграм-бота [@BotFather](https://t.me/botfather);
- `CHAT_ID` — ID канала, на котором будут публиковаться фото (короткая ссылка на него).

Пример содержания файла.`env`:
```
NASA_API_KEY=demo_key
TG_TOKEN=token
CHAT_ID=@channel
```

__Важно!__ Чтобы бот мог публиковать фото на канале, он должен быть назначен администратором этого канала.

Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, если есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```

### Как использовать

Cкачать фото с последнего запуска SpaceX:

```
fetch_spacex.py
```

Скачать фото APOD и EPIC от NASA:
```
fetch_nasa.py
```

Запустить публикацию скачанных фото в Telegram раз в сутки:
```
post_in_tg.py
```

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).