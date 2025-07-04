# chat-with-your-notes
Ask questions to your PDFs using AI.
# 👹 Chat With Your Notes — Powered by Srijan's Devil AI

**Talk to your PDFs like never before.**  
Upload lecture notes, manuals, research papers — and ask questions like you're chatting with a demon tutor who never sleeps.

> Built with 🔥 by [Srijan Reddy Thandra](https://github.com/SrijanReddyThandra)  
> Harnessing LangChain, FAISS, HuggingFace, and Streamlit.


## 🚀 Features

- 📄 Upload any text-based PDF
- 💬 Ask contextual questions about the content
- 🧠 Embeds your notes using `sentence-transformers`
- ⚙️ Uses `FAISS` for fast vector similarity
- 🤖 Answers powered by GPT2 (custom LLM) locally
- 🌑 Dark themed UI (devil mode enabled)
- 🧾 Saves chat history within session

---

## 🛠️ Tech Stack

| Component | Tool |
|----------|------|
| 💬 LLM | `HuggingFace GPT-2` via Transformers |
| 📚 Embeddings | `sentence-transformers` |
| 🔍 Vector DB | `FAISS` |
| 📎 PDF Parsing | `PyPDF2` |
| 🧠 Framework | `LangChain` |
| 🎨 UI | `Streamlit` |
| 🐍 Language | Python 3.9+ |

---

## 💻 Local Setup

```bash
# Clone the repo
git clone https://github.com/SrijanReddyThandra/chat-with-your-notes.git
cd chat-with-your-notes

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install requirements
pip install -r requirements.txt

# Run the devil 🧠
streamlit run app.py

