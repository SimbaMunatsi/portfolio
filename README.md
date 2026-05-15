# SimbaraShe Munatsi - AI Engineer Portfolio

A professional portfolio website showcasing AI engineering expertise, RAG systems, multi-agent AI architectures, and production-grade deployments. Built with Streamlit for rapid prototyping and deployment.

## 🎯 Overview

This portfolio is a fully functional, self-contained Streamlit application that highlights:
- **RAG Systems**: Production-grade Retrieval-Augmented Generation implementations
- **Multi-Agent AI**: LangGraph-based orchestration and agent coordination
- **Full-Stack AI**: FastAPI backends, vector databases, and LLM integration
- **DevOps & Deployment**: Docker, AWS ECS, CI/CD pipelines, and cloud infrastructure

## ✨ Features

- **Interactive Hero Section**: Profile image, professional summary, and key metrics
- **Live Project Showcase**: Two featured projects with demo videos and live site links
  - Bumbiro AI: Constitutional RAG Assistant
  - ResumeLens: Multi-Agent Resume Intelligence
- **Technical Skills**: Comprehensive skill tags for quick reference
- **Professional Experience**: Career timeline and key achievements
- **Certifications**: OCI and ReadyTensor professional certifications
- **Contact Integration**: Direct links to LinkedIn, GitHub, and email
- **Responsive Design**: Dark-themed, modern UI with custom CSS styling
- **Mobile Optimized**: Fully responsive layout for all devices

## 🛠️ Technology Stack

| Category | Technologies |
|----------|--------------|
| **Frontend** | Streamlit, HTML/CSS |
| **Python** | 3.10+ |
| **Data Processing** | Pandas, NumPy |
| **Visualization** | Streamlit native components |
| **Version Control** | Git, GitHub |
| **Deployment** | Streamlit Cloud, Docker |

## 📋 Prerequisites

