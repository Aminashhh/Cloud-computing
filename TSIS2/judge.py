import json
import requests

with open("prd.txt", "r", encoding="utf-8") as f:
    prd = f.read()

with open("code_submission.py", "r", encoding="utf-8") as f:
    code = f.read()

system_prompt = """
You are a strict Senior Architect and QA Judge Agent.

Your task:
Compare the PRD requirements against the submitted code.

You must:
- Score compliance from 0 to 100.
- Check functionality.
- Check error handling.
- Check security risks.
- Detect missing FileNotFoundError handling.
- Detect usage of eval or exec.

You MUST output ONLY valid JSON.
Do NOT write explanations.
Do NOT write markdown.
Only JSON.

Required format:

{
  "compliance_score": 0-100,
  "status": "PASS" or "FAIL",
  "audit_log": [
    {
      "requirement": "...",
      "met": true or false,
      "comment": "..."
    }
  ],
  "security_check": "Safe" or "Unsafe"
}
"""

API_KEY = "AIzaSyBhiuMF1lb1DQLVSn4bk5z_Okb9uuccYTk"
url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={API_KEY}"

payload = {
    "contents": [
        {
            "parts": [
                {
                    "text": f"{system_prompt}\n\nPRD:\n{prd}\n\nCODE:\n{code}"
                }
            ]
        }
    ]
}

response = requests.post(url, json=payload)

if response.status_code == 200:
    result = response.json()
    result_text = result['candidates'][0]['content']['parts'][0]['text']
    result_text = result_text.replace('JavaScript json', '').replace('', '').strip()
    
    with open("compliance_report.json", "w", encoding="utf-8") as f:
        f.write(result_text)
    
    print("Compliance report created successfully!")
else:
    print(f"Error: {response.status_code}")
    print(response.json())
