import streamlit as st


def render_certifications_page():
    st.title("🎓 Certifications")
    st.write("A collection of professional certifications and courses I have completed.")
    st.write("---")

    with st.expander("✅ AWS Certified Solutions Architect – Associate"):
        st.write("**Issuer:** Amazon Web Services (AWS)")
        st.write("**Date:** March 2024")
        st.write(
            """
            Validates the ability to design and deploy scalable, highly available, and 
            fault-tolerant systems on AWS. Covers core services including EC2, S3, RDS, 
            VPC, and IAM, along with architectural best practices.
            """
        )
        st.write("🔗 [View Certificate](https://aws.amazon.com/certification/)")

    with st.expander("✅ Python for Data Science and Machine Learning Bootcamp"):
        st.write("**Issuer:** Udemy / Jose Portilla")
        st.write("**Date:** November 2023")
        st.write(
            """
            Comprehensive course covering Python fundamentals, NumPy, Pandas, Matplotlib, 
            Seaborn, Scikit-Learn, and introductory deep learning with TensorFlow. 
            Included hands-on projects in data analysis and predictive modeling.
            """
        )
        st.write("🔗 [View Certificate](https://www.udemy.com/)")

    with st.expander("✅ Microsoft Azure Fundamentals (AZ-900)"):
        st.write("**Issuer:** Microsoft")
        st.write("**Date:** August 2023")
        st.write(
            """
            Foundational certification covering core Azure concepts, cloud service types 
            (IaaS, PaaS, SaaS), Azure pricing and SLAs, and an overview of Azure 
            compute, networking, and storage services.
            """
        )
        st.write("🔗 [View Certificate](https://learn.microsoft.com/en-us/certifications/azure-fundamentals/)")

    with st.expander("✅ Introduction to Cybersecurity"):
        st.write("**Issuer:** Cisco Networking Academy")
        st.write("**Date:** May 2023")
        st.write(
            """
            Covered the fundamentals of cybersecurity including threat landscapes, 
            network security, cryptography basics, and best practices for protecting 
            organizational and personal data.
            """
        )
        st.write("🔗 [View Certificate](https://www.netacad.com/)")

    with st.expander("✅ Scrum Fundamentals Certified (SFC)"):
        st.write("**Issuer:** SCRUMstudy")
        st.write("**Date:** January 2023")
        st.write(
            """
            Introduction to the Scrum framework for agile project management. Topics 
            include sprint planning, daily stand-ups, retrospectives, roles 
            (Scrum Master, Product Owner, Development Team), and the Scrum lifecycle.
            """
        )
        st.write("🔗 [View Certificate](https://www.scrumstudy.com/)")