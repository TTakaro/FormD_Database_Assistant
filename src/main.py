from db.database import Database
from nlp.nlp import NLP, api_key


class FormDAnalyzer:
    def __init__(self, db_path, api_key):
        self.db = Database(db_path)
        self.nlp = NLP(api_key)

    def process_query(self, natural_language_query):
        sql_query = self.nlp.query_to_sql(natural_language_query)
        print(f"SQL Query: {sql_query}")
        results = self.db.execute_query(sql_query)
        return results

    def close(self):
        self.db.close()


if __name__ == "__main__":
    db_path = "../data/form_d_database.db"

    analyzer = FormDAnalyzer(db_path, api_key)

    # query = What were the most frequently used federal exemptions?"
    # query = "What are the most prevalent industry sectors represented?"
    query = "Where are offerings originating from geographically? How has this changed over time?"
    response = analyzer.process_query(query)
    print(response)

    analyzer.close()
