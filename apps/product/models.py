product_query = """
    CREATE TABLE IF NOT EXISTS products 
    (
        id SERIAL PRIMARY KEY,
        product_name VARCHAR(64) NOT NULL,
        price FLOAT NOT NULL,
        quantity INTEGER NOT NULL
    )
"""