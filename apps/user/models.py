
cart_query = """
    CREATE TABLE IF NOT EXISTS carts 
    (
        id SERIAL PRIMARY KEY,
        product_name VARCHAR(64) NOT NULL,
        quantity INTEGER NOT NULL,
        price FLOAT NOT NULL,
        total FLOAT NOT NULL,
        user_id INTEGER REFERENCES users(id)
    )
"""