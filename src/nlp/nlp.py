from openai import OpenAI
from os import getenv
from dotenv import load_dotenv

from src.nlp.form_d_instructions import form_d_prompt


load_dotenv()
api_key = getenv("API_KEY")
client = OpenAI(api_key=api_key)

sys_prompt = """
You are an assistant that converts natural language queries into SQL queries. The database you
are working with is the form D database. Here is a description of the database: {form_d}
"""


class NLP:
    def __init__(self, api_key):
        return

    def query_to_sql(self, query):
        response = client.chat.completions.create(model="gpt-3.5-turbo-16k",
        messages=[
            {"role": "system", "content": sys_prompt.format(form_d_prompt)},
            {"role": "user", "content": query}
        ])
        return response.choices[0].message.content.strip()
