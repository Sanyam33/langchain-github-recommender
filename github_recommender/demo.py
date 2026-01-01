import streamlit as st
from agent import agent

# -------------------------------
# Page Config
# -------------------------------
st.set_page_config(
    page_title="Git Grab",
    page_icon="⭐",
    layout="wide"
)

# -------------------------------
# Custom CSS (Modern + Professional)
# -------------------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', 'Geist', system-ui, -apple-system, BlinkMacSystemFont, sans-serif;
}

.main {
    background: linear-gradient(180deg, #0f172a 0%, #020617 60%);
    color: #e5e7eb;
}

h1, h2, h3 {
    font-weight: 600;
}

.card {
    background: #020617;
    border: 1px solid #1e293b;
    border-radius: 14px;
    padding: 1.5rem;
    margin-bottom: 1.5rem;
}

.subtle {
    color: #94a3b8;
    font-size: 0.9rem;
}

.result-box {
    background: #020617;
    border-left: 4px solid #38bdf8;
    padding: 1.25rem;
    border-radius: 10px;
    margin-top: 1rem;
}

.sidebar-title {
    font-size: 1.1rem;
    font-weight: 600;
    margin-bottom: 0.75rem;
}
</style>
""", unsafe_allow_html=True)

# -------------------------------
# Sidebar (Filters)
# -------------------------------
with st.sidebar:
    st.markdown("<div class='sidebar-title'>🔍 Filters</div>", unsafe_allow_html=True)

    issue_type = st.selectbox(
        "Search Type",
        ["Repositories", "Issues"],
        index=1
    )

    labels = st.multiselect(
        "Issue Labels",
        ["good-first-issue", "help wanted", "bug", "enhancement"]
    )

    sort_by = st.selectbox(
        "Sort By",
        ["created", "updated", "comments"]
    )

    per_page = st.slider(
        "Results per page",
        min_value=5,
        max_value=50,
        value=10,
        step=5
    )

    st.markdown("<div class='subtle'>Filters affect how GitHub data is fetched.</div>", unsafe_allow_html=True)

# -------------------------------
# Main Header
# -------------------------------
st.markdown("""
<div class="card">
    <h1>Git Grab</h1>
    <p class="subtle">
        Discover trending open-source projects & issues tailored to your GitHub profile.
    </p>
</div>
""", unsafe_allow_html=True)

# -------------------------------
# Input Section
# -------------------------------
st.markdown("<div class='card'>", unsafe_allow_html=True)

col1, col2 = st.columns([3, 1])

with col1:
    username = st.text_input(
        "GitHub Username",
        placeholder="e.g. torvalds, gaearon, your-username"
    )

with col2:
    get_projects = st.button(
        "🚀 Find",
        type="primary",
        use_container_width=True
    )

st.markdown("</div>", unsafe_allow_html=True)

# -------------------------------
# Results Section
# -------------------------------
if username and get_projects:
    payload = {
        "username": username,
        "type": issue_type.lower(),
        "labels": labels,
        "sort": sort_by,
        "per_page": per_page
    }

    with st.spinner("Analyzing GitHub activity & generating insights..."):
        response = agent.invoke({
            "messages": [
                {
                    "role": "user",
                    "content": str(payload)
                }
            ]
        })

    st.markdown("<div class='result-box'>", unsafe_allow_html=True)
    st.markdown("### 🤖 AI Recommendations")
    st.write(response["messages"][-1].content)
    st.markdown("</div>", unsafe_allow_html=True)

# -------------------------------
# Footer
# -------------------------------
st.markdown("""
<br>
<p class="subtle" style="text-align:center;">
Built with ❤️ using GitHub Search API & LLMs
</p>
""", unsafe_allow_html=True)
