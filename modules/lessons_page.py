"""
Renders the 'Lessons' page: a list of lecture summaries.
Designed to scale cleanly as more lectures are added to lectures_data.py.
"""

import streamlit as st
from data.lectures_data import LECTURES, get_lecture_by_number, get_all_lecture_numbers_sorted


def render_lecture_card(lecture: dict):
    """Render a single lecture's full summary inside an expander."""
    header = f"📘 Lecture {lecture['number']} — {lecture['title']}"
    with st.expander(header, expanded=False):
        if lecture.get("topics"):
            tags = " ".join(f"`{topic}`" for topic in lecture["topics"])
            st.markdown(tags)
            st.write("")

        for section in lecture["sections"]:
            st.markdown(f"**{section['heading']}**")
            st.write(section["content"])
            st.write("")


def render_lessons_page():
    st.title("📚 Lessons")
    st.caption("Summaries of lecture content, organized by lecture number.")
    st.write("---")

    if not LECTURES:
        st.info("No lecture summaries have been added yet.")
        return

    lecture_numbers = get_all_lecture_numbers_sorted(descending=True)

    # Sidebar-style filter within the page for quick jumping between lectures
    selected = st.selectbox(
        "Jump to a lecture",
        options=["All"] + [f"Lecture {n}" for n in lecture_numbers],
    )

    st.write("")

    if selected == "All":
        for number in lecture_numbers:
            lecture = get_lecture_by_number(number)
            render_lecture_card(lecture)
    else:
        number = int(selected.split(" ")[1])
        lecture = get_lecture_by_number(number)
        render_lecture_card(lecture)