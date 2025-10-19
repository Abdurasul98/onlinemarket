user_query = """
    CREATE TABLE IF NOT EXISTS users
    (
        id SERIAL PRIMARY KEY,
        name VARCHAR(64) NOT NULL UNIQUE,
        parol VARCHAR(64) NOT NULL,
        phone VARCHAR(64) NOT NULL UNIQUE,
        is_active BOOLEAN DEFAULT FALSE,
        is_login BOOLEAN DEFAULT FALSE
    )
"""


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