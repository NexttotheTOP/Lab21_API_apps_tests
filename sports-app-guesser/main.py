import os 

import ai21
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

api_key_file = r"C:\Users\woutv\Documents\lablab_AI\sports-app-guesser\API_KEY"

# Check if the file exists
if os.path.exists(api_key_file):
    # Read the API key from the file
    with open(api_key_file, "r") as file:
        API_KEY = file.read().strip()
else:
    # Raise an error if the file is not found
    raise FileNotFoundError("API key file not found")

ai21.api_key = API_KEY

## function that takes description as input and returns name of the sport

# prompt for the model
PROMPT = "Based on the given description, name the sport.\nDescription: {description}\n Sport name: "

# Initialization of output variable
if "output" not in st.session_state:
    st.session_state["output"] = "Output:"

def guess_sport(inp):
    if not len(inp):
        return None
    
    # overwrite prompt with the description
    prompt = PROMPT.format(description=inp)

    response = ai21.Completion.execute(
        model="j2-grande-instruct",
        prompt=prompt,
        temperature=0.5,
        minTokens=1,
        maxTokens=15,
        numResults=1,
    )

    # Return name of the sport 
    st.session_state["output"] = response.completions[0].data.text

    # Balloon celebration
    st.balloons()


st.title("The Sports Guesser")

st.write(
    "This is a simple **Streamlit** app that generates Sport Name based on given description"
)

inp = st.text_area("Enter your description here", height=100)

st.button("Guess", on_click=guess_sport(inp))
st.write(f"Answer: {st.session_state.output}")
