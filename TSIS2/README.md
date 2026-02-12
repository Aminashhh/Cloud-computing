Judge Agent – AI Evaluation Project

About the Project
Judge Agent is a simple AI-based system that checks and evaluates student assignments automatically.
Instead of grading manually, the system reads the submitted text and gives feedback using an AI model. It can provide a score and explain what was done well and what needs improvement.
The main idea of this project is to show how artificial intelligence can help in education and save time for teachers.

Technologies Used
Python
OpenAI API
PDF/text file processing
JSON for results

How It Works
A file is uploaded or selected.
The program reads the content.
The text is sent to the AI model through API.
The AI analyzes the work and returns feedback and a score.

How to Run
Install required libraries:
pip install -r requirements.txt
Add your OpenAI API key to a .env file:
OPENAI_API_KEY=your_api_key_here

Run the program:
python main.py

Common Errors
FileNotFoundError – wrong file path or file does not exist.
API error – invalid API key or no internet connection.

Conclusion
This project demonstrates how AI can be used to automatically evaluate assignments and provide helpful feedback. It is a basic prototype that can be improved and expanded in the future.
