# Project Title : Legal Document Summarization

## Overview
<p align="justify">
This project introduces an automated solution for summarizing legal texts, leveraging machine learning techniques. In response to the growing complexity and volume of legal documents, there's a pressing need for efficient information extraction methods to support decision-making processes. Our approach employs natural language processing (NLP) techniques and deep learning architectures, including Transformer models, to develop a robust summarization model. By analyzing diverse legal documents, our system extracts key insights and condenses lengthy texts into concise summaries. Evaluation results confirm the effectiveness of our approach in accurately capturing essential information while maintaining readability. By automating the summarization process, our project contributes to streamlining legal workflows and enhancing productivity for legal professionals, researchers, and businesses. This project represents a significant advancement in the field of legal tech, offering a valuable tool for navigating the complexities of legal documentation. By leveraging innovation, we aim to revolutionize the way legal information is processed and utilized, benefiting legal professionals and the broader community alike.
</p>

## Setup Instructions
1. **Upload Files to Google Colab :** Begin by uploading the `Legal_summarization.ipynb` and `app.py` files to Google Colab for seamless execution and collaboration.
2. **Generate Hugging Face Token :** Log in to huggingface.com and navigate to Your Profile -> Access Tokens -> New Token. Generate a new token and name it for identification purposes. Copy the token value.
3. **Set up Colab Secrets :** In Google Colab, navigate to the secrets tab and add a new secret named 'HF_TOKEN'. Paste the copied token value into the corresponding field.
4. **Run the Project :** Execute each cell of the notebook sequentially to set up the environment, load necessary libraries, and process the legal documents.
5. **Access the Web Application :** Upon completion, the notebook will generate a URL for the web application. Follow the instructions to access the Streamlit app. You will be prompted to enter the IPv4 address provided by running the command `!wget -q -0 - ipv4.icanhazip.com` in code cell. Paste this address into the security screen to gain access to the summarization app.

## Files and Resources
1. **`fine_tuned_model` :** This folder is generated from the training and storing the T5 model which is trained on the dataset and being used to generate summary in the web application.
2. **`app.py` :** The `app.py` is the file that has the code of the streamlit app that handles the queries and input pdfs for which model will be used to summarize it late on.
3. **`Legal_summarization.ipynb` :** The `Legal_summarization.ipynb` file is the main file that contains all the dataset loading, preprocessing and model generation, training and model fine-tuning functions.

## Features
- **Efficient Summarization :** Utilizes state-of-the-art NLP T5 model to generate accurate and concise summaries of legal documents.
- **User-Friendly Interface :** The Streamlit web application provides an intuitive interface for users to interact with the summarization tool.
- **Secure Access :** Ensures security by requiring users to authenticate their access through the provided IPv4 address.
