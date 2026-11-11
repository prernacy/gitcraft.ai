import streamlit as st
import datetime

# Page Configuration
st.set_page_config(
    page_title="GitCraft AI - README & Architecture Studio",
    layout="wide"
)

# App Header
st.title("GitCraft AI: Professional README & Architecture Generator")
st.markdown("Build stunning, recruiter-ready GitHub repository documentation in seconds using 100% pure Python.")

# Sidebar Configuration for User Input
st.sidebar.header("Project Configuration")
project_name = st.sidebar.text_input("Project Name", "SmartBudgetTracker")
project_type = st.sidebar.selectbox("Project Category", ["Web Application", "CLI Tool / TUI", "Data Science / ML", "REST API Backend"])
primary_language = st.sidebar.selectbox("Primary Language", ["Python", "JavaScript", "TypeScript", "C++", "Salesforce Apex"])
features_input = st.sidebar.text_area("Key Features (one per line)", "User Authentication\nReal-time Expense Analytics\nSQLite Database Integration")

# Generate Button Action
if st.sidebar.button("Generate Documentation"):
    if not project_name.strip():
        st.warning("Please enter a valid project name!")
    else:
        st.success("Documentation generated successfully!")
        
        # Cleanly format features before inserting into markdown
        feature_lines = [f"- {f.strip()}" for f in features_input.split("\n") if f.strip()]
        formatted_features = "\n".join(feature_lines)
        
        repo_slug = project_name.lower().replace(" ", "-")
        current_date = datetime.date.today().strftime('%B %d, %Y')
        
        # Unified Markdown template (free of inner backticks to prevent Pylance errors)
        readme_content = f"""# {project_name}

A high-performance {project_type.lower()} built with *{primary_language}*. Designed for scalability, clean architecture, and developer efficiency.

---

## Key Features
{formatted_features}

---

## Tech Stack
- Core Language: {primary_language}
- Architecture: Modular, Clean Code Pattern
- UI Framework: Streamlit / Python Backend

---

## Installation & Setup

1. Clone the repository:
   git clone [https://github.com/your-username/](https://github.com/your-username/){repo_slug}.git
   cd {repo_slug}

2. Create a virtual environment:
   python -m venv venv
   source venv/bin/activate

3. Install dependencies:
   pip install -r requirements.txt

4. Run the application:
   streamlit run app.py

---
Generated automatically with GitCraft AI on {current_date}
"""
        
        # Display Results in Tabs
        tabs = st.tabs(["Live README Preview", "Architecture Blueprint", "Raw Markdown Code"])
        
        with tabs[0]:
            st.markdown("---")
            st.markdown(readme_content)
            
        with tabs[1]:
            st.markdown("### System Architecture Flow")
            st.code(f"""
[ User Interface ] 
       │
       ▼
[ {project_name} Core Engine ({primary_language}) ]
       │
       ├──► [ Business Logic & Validators ]
       └──► [ Local Database / Storage ]
            """, language="text")
            
        with tabs[2]:
            st.text_area("Copy Raw Markdown for your GitHub README.md", readme_content, height=350)
else:
    st.info("Fill out your project details in the sidebar and click Generate Documentation to get started!")