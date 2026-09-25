import psycopg

#dbaname vai receber o nome do banco de dados, user vai receber o nome do usuário, password vai receber a senha do usuário
with psycopg.connect("dbname=integrado-python user=postgres password=postgres") as conn:
     with conn.cursor() as cur:

        # Execute a command: this creates a new table
        cur.execute("""
            CREATE TABLE teste2 (
                id serial PRIMARY KEY,
                num INT,
                data VARCHAR(14)
            )
        """)
        
        cur.execute("""
            INSERT INTO teste2 (num, data) VALUES (%s, %s)
            """, (1, "Um texto aqui!"))

def main():
    print("Hello from post-py-integration!")


if __name__ == "__main__":
    main()
