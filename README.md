# 👹 Chat With Your Notes  
### _"Where your PDFs speak... and obey."_  
**Built by [Srijan Reddy](https://github.com/SRIJAN2426)**

---

## 📘 Description

GenAI-powered PDF Q&A tool using LangChain, FAISS, GPT2 — built by Srijan Reddy.
No more CTRL+F. Just ask. Get answers. Like a demon that understands text---

## ✨ Features

- 📄 Upload any PDF file
- 🤖 Ask natural language questions
- 🔍 Get contextually accurate answers
- ⚡ Fast in-memory vector search with FAISS
- 💡 Powered by local HuggingFace models — no OpenAI key needed
- 🌑 Dark-themed Streamlit UI (custom CSS)

---

## 🧠 Tech Stack

| Layer        | Tool / Library              |
|-------------|-----------------------------|
| Frontend    | `Streamlit`                 |
| Backend     | `LangChain`, `SentenceTransformers` |
| Embeddings  | `all-MiniLM-L6-v2` (HuggingFace) |
| Language Model | `GPT2` from `transformers` |
| Vector Store| `FAISS`                     |
| PDF Parsing | `PyPDF2`                    |
.
---

## 🛠️ Local Setup Instructions

```bash
# Clone the repo
git clone https://github.com/SRIJAN2426/chat-with-your-notes.git
cd chat-with-your-notes

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
chat-with-your-notes/
│
├── app.py                  # Main Streamlit app
├── requirements.txt        # Python dependencies
├── .gitignore
├── README.md
│
├── assets/
│   └── dark-theme.css      # Optional Streamlit custom styling
│
└── utils/
    ├── pdf_utils.py        # PDF text extraction logic
    └── qa_utils.py         # Vectorstore & QA chain setup

---

## 🖼️ UI Preview (Optional)

> 📸 Add screenshots here after running locally — like:
> - File Upload Page
> - Question + Answer View
> - Dark theme magic

---

## 🔮 Future Scope

- [ ] Support multiple PDF uploads
- [ ] Deploy on Streamlit Cloud
- [ ] Add summarization + highlights
- [ ] Save chat history
- [ ] Voice-based queries 🗣️

---

## 🙌 Credits

- 👨‍💻 Built by [**Srijan Reddy**](https://github.com/SRIJAN2426)
- 🔗 Powered by:
  - [LangChain](https://www.langchain.com/)
  - [HuggingFace Transformers](https://huggingface.co/)
  - [FAISS](https://github.com/facebookresearch/faiss)
  - [Streamlit](https://streamlit.io/)

---

> 💥 Unleashing PDF-based AI... **Srijan-style.**

