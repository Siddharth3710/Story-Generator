# story_generator.py
from transformers import pipeline, set_seed
import streamlit as st

# Load model
generator = pipeline("text-generation", model="gpt2")
set_seed(42)

# Streamlit UI
st.title("📝 AI Story Generator")
st.write("Enter a character and setting to generate a story (e.g., 'A robot named Max in a desert').")

# Input prompt
input_text = st.text_input("Enter your story prompt:")

# Generate story
if input_text:
    st.subheader("Generated Stories:")
    outputs = generator(input_text, max_length=80, num_return_sequences=3)
    for i, output in enumerate(outputs):
        st.write(f"{i+1}. {output['generated_text']}")
