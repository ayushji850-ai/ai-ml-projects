# GenAI Prompt Lab — OpenAI

This standalone project follows the uploaded lab workflow:
Python -> VS Code -> project -> venv -> provider SDK -> API key -> .env -> API call -> interactive prompting -> prompt-engineering experiments -> AI Study Assistant.

## Windows setup

```powershell
python --version
pip --version
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

If PowerShell blocks activation:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Copy `.env.example` to `.env`.

Add your own OpenAI API key and an actual model ID currently available to your API project.

Then:
```powershell
python app.py
```

Choose a prompt method:
- Zero-shot
- One-shot
- Few-shot
- Task Decomposition
- Chain-of-Thought-style
- Self-Consistency
- Tree-of-Thoughts-style
- ReAct-style

API keys are never included in this ZIP. Do not upload `.env` to GitHub.
