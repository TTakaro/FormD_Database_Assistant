# primeAssessment: Form D Analyzer

## Setup

1. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

2. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

3. Set up your OpenAI API key in the .env file.
```bash
API_KEY=##################
```

## Usage

1. Run the streamlit frontend script:
    ```bash
    streamlit run main.py
    ```

2. Example output:
    ```
    [('exemption1', 50), ('exemption2', 30)]
    ```
