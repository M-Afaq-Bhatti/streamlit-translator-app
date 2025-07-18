import streamlit as st
from transformers import TFAutoModelForSeq2SeqLM, AutoTokenizer
import tensorflow as tf

# Load model and tokenizer
@st.cache_resource
def load_model():
    model = TFAutoModelForSeq2SeqLM.from_pretrained("translation_model")
    tokenizer = AutoTokenizer.from_pretrained("translation_model")
    return model, tokenizer

model, tokenizer = load_model()

# App layout
st.set_page_config(page_title="EN→UR Translator", layout="centered")

st.markdown(
    "<h1 style='text-align: center; color: #4A90E2;'>Neural Translator</h1>",
    unsafe_allow_html=True
)
st.markdown(
    "<h4 style='text-align: center; color: gray;'>Translate English to Urdu using a fine-tuned Transformer model</h4>",
    unsafe_allow_html=True
)
st.markdown("---")

text_input = st.text_area("Enter English text to translate:", height=150)

if st.button("Translate"):
    if text_input.strip():
        input_ids = tokenizer(text_input, return_tensors="tf", padding=True, truncation=True).input_ids
        outputs = model.generate(input_ids)
        translated = tokenizer.decode(outputs[0], skip_special_tokens=True)

        st.markdown("### Urdu Translation:")
        st.success(translated)
    else:
        st.warning("Please enter some text.")

st.markdown("---")
st.markdown("<footer style='text-align: center; color: gray;'>Made with 💙 using Transformers + Streamlit</footer>", unsafe_allow_html=True)
