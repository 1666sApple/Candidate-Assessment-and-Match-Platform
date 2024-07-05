# Resume Summarizer

A Streamlit web application to summarize resumes, highlight skills to improve, suggest skills to learn, and evaluate the fit of a candidate for a job position using Google's Gemini model.

## Features

- Upload a resume in PDF format.
- Summarize the resume.
- Highlight skills the applicant needs to improve.
- Suggest crucial skills the applicant needs to learn.
- Evaluate the applicant's fit for the role and emphasize relevant strengths.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/1666sApple/Candidate-Assessment-and-Match-Platform.git
    ```

2. Change to the project directory:
```bash
cd Candidate-Assessment-and-Match-Platform
```
3. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```
4. Install the required packages:
```bash
pip install -r requirements.txt
```

## Configuration 
1. Create a `.env` file in the root directory of the project and add `Google_API_KEY`:

```bash
GOOGLE_API_KEY=your_google_api_key_here
```

## Usage
1. Run the application:
```bash
streamlit run app.py
```
2. Open the generated link in your web browser.
3. Upload a resume in PDF format and provide the job description.
4. Click the "Summarize" button to generate a summary of the resume.

