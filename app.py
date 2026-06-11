import streamlit as st
#from PIL import Image

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
#profile_pic_file = "assets/profile-pic.png"

with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()

#profile_pic = Image.open(profile_pic_file)

# Sidebar navigation
page = st.sidebar.radio("Navigate", ["Home", "About"])

if page == "Home":
    # --- HERO SECTION ---
    #col1, col2 = st.columns([1, 2], gap="small")
    #with col1:
        #st.image(profile_pic, width=230)

    #with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label="📄 Download Resume",
        data=PDFbyte,
        file_name="CV.pdf",
        mime="application/octet-stream",
    )

    # --- EXPERIENCE & QUALIFICATIONS ---
    st.write("\n")
    st.subheader("Experience & Qualifications")
    st.write(
        """
- ✔️ 5+ years of experience designing and deploying scalable web applications.
- ✔️ Skilled in Java, Spring Boot, JavaScript, and SQL/NoSQL databases.
- ✔️ Experienced in building RESTful APIs and microservice architectures.
- ✔️ Proficient in cloud platforms (AWS, Azure) and CI/CD pipelines.
"""
    )

    # --- SKILLS ---
    st.write("\n")
    st.subheader("Hard Skills")
    st.write(
        """
- 👩‍💻 Programming: Python (FastAPI, Scikit-learn, Pandas), SQL, DBT
- 📊 Data Visualization: PowerBI, Streamlit
- 🗄️ Databases: Snowflake, AWS, PostgreSQL
- 🤖 Machine Learning: Neural networks, classification algorithms
"""
    )

    # --- Projects History ---
    st.write("\n")
    st.subheader("Projects History")
    st.write("---")

    # --- Project 1
    st.write("🚧", "**Car Parking System - Arduino | 11 Marsi**")
    st.write("2024")
    st.write(
        """
- ► Designed and implemented a car parking system using Arduino, integrating sensors and microcontrollers for efficient parking management.
- ► Developed a user-friendly interface for real-time monitoring and control of parking spaces.
"""
    )

    # --- Project 2
    st.write("\n")
    st.write("🚧", "**PLC Coding | 11 Marsi**")
    st.write("2023")
    st.write(
        """
- ► Programmed PLCs for industrial automation projects, enhancing operational efficiency and reliability.
- ► Collaborated with cross-functional teams to design and implement automation solutions in manufacturing processes.
"""
    )

    # --- Project 3
    st.write("\n")
    st.write("🚧", "**Carwash Project | 11 Marsi**")
    st.write("2023")
    st.write(
        """
- ► Led the development of an automated car wash system, utilizing sensors and control systems to optimize the washing process.
- ► Implemented a user-friendly interface for customers to select wash options and monitor the status of
"""
    )

    # --- Project 4
    st.write("\n")
    st.write("🚧", "**Robotic Arm Coding | 11 Marsi**")
    st.write("2023")
    st.write(
        """
- ► Programmed robotic arms for precision tasks in manufacturing, improving accuracy and efficiency in production lines.
- ► Collaborated with colleagues to design and implement robotic solutions for complex manufacturing processes.
"""
    )

   

elif page == "About":
    st.title("About Me")
    st.write("""
    I am a diligent and ambitious individual with a great passion for Computer Engineering and
Software Programming. I am eager to be challenged in order to grow and further 
improve my computer skills.
    """)

    # Show LinkedIn and Email only on the About page
    st.write("📫", EMAIL)
    st.write(f"Feel free to connect with me on [LinkedIn]({LINKEDIN_URL}).")
