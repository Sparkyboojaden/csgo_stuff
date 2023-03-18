import psycopg2
from config import pg_host, pg_db, pg_user, pg_pass

conn = psycopg2.connect(
    host= pg_host
    database=pg_db
    user=pg_user
    password=pg_pass
)

# Create a cursor object
cur = conn.cursor()

# Insert data into the "test" table
cur.execute("INSERT INTO test (item, price) VALUES (%s, %s)", ("value1", 123))

# Commit the transaction
conn.commit()

# Close the cursor and connection
cur.close()
conn.close()