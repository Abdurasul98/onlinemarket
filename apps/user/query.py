from core.database import execute_query


class UserQueries:
    current_user_id = None

    @staticmethod
    def show_products():
        try:
            query = """ 
                    SELECT * FROM carts
                    WHERE user_id = %s AND quantity > 0
                """

            result = execute_query(query=query,params=(UserQueries.current_user_id,),fetch='all')

            if not result:
                return False

            for row in result:
                total_price = row['price'] * row['quantity']
                print(f"{row['id']}) {row['product_name']} - {row['quantity']}ta - {row['price']} som - Jami: {total_price} som")
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
                print("Not found")
                return False

            if product['quantity'] < quantity:
                print("Yetarli maxsulot yoq")
                return False

            total = product['price'] * quantity

            query = """INSERT INTO carts (product_name,quantity,price,total,user_id)
                       VALUES (%s,%s, %s,%s,%s)
                    """

            execute_query(query=query, params=(product_name, quantity,product['price'],total,UserQueries.current_user_id))

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
            product_name = params[0]
            query = """
                        DELETE FROM carts WHERE product_name = %s AND user_id = %s
                    """

            execute_query(query=query, params=(product_name,UserQueries.current_user_id))
            print("Deleted product")
            return True
        except Exception as e:
            print(e)
            return None



