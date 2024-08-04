import streamlit as st
from PIL import Image
import time

# Function to add background color
def add_bg_from_url():
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("https://wallpapercave.com/wp/wp3527212.jpg");
            background-attachment: fixed;
            background-size: cover;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Set the page title and icon
st.set_page_config(page_title="Happy Friendship Day", page_icon="👬", layout="wide")

# Add background color
add_bg_from_url()

# Title and subtitle
st.title("Happy Friendship Day! 🎉")
st.subheader("To my dearest friend")

# Adding a heart image

# Adding a personal message
st.write("""
    Dear Friend,

    On this special day, I want to let you know how much you mean to me. 
    Our friendship is one of the most cherished parts of my life. 
    Thank you for always being there, for the laughs, the support, and the countless memories.
    
    Cheers to many more years of friendship and adventures together!

""")

# Adding an animation
st.balloons()

# Animated progress bar for a fun touch
with st.spinner("Preparing something special..."):
    time.sleep(2)

st.success("Here's a virtual hug for you! 🤗")

# Displaying a friendship quote
st.markdown(
    """
    > "A friend is one that knows you as you are, understands where you have been, 
    > accepts what you have become, and still, gently allows you to grow."
    > 
    > – William Shakespeare
    """
)

# Adding a button for an interactive element
if st.button('Receive Virtual Hug'):
    st.write("🤗 Sending a virtual hug your way! 🤗")

# Adding some images related to friendship

# Ending note
st.write("""
    May our bond continue to grow stronger with each passing day. 
    Happy Friendship Day once again!

""")
