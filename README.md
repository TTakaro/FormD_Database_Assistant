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

3. Set up your OpenAI API key in your bash rc.
```bash
API_KEY=##################
EXPORT API_KEY
```

## Usage

1. Run the main script with a natural language query:
    ```bash
    python main.py
    ```

2. Example output:
    ```
    [('exemption1', 50), ('exemption2', 30)]
    ```
