import streamlit as st

st.set_page_config(
    page_title="SimbaraShe Munatsi | AI Engineer",
    page_icon="🤖",
    layout="wide"
)

# ----------------------
# CUSTOM STYLING
# ----------------------
st.markdown(
    """
    <style>
    .main {
        padding-top: 1rem;
    }

    .hero {
        padding: 2rem;
        border-radius: 18px;
        background: linear-gradient(135deg, #0f172a, #111827);
        color: white;
        margin-bottom: 2rem;
    }

    .hero h1 {
        font-size: 3rem;
        margin-bottom: 0.5rem;
    }

    .hero p {
        font-size: 1.1rem;
        color: #d1d5db;
    }

    .metric-card {
        background: #111827;
        padding: 1.2rem;
        border-radius: 16px;
        text-align: center;
        color: white;
        border: 1px solid #1f2937;
    }

    .section-title {
        font-size: 2rem;
        font-weight: 700;
        margin-top: 2rem;
        margin-bottom: 1rem;
    }

    .project-card {
        padding: 1.5rem;
        border-radius: 18px;
        background: #111827;
        color: white;
        border: 1px solid #1f2937;
        margin-bottom: 1rem;
    }

    .project-card h3 {
        margin-bottom: 0.5rem;
    }

    .skill-pill {
        display: inline-block;
        padding: 0.4rem 0.8rem;
        margin: 0.3rem;
        border-radius: 999px;
        background: #1e293b;
        color: white;
        font-size: 0.9rem;
    }

    .footer {
        text-align: center;
        padding: 2rem;
        color: #9ca3af;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ----------------------
# HERO SECTION
# ----------------------
col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    st.image("./data/simba.png", width=300)

st.markdown(
    """
    <div class='hero'> 
        <h1>SimbaraShe Munatsi</h1>
        <h3>AI Engineer | RAG & Multi-Agent Systems</h3>
        <p>
            I am an AI Engineer specializing in production <b>Retrieval-Augmented Generation (RAG)</b> and <b>multi-agent AI systems</b> using FastAPI, LangGraph, Language Models, and vector databases. My passion lies in building deployable AI products that reduce manual work, improve AI reliability, and optimize LLM performance. I focus on modular architectures with built-in observability, authentication, and tracing to deliver high-quality, production-ready AI solutions.    
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

# ----------------------
# CONTACT
# ----------------------
st.markdown("<a name='contact'></a>", unsafe_allow_html=True)
st.markdown("## Contact")

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.info("📍 Harare, Zimbabwe")

with col2:
    st.info("📞 +263 775 015 821")

with col3:
    st.info("vsmunatsi@gmail.com")

with col4:
    st.link_button("💼 LinkedIn", "https://www.linkedin.com/in/victor-simbarashe-munatsi/")

with col5:
    st.link_button("💻 GitHub", "https://github.com/SimbaMunatsi/SimbaMunatsi")

# ----------------------
# METRICS
# ----------------------
st.markdown("## Impact Highlights")

m1, m2, m3, m4 = st.columns(4)

with m1:
    st.markdown(
        """
        <div class='metric-card'>
            <h2>70–90%</h2>
            <p>Manual Work Reduction</p>
        </div>
        """,
        unsafe_allow_html=True
    )

with m2:
    st.markdown(
        """
        <div class='metric-card'>
            <h2>60%</h2>
            <p>LLM Cost Reduction</p>
        </div>
        """,
        unsafe_allow_html=True
    )

with m3:
    st.markdown(
        """
        <div class='metric-card'>
            <h2>45%</h2>
            <p>Latency Improvement</p>
        </div>
        """,
        unsafe_allow_html=True
    )

with m4:
    st.markdown(
        """
        <div class='metric-card'>
            <h2>10k+</h2>
            <p>Pages Indexed</p>
        </div>
        """,
        unsafe_allow_html=True
    )

# ----------------------
# ABOUT SECTION
# ----------------------

# ----------------------
# SKILLS
# ----------------------
st.markdown("## Technical Skills")

skills = [
    "Python",
    "FastAPI",
    "LangGraph",
    "LangChain",
    "RAG",
    "Agentic AI",
    "PostgreSQL",
    "PGVector",
    "ChromaDB",
    "Docker",
    "AWS ECS",
    "Render",
    "JWT Auth",
    "OpenAI APIs",
    "RAGAS",
    "DeepEval",
    "LangSmith",
    "CI/CD",
    "SQLAlchemy",
    "ChromaDB",
    "REST APIs",
    "GitHub Actions",
    "LoRA Fine-Tuning",
]

skill_html = ""
for skill in skills:
    skill_html += f"<span class='skill-pill'>{skill}</span>"

st.markdown(skill_html, unsafe_allow_html=True)

# ----------------------
# PROJECTS
# ----------------------
st.markdown("## Featured Projects")

img_col1, img_col2 = st.columns([1, 1])
with img_col1:
    st.markdown("<div style='display:flex; justify-content:center;'>", unsafe_allow_html=True)
    st.image("./data/bumbiro.png", width=350)
    st.markdown("</div>", unsafe_allow_html=True)
with img_col2:
    st.markdown("<div style='display:flex; justify-content:center;'>", unsafe_allow_html=True)
    st.image("./data/resumelens.png", width=350)
    st.markdown("</div>", unsafe_allow_html=True)

# PROJECT 1
st.markdown(
    """
    <div class='project-card'>
        <h3>⚖️ Bumbiro AI — Constitutional RAG Assistant</h3>
        <p>
            <a href="https://www.youtube.com/watch?v=AAN0nnhqaPk" target="_blank" style="color: #60a5fa; text-decoration: none; margin-right: 1rem;">🎥 Demo Video</a>
            <a href="https://bumbiro-ai.streamlit.app" target="_blank" style="color: #60a5fa; text-decoration: none;">🌐 Live MVP</a>
        </p>
        <p>
            Production RAG system built over 3k+ pages of Zimbabwean constitutional and legal documents.
            Uses hybrid vector retrieval, citation grounding, and FastAPI backend services.
        </p>

        <ul>
            <li>Reduced legal research time from hours to minutes, 8hrs->20mins</li>
            <li>Implemented hybrid vector + BM25 retrieval</li>
            <li>Dockerized backend with production monitoring</li>
            <li>Integrated LangSmith tracing and evaluation pipelines</li>
            <li>Deployed on AWS ECS Fargate with CI/CD pipelines</li>
        </ul>

        <p><b>Tech Stack:</b> FastAPI, LangChain, PGVector, Docker, OpenAI, LangSmith</p>
    </div>
    """,
    unsafe_allow_html=True
)

# PROJECT 2
st.markdown(
    """
    <div class='project-card'>
        <h3>📄 ResumeLens — Multi-Agent Resume Intelligence</h3>
        <p>
            <a href="https://www.youtube.com/watch?v=2WHGGhjFbhw&t=7s" target="_blank" style="color: #60a5fa; text-decoration: none; margin-right: 1rem;">🎥 Demo Video</a>
            <a href="https://resumelens-zim.streamlit.app" target="_blank" style="color: #60a5fa; text-decoration: none;">🌐 Live MVP</a>
        </p>
        <p>
            Multi-agent AI platform for ATS optimization, resume analysis, and recruiter automation.
            Built using LangGraph orchestration and FastAPI backend services.
        </p>

        <ul>
            <li>Automated recruiter screening workflows</li>
            <li>Improved ATS alignment through AI rewriting pipelines</li>
            <li>Processed 200+ resumes through deployed workflows</li>
            <li>Implemented authentication and multi-user support</li>
            <li>Deployed on Render + Supabase with continuous deployment</li>
        </ul>

        <p><b>Tech Stack:</b> FastAPI, LangGraph, PostgreSQL, Streamlit, Render</p>
    </div>
    """,
    unsafe_allow_html=True
)

# ----------------------
# EXPERIENCE
# ----------------------
st.markdown("## Professional Experience")

st.markdown(
    """
    ### Freelance AI Developer | Remote
    **Jan 2025 – Present**

    - Built and deployed AI systems using FastAPI, LangGraph, PostgreSQL, and vector search
    - Reduced LLM costs 60% and latency 45% through retrieval optimization
    - Implemented evaluation pipelines using RAGAS, DeepEval, and LangSmith
    - Deployed Dockerized AI applications on AWS ECS Fargate and Render
    """
)

st.markdown(
    """
    ### PEK 12 — Team Lead, Infrastructure & Installations
    **Mar 2019 – Jun 2024**

    - Led deployment of 40+ telecom base stations across three provinces
    - Maintained 98% uptime SLA across operational sites
    - Reduced network downtime 35% using KPI dashboards
    """
)

# ----------------------
# CERTIFICATIONS
# ----------------------
st.markdown("## Certifications")

cert_col1, cert_col2 = st.columns(2)

with cert_col1:
    st.success("OCI Generative AI Professional")
    st.success("OCI AI Vector Search Professional")

with cert_col2:
    st.success("ReadyTensor RAG Systems Expert")
    st.success("ReadyTensor Agentic AI Builder")

# ----------------------
# CALL TO ACTION
# ----------------------
st.markdown("## Let's Build AI Systems")

st.write(
    """
    Open to:
    - AI Engineering Roles
    - Freelance AI Projects
    - RAG System Development
    - Multi-Agent AI Workflows
    - Backend AI Engineering
    - AI Product Development
    """
)

st.markdown(
    """
    <a href="#contact" style="text-decoration: none;">
        <button style="padding: 0.5rem 1rem; background: #0f172a; color: white; border: 1px solid #1f2937; border-radius: 8px; cursor: pointer; font-size: 1rem;">
            Contact Me
        </button>
    </a>
    """,
    unsafe_allow_html=True
)

# ----------------------
# FOOTER
# ----------------------
st.markdown(
    """
    <div class='footer'>
        Built with Streamlit • Designed and Developed by Simbarashe Munatsi
    </div>
    """,
    unsafe_allow_html=True
)
