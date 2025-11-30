# Setup Guide - Roadmap Agent

## Quick Start (5 minutes)

### Step 1: Get Your API Key

1. Go to [Google AI Studio](https://aistudio.google.com/app/apikey)
2. Sign in with your Google account
3. Click "Create API Key"
4. Copy the API key

### Step 2: Configure the API Key

**Option A: Using .env file (Recommended)**

1. Copy the example file:

   ```bash
   cp .env.example .env
   ```

2. Open `.env` and add your API key:

   ```bash
   GOOGLE_GENAI_USE_VERTEXAI=FALSE
   GOOGLE_API_KEY=AIzaSyAbc123YourActualAPIKeyHere
   ```

3. In `config.py`, uncomment these lines (around line 20-22):
   ```python
   from dotenv import load_dotenv
   load_dotenv()
   os.environ["GOOGLE_GENAI_USE_VERTEXAI"] = "FALSE"
   os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")
   ```

**Option B: Direct in code (Quick test only)**

In `config.py`, uncomment and edit these lines (around line 28-29):

```python
os.environ["GOOGLE_GENAI_USE_VERTEXAI"] = "FALSE"
os.environ["GOOGLE_API_KEY"] = "AIzaSyAbc123YourActualAPIKeyHere"
```

⚠️ **Never commit your actual API key to version control!**

### Step 3: Install Dependencies

```bash
# Create virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install required packages
pip install -r requirements.txt
```

### Step 4: Run the Agent

**Option A: Web Interface**

```bash
adk web
```

Then open your browser to the URL shown (usually http://localhost:8000)

**Option B: Test Script**

```bash
python -m tests.test_agent
```

---

## Project Structure

```
roadmap_agent/
├── .env                    # Your API key (create this, never commit)
├── .env.example           # Template for .env file
├── requirements.txt       # Python dependencies
├── README.md             # Project overview
├── SETUP.md              # This file
├── roadmap_agent/
│   ├── __init__.py
│   ├── agent.py          # Main orchestrator
│   ├── config.py         # 🔑 ADD API KEY HERE
│   ├── agent_utils.py
│   ├── tools.py
│   ├── validation_checkers.py
│   └── sub_agents/
│       ├── __init__.py
│       ├── domain_researcher.py
│       ├── roadmap_planner.py
│       ├── resource_curator.py
│       ├── practice_advisor.py
│       └── roadmap_editor.py
└── tests/
    └── test_agent.py
```

---

## Troubleshooting

### Error: "API key not configured"

- Make sure you uncommented the API key lines in `config.py`
- Check that your `.env` file exists and has the correct format
- Verify your API key is correct (no extra spaces)

### Error: "Module not found"

- Run `pip install -r requirements.txt`
- Make sure your virtual environment is activated

### Error: "google.auth.exceptions.DefaultCredentialsError"

- This means it's trying to use Vertex AI (Google Cloud)
- Make sure you set `GOOGLE_GENAI_USE_VERTEXAI=FALSE`
- Use Option A or B above to configure AI Studio instead

### API Key Best Practices

- ✅ Use `.env` file (add `.env` to `.gitignore`)
- ✅ Use environment variables
- ❌ Don't hardcode keys in your code
- ❌ Don't commit keys to GitHub
- ❌ Don't share keys publicly

---

## Usage Example

Once running, interact like this:

```
You: I want to prepare for a Data Analyst job

Agent: Great! To create the best roadmap for you, I need some information:
       1. What's your current experience level?
       2. What's your preferred learning style?
       3. How much time can you dedicate daily?

You: I'm a complete beginner. I prefer video tutorials and hands-on practice.
     I can dedicate 3 hours per day.

Agent: [Generates personalized 4-week roadmap...]
```

---

## Need Help?

- **Google ADK Documentation**: https://github.com/google/adk-docs
- **API Studio Help**: https://ai.google.dev/docs
- **Issues**: Create an issue in your repository

Happy learning! 🚀
