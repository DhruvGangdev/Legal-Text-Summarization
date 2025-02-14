import streamlit as st
import fitz  # PyMuPDF
from transformers import T5Tokenizer, T5ForConditionalGeneration
import io

# Load the T5 tokenizer and model
tokenizer = T5Tokenizer.from_pretrained("/content/drive/MyDrive/fine_tuned_model")
model = T5ForConditionalGeneration.from_pretrained("/content/drive/MyDrive/fine_tuned_model")

def read_pdf(pdf_file):
    text = ""
    # Open the PDF file
    with io.BytesIO(pdf_file.read()) as f:
        pdf_document = fitz.open(stream=f, filetype="pdf")
        # Iterate over each page
        for page_num in range(len(pdf_document)):
            page = pdf_document.load_page(page_num)
            # Extract text from the page
            text += page.get_text()
    return text

def summarize_text(text):
    # Tokenize and encode the text for summarization
    inputs = tokenizer.encode("summarize: " + text, return_tensors="pt", max_length=1024, truncation=True)
    # Generate summary
    summary_ids = model.generate(inputs, 
                                 max_length=150, 
                                 min_length=40, 
                                 length_penalty=2.0, 
                                 num_beams=4, 
                                 early_stopping=True)
    # Decode the summary
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    return summary

def main():
    st.title("Legal Text Summarizer")
    st.markdown(
        """
        <style>
            .reportview-container {
                background: #f8f8f8;
            }
            .sidebar .sidebar-content {
                background: #f8f8f8;
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    # File uploader for PDF files
    st.sidebar.title("Upload PDF")
    pdf_file = st.sidebar.file_uploader("Upload a PDF file", type=['pdf'])

    if pdf_file:
        # Display the uploaded file
        st.sidebar.write(pdf_file.name)

        # Read text from the PDF file
        pdf_text = read_pdf(pdf_file)
        
        # Display the extracted text
        st.header("Text extracted from PDF:")
        st.write(pdf_text)

        # Summarize text
        if st.button("Summarize", key="summarize_btn"):
            with st.spinner("Summarizing..."):
                summary = summarize_text(pdf_text)
            # Display the summary
            st.header("Summary:")
            st.write(summary)

if __name__ == "__main__":
    main()
