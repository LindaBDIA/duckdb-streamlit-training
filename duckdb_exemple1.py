import duckdb

db = duckdb.connect(database=':memory:')
db.execute("CREATE TABLE people (id INTEGER, name TEXT, age INTEGER)")
db.execute("INSERT INTO people VALUES (1, 'Alice', 25), (2, 'Bob', 30), (3, 'Charlie', 35)")
result = db.execute("SELECT * FROM people").fetchall()
print(result)

db.execute("CREATE TABLE titanic AS SELECT * FROM read_csv_auto('data/titanic.csv')")
result = db.execute("SELECT COUNT(*) FROM titanic").fetchall()
print(result)

query = """
SELECT Sex, COUNT(*) AS survivors
FROM titanic
WHERE Survived = 1
GROUP BY Sex
"""
result = db.execute(query).fetchdf()
print(result)