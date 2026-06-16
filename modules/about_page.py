import streamlit as st


def render_about_page(email: str, linkedin_url: str):
    st.title("About Me")
    st.write(
        """
    I am a diligent and ambitious individual with a great passion for Computer Engineering and
Software Programming. I am eager to be challenged in order to grow and further 
improve my computer skills.
    """
    )

    # Show LinkedIn and Email only on the About page
    st.write("📫", email)
    st.write(f"Feel free to connect with me on [LinkedIn]({linkedin_url}).")