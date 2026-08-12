# ⚡ ZeroTrace — AI-Powered Telegram Bot

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:050505,50:6a00ff,100:00e5ff&height=220&section=header&text=ZeroTrace&fontSize=65&fontColor=ffffff&animation=fadeIn&fontAlignY=35" width="100%" />
</p>

<p align="center">
  <b>🤖 An AI-powered Telegram assistant built with Python, Gemini & Telegram Bot API.</b>
</p>

<p align="center">
  <i>Smart. Fast. Interactive. Built for the ZeroTrace community.</i>
</p>

<p align="center">

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge\&logo=python\&logoColor=white)](https://www.python.org/)
[![Telegram](https://img.shields.io/badge/Telegram-Bot-26A5E4?style=for-the-badge\&logo=telegram\&logoColor=white)](https://telegram.org/)
[![Google Gemini](https://img.shields.io/badge/Google-Gemini-8E75B2?style=for-the-badge\&logo=google\&logoColor=white)](https://ai.google.dev/)
[![Requests](https://img.shields.io/badge/HTTP-Requests-2CA5E0?style=for-the-badge)](https://requests.readthedocs.io/)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](#-license)

</p>

---

## 🌌 About ZeroTrace

**ZeroTrace** is a Python-based Telegram AI bot designed to provide an interactive and intelligent experience directly inside Telegram.

The bot combines:

* 🤖 Google Gemini AI
* 📱 Telegram Bot API
* ✨ Fancy text transformation
* 🔗 URL shortening
* 🌐 Social-media integration
* ⚡ Simple command-based interaction
* 🧠 AI-powered conversational responses

The bot receives normal Telegram messages, sends them to the Gemini model, transforms the generated response into a stylized format, and sends the final response back to the user.

---

## ✨ Features

### 🤖 AI Assistant

ZeroTrace uses Google's Gemini API to generate AI responses.

The current implementation initializes the Gemini client from environment credentials and uses:

`gemini-3.1-flash-lite`

for response generation.

The AI is configured to behave like a natural Telegram assistant with concise, friendly and technical responses.

---

### 📱 Telegram Integration

The bot is built using `pyTelegramBotAPI`.

It supports Telegram commands and normal text messages.

Example:

```text
/start
/social_media
/contact_us
/shortner
```

Any message that does not match a dedicated command can be processed by the AI assistant.

---

### 🎨 Fancy Text

AI-generated responses are passed through a text transformation service before being sent to Telegram.

The project includes a reusable:

```text
transform_text()
```

function that communicates with the Fancy Text Decorator API.

This makes the bot's responses visually more interesting.

---

### 🔗 URL Shortener

ZeroTrace includes a URL-shortening utility.

Users can send a long URL after using:

```text
/shortner
```

The bot validates the URL and sends the shortened result back.

The current implementation uses TinyURL's API.

---

### 🌐 Social Media Command

The `/social_media` command displays the project's social profiles and community links.

The current source already contains links for:

* YouTube
* Instagram
* Discord
* Facebook
* Telegram
* X / Twitter

You can customize these links for your own project.

---

### 📞 Contact Command

The `/contact_us` command provides a simple way for users to access the project's community/contact destination.

---

## 🧠 How It Works

```text
                 ┌──────────────────┐
                 │      Telegram    │
                 │      User        │
                 └────────┬─────────┘
                          │
                          ▼
                 ┌──────────────────┐
                 │   ZeroTrace Bot  │
                 │    main.py       │
                 └────────┬─────────┘
                          │
              ┌───────────┼───────────┐
              │           │           │
              ▼           ▼           ▼
          Commands       Tools       AI
              │           │           │
              │           │           ▼
              │           │     ┌─────────────┐
              │           │     │   Gemini    │
              │           │     │     API     │
              │           │     └──────┬──────┘
              │           │            │
              │           └────────────┤
              │                        ▼
              │                 AI Response
              │                        │
              │                        ▼
              │                 Fancy Text API
              │                        │
              └────────────────────────┤
                                       ▼
                              ┌────────────────┐
                              │ Telegram User  │
                              └────────────────┘
```

---

# 📁 Project Structure

```text
ZeroTrace/
│
├── main.py
├── agent.py
├── config.py
├── tools.py
├── font_change.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

### `main.py`

The main Telegram bot application.

It:

* Initializes the Telegram bot
* Registers commands
* Handles `/start`
* Handles `/social_media`
* Handles `/contact_us`
* Handles `/shortner`
* Processes normal messages
* Sends AI responses back to users

---

### `agent.py`

Contains the Gemini AI integration.

It initializes the Google GenAI client and contains the AI system instruction.

The main AI function is:

```text
explain_ai(prompt)
```

---

### `font_change.py`

Contains the fancy-text transformation functionality.

It sends text to the Fancy Text Decorator API and returns the transformed output.

---

### `tools.py`

Contains utility functionality such as URL shortening.

The current implementation uses TinyURL.

---

### `config.py`

Loads environment variables using `python-dotenv`.

The current project expects:

```env
TELEGRAM_BOT_TOKEN=YOUR_TELEGRAM_BOT_TOKEN
CHAT_ID=YOUR_CHAT_ID
```

---

### `requirements.txt`

Current dependencies include:

```text
pyTelegramBotAPI
python-dotenv
google-genai
requests
```

---

# 🚀 Installation

## 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/ZeroTrace.git
cd ZeroTrace
```

Replace `YOUR_USERNAME` with your GitHub username.

---

## 2. Create a Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔐 Environment Variables

Create a file named:

```text
.env
```

Add:

```env
TELEGRAM_BOT_TOKEN=YOUR_TELEGRAM_BOT_TOKEN
CHAT_ID=YOUR_CHAT_ID
GEMINI_API_KEY=YOUR_GEMINI_API_KEY
```

> ⚠️ Never publish your `.env` file or expose your API keys.

Add `.env` to `.gitignore`:

```gitignore
.env
venv/
__pycache__/
*.pyc
```

---

# 🔑 Getting Your Telegram Bot Token

1. Open Telegram.
2. Search for `@BotFather`.
3. Start a conversation.
4. Use `/newbot`.
5. Follow the instructions.
6. Copy the generated bot token.
7. Put it inside your `.env`.

Example:

```env
TELEGRAM_BOT_TOKEN=123456789:YOUR_SECRET_TOKEN
```

Never share this token publicly.

---

# 🧠 Getting a Gemini API Key

Create a Google Gemini API key through Google's AI developer platform.

Then add it to:

```env
GEMINI_API_KEY=YOUR_GEMINI_API_KEY
```

The project loads environment variables using `python-dotenv` and initializes the GenAI client from those credentials.

---

# ▶️ Run the Bot

After configuring the environment:

```bash
python main.py
```

If everything is configured correctly, the bot will start polling Telegram.

You can then open your Telegram bot and send:

```text
/start
```

---

# 🤖 Available Commands

| Command         | Description                           |
| --------------- | ------------------------------------- |
| `/start`        | Display the ZeroTrace welcome message |
| `/social_media` | Display social-media/community links  |
| `/contact_us`   | Display contact/community information |
| `/shortner`     | Shorten a long URL                    |
| Normal message  | Send the message to the AI assistant  |

---

# 💬 Example Interaction

```text
User:
Explain artificial intelligence.

ZeroTrace:
AI is a technology that allows computers to perform tasks
that normally require human intelligence...
```

The response is then processed through the project's fancy-text transformation layer.

---

# 🛠️ Customization

## Change Bot Name

Search inside `main.py` for:

```text
ZeroTrace
```

and replace it with your preferred project name.

---

## Change Welcome Message

The `/start` response is defined inside `main.py`.

You can customize:

* Bot description
* Emojis
* Community message
* Branding
* Call-to-action
* Project information

---

## Change Social Links

Inside `main.py`, locate the `/social_media` section.

You can replace the existing destinations with your own:

```text
YouTube
Instagram
Discord
Facebook
Telegram
X / Twitter
LinkedIn
```

---

# 🌐 Official Social Profiles

> Replace the placeholders below with your actual profiles.

<p align="center">

<a href="https://discord.gg/zerotrace">
<img src="https://img.shields.io/badge/Discord-Join%20Community-5865F2?style=for-the-badge&logo=discord&logoColor=white">
</a>

<a href="https://youtube.com/@zerotraceroot">
<img src="https://img.shields.io/badge/YouTube-Subscribe-FF0000?style=for-the-badge&logo=youtube&logoColor=white">
</a>

<a href="https://www.instagram.com/zerotraceroot/">
  <img src="https://img.shields.io/badge/Instagram-Follow-E4405F?style=for-the-badge&logo=instagram&logoColor=white">
</a>


<a href="https://x.com/tech_by_niteshh">
<img src="https://img.shields.io/badge/X-Follow-000000?style=for-the-badge&logo=x&logoColor=white">
</a>

<a href="https://www.linkedin.com/in/nitesh-chaurasiya-a7b2aa3a5/">
<img src="https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white">
</a>

</p>

### 🔗 Social Link Configuration

Replace these values:

```text
YOUR_DISCORD_URL
YOUR_YOUTUBE_URL
YOUR_TWITTER_URL
YOUR_LINKEDIN_URL
```

with your real links.

Example:

```text
Discord    → https://discord.gg/YOUR_SERVER
YouTube    → https://youtube.com/@YOUR_CHANNEL
X          → https://x.com/YOUR_USERNAME
LinkedIn   → https://linkedin.com/in/YOUR_USERNAME
```

---

# 👨‍💻 Developer

## tech_by_niteshh

<p align="center">
  <img src="https://github-readme-activity-graph.vercel.app/graph?username=tech-by-niteshh&theme=react-dark&hide_border=true" width="100%">
</p>

### Profile

```text
👨‍💻 Developer     : tech_by_niteshh
🤖 Project         : ZeroTrace
🧠 Focus           : AI • Automation • Python
📱 Platform        : Telegram
⚡ Architecture    : Python + Gemini + Telegram Bot API
```

### Developer Links

| Platform       | Link                |
| -------------- | ------------------- |
| 🐙 GitHub      | `YOUR_GITHUB_URL`   |
| 💬 Discord     | `YOUR_DISCORD_URL`  |
| ▶️ YouTube     | `YOUR_YOUTUBE_URL`  |
| 𝕏 X / Twitter | `YOUR_TWITTER_URL`  |
| 💼 LinkedIn    | `YOUR_LINKEDIN_URL` |

---

# 🧑‍💻 Contributors

Want to improve ZeroTrace?

You're welcome.

### Contribution Flow

```text
Fork
  ↓
Clone
  ↓
Create Branch
  ↓
Make Changes
  ↓
Test
  ↓
Commit
  ↓
Push
  ↓
Create Pull Request
```

Example:

```bash
git checkout -b feature/my-new-feature

git add .

git commit -m "Add new feature"

git push origin feature/my-new-feature
```

Then open a Pull Request on GitHub.

---

# 💡 Ideas for Future Versions

Some possible improvements:

* [ ] Admin dashboard
* [ ] User database
* [ ] AI conversation history
* [ ] Multiple AI models
* [ ] Image generation
* [ ] Voice message support
* [ ] Speech-to-text
* [ ] Text-to-speech
* [ ] Telegram inline mode
* [ ] User preferences
* [ ] Rate limiting
* [ ] Analytics
* [ ] Better error handling
* [ ] Docker support
* [ ] Web dashboard
* [ ] Plugin architecture
* [ ] Multi-language support

---

# 🔒 Security

Never commit secrets such as:

```text
TELEGRAM_BOT_TOKEN
GEMINI_API_KEY
API keys
Private tokens
Passwords
```

Use environment variables instead.

Your `.gitignore` should contain:

```gitignore
.env
venv/
__pycache__/
*.pyc
```

If you accidentally expose a Telegram bot token, immediately revoke/regenerate it through BotFather.

---

# ⚠️ Current Implementation Notes

The current source uses external services for two important operations:

### Gemini

AI responses are generated through Google's GenAI API.

### Fancy Text Decorator

AI responses are passed to:

```text
https://fancytextdecorator.com/api.php
```

for text transformation.

### TinyURL

URL shortening currently uses the TinyURL API.

Because these services are external dependencies, their availability and behavior may affect the bot.

---

# 🐛 Troubleshooting

## Bot doesn't start

Check:

```text
TELEGRAM_BOT_TOKEN
```

in your `.env`.

Then verify that your dependencies are installed:

```bash
pip install -r requirements.txt
```

---

## Gemini responses aren't working

Check:

```text
GEMINI_API_KEY
```

and make sure your API credentials are valid.

Also check the terminal output for Gemini API errors.

---

## URL shortening doesn't work

Make sure the URL starts with:

```text
http://
```

or:

```text
https://
```

The bot validates URLs before attempting to shorten them.

---

## Fancy text isn't working

The fancy-text transformation function communicates with an external API.

If that service is unavailable, the transformation step can fail.

---

# 📜 License

This project is released under the MIT License.

You are free to:

* Use it
* Modify it
* Distribute it
* Build upon it

as long as the license requirements are followed.

---

# ⭐ Support the Project

If you find ZeroTrace useful:

⭐ Star the repository
🍴 Fork the project
🐛 Report bugs
💡 Suggest features
🤝 Contribute code
📢 Share the project

Every contribution helps the project grow.

---

# 🌌 ZeroTrace

<p align="center">

<b>Where curiosity meets something extraordinary.</b>

<br><br>

🤖 AI • ⚡ Automation • 🐍 Python • 📱 Telegram

<br><br>

<a href="YOUR_DISCORD_URL">Discord</a>
  •   <a href="YOUR_YOUTUBE_URL">YouTube</a>
  •   <a href="YOUR_TWITTER_URL">X</a>
  •   <a href="YOUR_LINKEDIN_URL">LinkedIn</a>

</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:00e5ff,50:6a00ff,100:050505&height=120&section=footer" width="100%" />
</p>

---

<p align="center">
  Made with ❤️ and Python by <b>tech_by_niteshh</b>
</p>
