# Streamlit Translator App

This is a lightweight **language translation web app** built with **Streamlit** and powered by **Hugging Face Transformers**. It translates English text to Urdu in real time using a pre-trained NLP model.

---

## Features

- English-to-Urdu translation  
- Real-time predictions using a trained model  
- Clean and modern UI using Streamlit  
- Powered by Hugging Face Transformers

---

## Folder Structure

```
streamlit-translator-app/
│
├─ app.py                 # Main Streamlit app
├─ requirements.txt       # Python dependencies
├─ model/                 # Folder containing the pre-trained model files
│   ├─ assets/
│   └─ saved_model/
└─ README.md              # Project documentation
```

---

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/M-Afaq-Bhatti/streamlit-translator-app.git
   cd streamlit-translator-app
   ```

2. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```
