import psycopg

#dbaname vai receber o nome do banco de dados, user vai receber o nome do usuário, password vai receber a senha do usuário
with psycopg.connect("dbname=integrado-python user=postgres password=postgres") as conn:
     with conn.cursor() as cur:

        cur.execute("""
            CREATE TABLE IF NOT EXISTS teste2 (
                id serial PRIMARY KEY,
                num INT,
                data VARCHAR(14)
            )
        """)
        
        cur.execute("SELECT * FROM teste2")
        dados_teste2 = cur.fetchall()
        print(dados_teste2)

        if len(dados_teste2) == 0:
            cur.execute("""
                INSERT INTO teste2 (num, data) VALUES (%s, %s)
                """, (1, "Um texto aqui!"))

        

def main():
    print("Hello from post-py-integration!")


if __name__ == "__main__":
    main()
