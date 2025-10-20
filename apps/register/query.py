from core.database import execute_query


class RegisterQueries:
    @staticmethod
    def register_users(params: tuple) -> None | bool:
        try:
            name , parol , phone = params
            query_select = """
                    SELECT * FROM users WHERE name = %s
            """
            users = execute_query(query=query_select, params = (name,),fetch='one')


            if users:
                print("User already exists")
                return False


            query = """INSERT INTO users (name, parol,phone,is_active)
                       VALUES (%s, %s,%s, FALSE) 
                    """
            execute_query(query=query, params=(name, parol, phone))



            get_id_user = """
                             SELECT id FROM users WHERE name = %s
                        """
            result = execute_query(query=get_id_user, params=(name,),fetch='one')

            if not result:
                print("User not registered")
                return None

            user_id = result['id']



            query = """
                    INSERT INTO carts (product_name, quantity, price, total, user_id)
                    VALUES ('', 0, 0, 0, %s)
                """
            execute_query(query=query, params=(user_id,))
            print("Added user")
            return True


        except Exception as e:
            print(e)
            return None

    from core.database import execute_query



class LoginQueries:

    @staticmethod
    def login_user(params: tuple) -> bool:
        a_name = 'a'
        a_parol = 'a'

        try:
            name, parol = params
            if name == a_name and parol == a_parol:
                return "admin"

            query = """SELECT * FROM users WHERE name = %s AND parol = %s"""
            user = execute_query(query=query,params=(name, parol),fetch="one")

            if not user:
                print("Wrong name or password")
                return False

            update_query = """UPDATE users SET is_active = TRUE WHERE id = %s"""
            execute_query(query=update_query,params=(user['id'],))

            print(f"Welcome {user['name']}")
            return 'user'

        except Exception as e:
            print(e)
            return False

