import streamlit as st

from modules.home_page import render_home_page
from modules.about_page import render_about_page
from modules.certifications_page import render_certifications_page
from modules.lessons_page import render_lessons_page

# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Ubejd Shahini"
PAGE_ICON = ":wave:"
NAME = "Ubejd Shahini"
DESCRIPTION = """
Student in University of Prishtina.
"""

EMAIL = "shahiniubejd@gmail.com"
LINKEDIN_URL = "https://www.linkedin.com/in/ubejdshahini/"

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# Directly reference files in the assets folder (ensure it exists)
resume_file = "assets/my_cv.pdf"

with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()

# Sidebar navigation
page = st.sidebar.radio("Navigate", ["Home", "Lessons", "Certifications", "About"])

if page == "Home":
    render_home_page(NAME, DESCRIPTION, PDFbyte)

elif page == "Lessons":
    render_lessons_page()

elif page == "Certifications":
    render_certifications_page()

elif page == "About":
    render_about_page(EMAIL, LINKEDIN_URL)