# Chat Log Summarizer

This project processes and summarizes chat logs (e.g., between a user and an AI) using TF-IDF keyword analysis. It is designed to work in a terminal-based environment and can summarize **multiple `.txt` chat files** from a specified folder.

---

## Features

- Reads chat logs formatted with `User:` and `AI:` lines
- Extracts meaningful keywords using TF-IDF
- Summarizes the nature of the conversation
- Supports batch processing of all `.txt` files in a folder
- Terminal-based — no UI required


---

## Project Structure

ai-chat-log-summarizer/
├── summarize_chats.py # Main script
├── chat_logs/ # Folder with chat log .txt files
│ ├── chat1.txt
│ ├── chat2.txt
│ └── ...
├── requirements.txt
└── README.md


---

## Setup (with virtual environment)

1. **Clone the repository**:

```bash
git clone https://github.com/sonjoy2074/ai-chat-log-summarizer
cd ai-chat-log-summarizer

pip install -r requirements.txt

python summarize_chats.py


