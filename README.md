## LangChain GitHub Recommender

A Python project using LangChain to recommend GitHub repositories to the user based on their coding interests.

## Setup

Get your api keys from any of the following services:
- Groq
- HuggingFace
- OpenAI

Create a .env file in the root directory of the project and add the following variables:

```bash
GROQ_API_KEY=your_groq_api_key
HUGGINGFACEHUB_ACCESS_TOKEN=your_huggingface_access_token
OPENAI_API_KEY=your_openai_api_key
```

Install the required packages:
```bash
pip install -r requirements.txt
```

Run the agent:
```bash
streamlit run agent.py
```




