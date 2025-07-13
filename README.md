# LinkedIn Post Generator 🧠✍️

Welcome to the **LinkedIn Post Generator**, a multi-agent AI project powered by [CrewAI](https://crewai.com).

---

## ⚙️ Installation

**Requirements:** Python `>=3.10` and `<=3.13`

### 1. Install [UV](https://docs.astral.sh/uv/) (if not already)

```bash
# For macOS and Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# For Windows
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

# Using pip
pip install uv
```

### 3. Clone the repository and get inside of it.
```bash
git clone https://github.com/Nischal2015/agentic-ai-boilerplate
cd agentic-ai-boilerplate
```

### 3. Lock and install dependencies

#### Using `uv` (recommended)
```bash
# Using uv (recommended)
uv lock
uv sync
```

#### Using `pip` (if uv is not working)
```bash
# Create virtual environment
# For Linux/MacOS
python3 -m venv .venv

# For Windows
python -m venv .venv

# Activate virtual environment
# For Linux/MacOS
source ./venv/bin/activate

# For Windows
.\venv\Scripts\activate

# Install the packages
pip install --upgrade pip setuptools wheel
pip install -r requirements.txt
```

---

## 🔐 Environment Variables

Create a `.env` file in the root with:

```env
OPENAI_API_KEY=your_openai_key
SERPER_API_KEY=your_serper_key
```

---

You can create your Serper account right [here](https://serper.dev/signup) to get the `SERPER_API_KEY`.

> ℹ️ **Info**
>
> We will provide you with the `OPENAI_API_KEY`.

You can modify inputs or logic in:
- `linkedin_post_inputs` for test data
- Agent/task configurations in `main.py`
- Create your own tools by subclassing `BaseTool` (see `MyCustomTool`)

---

## Running the project
```bash
# Make sure virtual environment is activated
# For Linux/MacOS
python3 main.py

# For Windows
python main.py
```

## 🙋‍♀️ Need Help?

- [CrewAI Documentation](https://docs.crewai.com)
- [GitHub Repo](https://github.com/joaomdmoura/crewai)
- [Chat with the Docs](https://chatg.pt/DWjSBZn)

---

Give your LinkedIn posts an AI-powered upgrade.
