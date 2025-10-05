import streamlit as st
from datetime import datetime
from pathlib import Path
from PIL import Image  # <-- import PIL

# Page configuration
st.set_page_config(
    page_title="Birthday Greeting",
    page_icon="🎉",
    layout="centered"
)

# Header
st.title("🎂 Happy Birthday! 🎂")

# Fixed Name
name = "Jayanjan Bhattacharya"
st.subheader(f"Hey {name}! 🎉")
st.write("Wishing you a day filled with love, joy, and all the cake you can eat!")

# Local images for collage
image_paths = [
    "photo_2025-10-06_00-03-00.jpg",
    "photo_2025-10-06_00-03-06.jpg",
    "photo_2025-10-06_00-06-49.jpg",
    "photo_2025-10-06_00-03-18.jpg"
]

# Display images in a 2-column grid
cols = st.columns(2)
for idx, img_path in enumerate(image_paths):
    path = Path(img_path)
    col = cols[idx % 2]  # alternate columns
    if path.exists():
        img = Image.open(path)  # <-- open image using PIL
        col.image(img, use_column_width=True)
    else:
        col.write(f"Image not found: {img_path}")

# Fixed Birthday Date
birth_date = datetime(2025, 6, 10)
today = datetime.today()

# Calculate days until birthday
next_birthday = birth_date.replace(year=today.year)
if next_birthday < today:
    next_birthday = next_birthday.replace(year=today.year + 1)
days_left = (next_birthday - today).days

st.write(f"🎈 Only {days_left} day(s) left until the next birthday!")

# Footer
st.markdown("---")
st.write("Gawk Gawk Gawk❤️ ")
