import streamlit as st
from utils.pdf_utils import extract_text_from_pdf
from utils.qa_utils import build_vectorstore, get_qa_chain

# Inject dark theme CSS
with open("assets/dark-theme.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.set_page_config(page_title="😈 Devil's Notes Chat", layout="wide")
st.title("👹 SRIJAN’S DEVIL Q&A BOT")

pdf = st.file_uploader("📄 Upload your notes (PDF)", type="pdf")

if pdf:
    text = extract_text_from_pdf(pdf)
    if not text.strip():
        st.error("No text found in PDF!")
    else:
        vectorstore = build_vectorstore(text)
        qa = get_qa_chain()

        query = st.text_input("💬 Ask your notes:")
        if query:
            docs = vectorstore.similarity_search(query)
            answer = qa.run(input_documents=docs, question=query)
            st.success(answer)

            if 'history' not in st.session_state:
                st.session_state.history = []
            st.session_state.history.append((query, answer))

        if 'history' in st.session_state:
            st.markdown("---")
            st.subheader("🧠 Chat History")
            for i, (q, a) in enumerate(st.session_state.history[::-1]):
                st.write(f"**Q{i+1}:** {q}")
                st.write(f"**A{i+1}:** {a}")
else:
    st.info("👹 Upload a PDF to summon the demon.")

