from apps.user.models import cart_query
from core.database import execute_query

main_menu = """
1. User
2. Admin
3. Exit
"""

user_menu = """
1. Show products
2. Show products in cart
3. Add products to cart
4. Delete product
5. Exit
"""


admin_menu = """
1. Add product
2. Delete product
3. Update product
4. Show product
5. Exit
"""



def get_user_option(menu: str, max_option: int):
    while True:
        print(menu)
        option = input("Enter your option: ")
        if not (1 <= int(option) <= max_option):
            print("Invalid option number!")
        else:
            return option


def execute_tables():
    from apps.user.models import user_query
    from apps.product.models import product_query

    execute_query(query=user_query)
    execute_query(query=product_query)
    execute_query(query=cart_query)