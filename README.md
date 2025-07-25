# Arbitrage Bot 🤖💸

Этот бот автоматически ищет арбитражные возможности на Binance и отправляет сигналы в Telegram.

---

## 🔧 Установка через Render

### 1. Загрузка проекта
Создай новый репозиторий на GitHub и загрузите туда файлы:
- `main.py`
- `requirements.txt`
- `.env.example` (необязательно, для примера)

---

### 2. Подключение GitHub к Render

1. Перейди на сайт: [https://render.com](https://render.com)
2. Нажми `New` → `Web Service`
3. Выбери GitHub → выбери свой репозиторий `Arbitrage-bot`

---

### 3. Конфигурация Web Service

| Поле | Значение |
|------|----------|
| **Name** | arbitrage-bot |
| **Branch** | main |
| **Build Command** | `pip install -r requirements.txt` |
| **Start Command** | `python main.py` |
| **Environment** | Python 3 |

---

### 4. Переменные окружения (.env)

Добавь эти переменные вручную в Render:

| Key | Значение |
|-----|----------|
| `TELEGRAM_TOKEN` | токен твоего Telegram-бота |
| `TELEGRAM_CHAT_ID` | твой chat_id в Telegram |
| `BINANCE_API_KEY` | Binance API ключ |
| `BINANCE_API_SECRET` | Binance секретный ключ |

---

### 5. Запуск

Нажми `Create Web Service`. Через 30–60 секунд бот должен заработать и начать отправлять сигналы в Telegram 📲

Если бот не работает — открой Logs и проверь сообщения об ошибке.

---

**Удачного трейдинга! 🚀**