user_query = """
    CREATE TABLE IF NOT EXISTS users
    (
        id SERIAL PRIMARY KEY,
        name VARCHAR(64) NOT NULL ,
        parol VARCHAR(64) NOT NULL,
        phone VARCHAR(64) NOT NULL ,
        is_active BOOLEAN DEFAULT FALSE
    )
"""