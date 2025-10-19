from core.database import execute_query

class AdminQuery:
    @staticmethod
    def add_product_to_magazine(params: tuple) -> None | bool:
        try:
            query = """
                    INSERT INTO products(product_name, price, quantity)
                    VALUES(%s, %s, %s)
                """

            execute_query(query=query,params=params)
            print("Added products")
            return True
        except Exception as e:
            print(e)
            return None

    @staticmethod
    def delete_product_from_magazine(id_product)  -> None | bool:
        try:
            query = """
                    DELETE FROM products WHERE id = %s
                """

            params = (id_product,)
            execute_query(query=query,params=params)
            print("Deleted product")

            return True
        except Exception as e:
            print(e)
            return None



    @staticmethod
    def show_products()  -> None | bool:
        try:
            query = """ 
                    SELECT * FROM products
                """

            result = execute_query(query=query,fetch='all')

            if not result:
                return False

            for row in result:
                print(f"{row['id']}) {row['product_name']} - {row['price']} som- {row['quantity']} ta")
            return True

        except Exception as e:
            print(e)
            return None




    @staticmethod
    def update_product_in_magazine(params: tuple) -> None | bool:
        try:
            query = """
                UPDATE products
                SET product_name = %s,price = %s,quantity = %s
                WHERE id = %s
            """
            execute_query(query=query, params=params)
            print("Updated product")
            return True
        except Exception as e:
            print(e)
            return None
