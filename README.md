📘 Project Description

CredHunt is a lightweight credential exposure scanner designed to detect hardcoded secrets such as API keys, passwords, private keys, and tokens within project files.
It’s built in Python and focuses on security hygiene, local scanning, and ethical detection — making it ideal for demonstrating practical skills in Offensive Cybersecurity, Python automation, and Security Auditing.

Unlike basic regex tools, CredHunt includes:
File pattern scanning for .py, .env, .json, .cfg, .txt files
SHA-256 hashing of detected strings (to protect real secret values)
HTML and PDF reporting
Modular structure for future upgrades (system-wide scans, Git repo scans, or CI integration)

🚀 Features

✅ Scans for:
Hardcoded API keys, tokens, and private keys
Common patterns like password="..." or AKIA... (AWS keys)
High-entropy strings that resemble secrets

✅ Generates a clean HTML report (and optional PDF) with:
File path
Type of secret
Masked snippet
SHA-256 hash for safe identification

✅ Safe-by-design:
All scanning happens locally on the user’s system
No data is uploaded or transmitted anywhere
Results are hashed and redacted

✅ Easy to Extend:
Add new regex rules easily in scanner.py
Ready for CI integration and enterprise use cases

### 🧩 Project Structure

```
CredHunt/
│
├── credhunt.py              # Main runner script
│
├── core/
│   ├── scanner.py           # Main scanning logic
│   └── utils.py             # Helper functions (hashing, etc.)
│
├── reports/
│   ├── report.html          # Auto-generated HTML report
│   └── report.pdf           # Optional PDF output
│
├── templates/
│   └── report_template.html # HTML report structure
│
├── test_data/
│   ├── config.py            # Sample data for testing
│   └── keys.env             # Example .env file with credentials
│
└── requirements.txt         # Python dependencies
```

⚙️ Installation
1️⃣ Create a Virtual Environment
python -m venv credHunt-venv
.\credHunt-venv\Scripts\activate

2️⃣ Install Dependencies
pip install -r requirements.txt

Typical requirements.txt: 
pdfkit
jinja2

3️⃣ Install wkhtmltopdf (for PDF export)
Download from: https://wkhtmltopdf.org/downloads.html
After installation, make sure it’s added to your PATH or manually configure the binary path inside reporter.py: 
path = r"C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe"
config = pdfkit.configuration(wkhtmltopdf=path)

🧠 Usage
🔹 Basic Scan (Local Folder)
python credhunt.py
When prompted, enter a folder path, e.g.:
Enter path to scan: C:\Users\Srikar\Desktop\projects\test_data

Output:
report.html → Saved inside /reports
report.pdf → Optional (if wkhtmltopdf installed)

🔹 Sample Output
File	Type	Snippet	Hash
test_data/config.py	AWS Access Key	AKIAIOSFODNN7EXAMPLE	1a5d44a2dca19669d...
test_data/config.py	Password String	password="mySecret123"	3421f653163ddbc9...
test_data/keys.env	Possible API Key	wJalrXUtnFEMI/K7M...	78314b11be2e5815...

💡 Future Enhancements
Add system-mode scanning for .aws, .ssh, .env folders (with user consent).
GitHub repo scanning using the PyGitHub API.
Web UI with Flask for uploading zip files.
GitHub Actions pipeline to auto-run scans on commits.

🧑‍💻 Skills Demonstrated
Python for Cybersecurity Automation
Regex for Secret Detection
Secure Report Generation (HTML/PDF)
Safe Data Handling (hashing, redaction)
Modular Code Architecture

🧾 License
This project is for educational and ethical research purposes only.
Do not use CredHunt to scan systems or code you do not have permission to access.
