from langchain.tools import Tool
import sqlite3

def db_func(query):
    # Connect to the database
    db_path = "../data/form_d_database.db"
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Execute the query
    cursor.execute(query)

    # Fetch all results
    results = cursor.fetchall()

    # Close the connection
    conn.close()
    return results

db_tool = Tool.from_function(
    func=db_func,
    name="QueryDatabase",
    description="Sends a SQL query to the form d database. Use this to tell the user about the contents of the database."
)