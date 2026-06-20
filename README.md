# 🤖 Q&A Bot using Groq API and Python

A fast and intelligent Question & Answer chatbot built with **Python** and the **Groq API**. This project leverages Groq's ultra-fast LLM inference capabilities to provide accurate and real-time responses to user queries.

---

## 🚀 Features

* ⚡ Lightning-fast responses powered by Groq
* 🧠 Natural Language Understanding
* 💬 Interactive Question & Answer Interface
* 🔄 Continuous conversation support
* 🛠 Easy setup and customization
* 🔐 Secure API key management using environment variables
* 📦 Lightweight and beginner-friendly codebase

---

## 🏗️ Tech Stack

* **Python 3.9+**
* **Groq API**
* **dotenv**
* **Requests / Groq SDK**
* **Command Line Interface (CLI)**

---

## 📁 Project Structure

```bash
qa-bot-groq/
│
├── app.py                # Main chatbot application
├── requirements.txt      # Project dependencies
├── .env                  # Environment variables
├── README.md             # Project documentation
└── utils/
    └── helper.py         # Helper functions (optional)
```

---

## 🔧 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/qa-bot-groq.git
cd qa-bot-groq
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate the environment:

**Windows**

```bash
venv\Scripts\activate
```

**Mac/Linux**

```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Configure Groq API Key

Create a `.env` file in the project root directory:

```env
GROQ_API_KEY=your_groq_api_key_here
```

---

## ▶️ Run the Bot

```bash
python app.py
```

Example:

```text
You: What is Artificial Intelligence?

Bot: Artificial Intelligence (AI) refers to the simulation of human intelligence in machines that are programmed to think, learn, and solve problems.
```

---

## 💻 Sample Code

```python
from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

while True:
    question = input("You: ")

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "user", "content": question}
        ]
    )

    print("Bot:", response.choices[0].message.content)
```

---

## 📦 Requirements

```txt
groq
python-dotenv
```

Install them using:

```bash
pip install groq python-dotenv
```

---

## 🎯 Use Cases

* Educational Q&A Systems
* Customer Support Bots
* Knowledge Assistants
* Personal AI Assistants
* FAQ Automation
* Learning and Research Tools

---

## 🔒 Security Notes

* Never expose your Groq API key publicly.
* Add `.env` to your `.gitignore` file.
* Rotate API keys periodically.

Example `.gitignore`:

```gitignore
.env
venv/
__pycache__/
```

---

## 📈 Future Improvements

* Web-based UI using Flask or Streamlit
* Conversation memory
* PDF document Q&A
* Voice-enabled chatbot
* Database integration
* Multi-user support
* Authentication system

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome.

1. Fork the repository
2. Create a new branch
3. Commit your changes
4. Push to your branch
5. Open a Pull Request

---

## 📜 License

This project is licensed under the MIT License.

---

## ⭐ Support

If you found this project helpful, please consider giving it a ⭐ on GitHub.

Happy Coding! 🚀
