from core.database import execute_query


class UserQueries:
    @staticmethod
    def show_products():
        try:
            query = """ 
                    SELECT * FROM carts
                """

            result = execute_query(query=query,fetch='all')

            if not result:
                return False

            for row in result:
                print(f"{row['id']}) {row['product_name']} - {row['quantity']}ta ")
            return True

        except Exception as e:
            print(e)
            return None

    @staticmethod
    def add_product_to_cart(params: tuple) -> None | bool:
        try:
            product_name, quantity = params

            query_select = "SELECT * FROM products WHERE product_name = %s"
            product = execute_query(query=query_select, params=(product_name,), fetch='one')

            if not product:
                print("NOt found")
                return False

            if product['quantity'] < quantity:
                print("Yetarli maxsulot yoq")
                return False

            query = """INSERT INTO carts (product_name,quantity)
                       VALUES (%s, %s)
                    """

            execute_query(query=query, params=(product_name, quantity))

            query_update = """
                        UPDATE products
                        SET quantity = quantity -%s
                        WHERE product_name = %s
                    """
            execute_query(query=query_update, params=(quantity, product_name))
            print("Added product to cart")
            return True

        except Exception as e:
            print(e)
            return None


    @staticmethod
    def delete_from_cart(params: tuple) -> None | bool:
        try:
            query = """
                        DELETE FROM carts WHERE product_name = %s
                    """

            execute_query(query=query, params=params)
            print("Deleted product")
            return True
        except Exception as e:
            print(e)
            return None