Before you begin, ensure you have the following installed:
- **Python 3.10 or higher** ([Download](https://www.python.org/downloads/))
- **Git** ([Download](https://git-scm.com/))
- **pip** (comes with Python)
- **Virtual environment** (built into Python 3.3+)

Verify installations:
```bash
python --version
git --version
pip --version
```

## 📦 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/SimbaMunatsi/portfolio.git
cd portfolio
```

### 2. Create a Virtual Environment

**On macOS/Linux:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

**On Windows:**
```bash
python -m venv .venv
.venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Add Project Assets

Ensure the `data/` folder contains:
- `simba.png` - Profile image (200x200 recommended)
- `bumbiro.png` - Bumbiro AI project screenshot
- `resumelens.png` - ResumeLens project screenshot

```
portfolio/
├── ui.py
├── requirements.txt
├── README.md
└── data/
    ├── simba.png
    ├── bumbiro.png
    └── resumelens.png
```

## 🚀 Running the Application

### Local Development

```bash
streamlit run ui.py
```

The application will open in your default browser at `http://localhost:8501`

### Development Mode with Auto-Reload

```bash
streamlit run ui.py --logger.level=debug
```

### Production Deployment

For production deployment with Streamlit Cloud:

```bash
git push
```

Then connect your GitHub repository to [Streamlit Cloud](https://streamlit.io/cloud) and deploy.

## 📁 Project Structure

```
portfolio/
├── ui.py                      # Main Streamlit application
├── requirements.txt           # Python dependencies
├── README.md                  # This file
├── .gitignore                # Git ignore rules
└── data/                      # Media assets
    ├── simba.png
    ├── bumbiro.png
    └── resumelens.png
```

## ⚙️ Configuration

### Streamlit Configuration

Create `~/.streamlit/config.toml` to customize Streamlit settings:

```toml
[theme]
primaryColor = "#0f172a"
backgroundColor = "#111827"
secondaryBackgroundColor = "#1f2937"
textColor = "#d1d5db"
font = "sans serif"

[client]
showErrorDetails = true
```

### Environment Variables (Optional)

If you add features requiring API keys:

```bash
# Create .env file
STREAMLIT_API_KEY=your_key_here

# Load in Python
import os
from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv("STREAMLIT_API_KEY")
```

## 🔧 Customization

### Updating Personal Information

Edit `ui.py` and modify:
- **Hero Section** (lines ~80-95): Name, headline, bio
- **Contact Section** (lines ~109-120): Email, phone, social links
- **Skills** (lines ~180-205): Add/remove technical skills
- **Experience** (lines ~325-350): Update career history
- **Certifications** (lines ~355-365): Add new certifications

### Styling

CSS styles are defined in the `st.markdown()` call at the top of `ui.py`. Modify the `<style>` block to customize:
- Colors, fonts, spacing
- Card styling (`.project-card`, `.metric-card`, `.skill-pill`)
- Responsive breakpoints

### Adding New Projects

Add new project cards after PROJECT 2:

```python
st.markdown(
    """
    <div class='project-card'>
        <h3>🎯 Project Title</h3>
        <p>
            <a href="https://youtube.com/..." target="_blank" style="color: #60a5fa;">🎥 Demo</a>
            <a href="https://example.streamlit.app" target="_blank" style="color: #60a5fa;">🌐 Site</a>
        </p>
        <p>Project description here...</p>
        <ul>
            <li>Achievement 1</li>
            <li>Achievement 2</li>
        </ul>
        <p><b>Tech Stack:</b> Tech1, Tech2, Tech3</p>
    </div>
    """,
    unsafe_allow_html=True
)
```

## 📊 Performance Optimization

### Image Optimization

Compress images before adding to `data/`:
```bash
# Using ImageMagick
convert input.png -quality 85 -resize 800x600 output.png

# Using PIL in Python
from PIL import Image
img = Image.open('image.png')
img.thumbnail((800, 600))
img.save('image_optimized.png', quality=85)
```

### Caching

Add Streamlit caching for expensive operations:

```python
@st.cache_data
def load_data():
    # Your data loading logic
    return data
```

## 🐳 Docker Deployment

### Build Docker Image

```dockerfile
# Dockerfile
FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "ui.py"]
```

Build and run:
```bash
docker build -t portfolio .
docker run -p 8501:8501 portfolio
```

## 🚢 Production Deployment

### Streamlit Cloud (Recommended)

1. Push code to GitHub
2. Go to [Streamlit Cloud](https://streamlit.io/cloud)
3. Deploy repository
4. Share public URL

### AWS ECS/Fargate

```bash
# Create ECR repository
aws ecr create-repository --repository-name portfolio

# Build and push
docker build -t portfolio .
docker tag portfolio:latest <account>.dkr.ecr.<region>.amazonaws.com/portfolio:latest
docker push <account>.dkr.ecr.<region>.amazonaws.com/portfolio:latest
```

### Render

1. Connect GitHub repository
2. Create new Web Service
3. Set Build Command: `pip install -r requirements.txt`
4. Set Start Command: `streamlit run ui.py --server.port=10000 --server.address=0.0.0.0`
5. Deploy

## 🧪 Testing

### Manual Testing Checklist

- [ ] All links navigate correctly
- [ ] Images load without errors
- [ ] Responsive design on mobile/tablet/desktop
- [ ] Contact buttons link to correct destinations
- [ ] Project demo videos play
- [ ] Live site links are accessible
- [ ] Styles render correctly

## 📝 Dependencies

See `requirements.txt` for full list. Key dependencies:
- `streamlit>=1.28.0` - Web framework
- `Pillow>=10.0.0` - Image processing

## 🐛 Troubleshooting

| Issue | Solution |
|-------|----------|
| **Module not found error** | Run `pip install -r requirements.txt` |
| **Images not displaying** | Verify `data/` folder exists with correct image files |
| **Port 8501 already in use** | `streamlit run ui.py --server.port=8502` |
| **Slow performance** | Optimize image sizes, add caching decorators |
| **Git not recognized** | Reinstall Git or add to system PATH |

## 📞 Contact & Support

- **Email**: vsmunatsi@gmail.com
- **LinkedIn**: [Victor Simbarashe Munatsi](https://www.linkedin.com/in/victor-simbarashe-munatsi/)
- **GitHub**: [SimbaMunatsi](https://github.com/SimbaMunatsi)
- **Location**: Harare, Zimbabwe
- **Phone**: +263 775 015 821

## 📄 License

This project is personal portfolio content. Feel free to use as a template for your own portfolio, but respect the original project showcases and achievements.

## 🙏 Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- Deployed on [Streamlit Cloud](https://streamlit.io/cloud)
- Designed with modern UI/UX principles
- Inspired by production-grade AI systems

## 📚 Resources

- [Streamlit Documentation](https://docs.streamlit.io/)
- [Python Virtual Environments](https://docs.python.org/3/tutorial/venv.html)
- [Git Documentation](https://git-scm.com/doc)
- [Markdown Guide](https://www.markdownguide.org/)

---

**Last Updated**: May 2025  
**Maintained By**: Simbarashe Munatsi  
**Status**: ✅ Production Ready
