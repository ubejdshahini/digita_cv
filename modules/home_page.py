import streamlit as st


def render_home_page(name: str, description: str, pdf_bytes: bytes):
    st.title(name)
    st.write(description)
    st.download_button(
        label="📄 Download Resume",
        data=pdf_bytes,
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
    st.write("🚧", "**Car Parking System - Arduino | 11 1**")
    st.write("2024")
    st.write(
        """
- ► Designed and implemented a car parking system using Arduino, integrating sensors and microcontrollers for efficient parking management.
- ► Developed a user-friendly interface for real-time monitoring and control of parking spaces.
"""
    )

    # --- Project 2
    st.write("\n")
    st.write("🚧", "**PLC Coding | 11 1**")
    st.write("2023")
    st.write(
        """
- ► Programmed PLCs for industrial automation projects, enhancing operational efficiency and reliability.
- ► Collaborated with cross-functional teams to design and implement automation solutions in manufacturing processes.
"""
    )

    # --- Project 3
    st.write("\n")
    st.write("🚧", "**Carwash Project | 11 1**")
    st.write("2023")
    st.write(
        """
- ► Led the development of an automated car wash system, utilizing sensors and control systems to optimize the washing process.
- ► Implemented a user-friendly interface for customers to select wash options and monitor the status of
"""
    )

    # --- Project 4
    st.write("\n")
    st.write("🚧", "**Robotic Arm Coding | 11 1**")
    st.write("2023")
    st.write(
        """
- ► Programmed robotic arms for precision tasks in manufacturing, improving accuracy and efficiency in production lines.
- ► Collaborated with colleagues to design and implement robotic solutions for complex manufacturing processes.
"""
    )