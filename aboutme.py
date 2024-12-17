import streamlit as st

# Page Configuration
st.set_page_config(page_title="Steve Laurenz Villas - Portfolio", page_icon="🧑‍💻", layout="wide")

# Load Profile Picture

# Custom CSS Styling
st.markdown("""
    <style>
        /* Main background gradient */
        .main {
            background: linear-gradient(135deg, #1F1F3B, #292F4D);
            color: #FFFFFF;
        }

        /* General styles */
        html, body, [class*="st"] {
            font-family: 'Poppins', sans-serif;
        }

        /* Header and Title */
        .header {
            text-align: left;
            font-size: 50px;
            font-weight: bold;
            color: #00E6FF;
            margin-bottom: 20px;
        }

        .subheader {
            font-size: 22px;
            font-weight: bold;
            color: #00D9FF;
            margin: 30px 0 10px;
        }

        /* Project Cards */
        .project-card {
            background-color: #2C2C3C;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.5);
            transition: all 0.3s ease-in-out;
            margin-bottom: 20px;
        }

        .project-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 8px 20px rgba(0, 0, 0, 0.7);
        }

        /* Footer */
        .footer {
            text-align: center;
            font-size: 16px;
            color: #C0C0C0;
            margin-top: 50px;
        }
    </style>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap" rel="stylesheet">
""", unsafe_allow_html=True)

# Main Content
st.markdown('<div class="header">Welcome to My Portfolio</div>', unsafe_allow_html=True)

# Layout for Left Content and Rightmost Image
col1, col2 = st.columns([3, 1])

with col1:
    st.markdown("### 👋 About Me")
    st.write("""
    I am a BSIT student with a passion for **technology** and **problem-solving**. My interests lie in **cybersecurity**, 
    **system administration**, **frontend development**, and **technical support**. I aim to contribute to impactful projects 
    and continue to develop my expertise in the IT field.
    """)
    st.write("📍 **Cogon West, Carmen, Cebu, Philippines**")
    st.write("📧 [villasstevelaurenz@gmail.com](mailto:villasstevelaurenz@gmail.com) | 📞 **0945 667 2503**")
    st.write("🔗 [LinkedIn Profile](https://www.linkedin.com/in/steve-laurenz-villas-a02729340)")


st.markdown('<hr>', unsafe_allow_html=True)

# Skills Section
st.markdown('<div class="subheader">🛠️ Technical Skills</div>', unsafe_allow_html=True)
st.write("""
- **System Administration**: Windows Server (2016/2012), GPO setup, user management.  
- **Cybersecurity**: Kali Linux, Metasploitable, OWASP Juice Shop, Multillidae.  
- **Frontend Development**: HTML, CSS, JavaScript, React.js, Responsive Web Design, UI/UX.
""")

st.markdown('<hr>', unsafe_allow_html=True)

# Projects Section
st.markdown('<div class="subheader">🚀 Projects</div>', unsafe_allow_html=True)
projects = [
    {"name": "ProDigi", "description": "A journal and planner app integrated with a grammar-checking API.", "skills": "HTML, CSS, JavaScript, UI/UX"},
    {"name": "ReflectDaily", "description": "A reflection and habit-tracking tool for personal growth.", "skills": "React.js, HTML, CSS, UI/UX"},
    {"name": "SocialSphere", "description": "Content management site integrated with Facebook API.", "skills": "HTML, CSS, JavaScript, UI/UX"},
]

for project in projects:
    st.markdown(f"""
        <div class="project-card">
            <h4 style="color: #00E6FF; margin-bottom: 5px;">{project['name']}</h4>
            <p>{project['description']}</p>
            <em>Skills Used:</em> {project['skills']}
        </div>
    """, unsafe_allow_html=True)

st.markdown('<hr>', unsafe_allow_html=True)

# Certifications Section
st.markdown('<div class="subheader">📜 Certifications</div>', unsafe_allow_html=True)
certifications = [
    "Kaggle – Data Visualization Online Course",
    "Alison – Data Analytics Online Course",
    "Huawei Online – HCIP Storage Expert Course",
    "Cebu ICT Student Congress 2024",
    "CISCO – Introduction to Cybersecurity"
]
for cert in certifications:
    st.write(f"- {cert}")

# Footer
st.markdown('<div class="footer">Thank you for visiting my portfolio! 🚀</div>', unsafe_allow_html=True)
st.write("🔗 [LinkedIn Profile](https://www.linkedin.com/in/steve-laurenz-villas-a02729340)")
