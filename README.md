# Telelyzer

Telelyzer is a powerful AI-driven analytics platform built with Streamlit and Python, designed to analyze agent-customer interactions and detect potential misselling. Leveraging Crew AI for agentic workflows and a fine-tuned Tinu-BERT model, Telelyzer identifies misselling and provides actionable insights.

## Key Features

- Misselling Detection: Finetuned a Tiny-BERT model on misselling phrases dataset.
- Agentic Workflows: Integrates Crew AI to build agentic workflows to measure script adherence and rate agents.
- Voice Emotion Classification (Upcoming): Training a Deep Learning model to detect agent frustration. 
- Full Stack Integration (Upcoming): Build a full stack website using ReactJS & FastAPI. 


## Follow these steps to set up Telelyzer on your local machine:

### Prerequisites
- Python 3.8+
- Streamlit
- OpenAI API Key (if required for agentic workflows)

### Setup Instructions

1. **Clone the Repository**:


    ```bash
        git clone https://github.com/AtharvaMaskar26/telelyzer.git

        cd telelyzer
    ```

2. Installing Dependencies
    ```bash
        pip install -r requirements.txt
    ```

3. Create an env file. 
    In your root directory create a .env file and add your API KEY to it
    ```bash
        OPENAI_API_KEY = "sk-svcacct-LIZdd7QHUq6RN4MW0l1IT3BlbkFJwZTtbtIomtao6nXvrKhz"
    ```

4. You can download the model file from here, and store it in the model directory

5. Running the app
Launch Streamlit by running:
```bash
    streamlit run app.py
```

# Contributing
Feel free to suggest any changes.