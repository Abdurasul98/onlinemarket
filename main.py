from apps.admin.query import AdminQuery
from apps.user.query import UserQueries
from core.utils import get_user_option, main_menu, user_menu, admin_menu, execute_tables


class Menu:
    def main(self):
        while True:
            option = get_user_option(menu=main_menu,max_option=3)

            if option == "1":
                return self.user_main()

            elif option == "2":
                return self.admin_main()

            elif option == "3":
                print("Bye")
                exit()

            else:
                print("Invalid option")
                return self.main()


    def user_main(self):
        while True:
            option = get_user_option(menu=user_menu,max_option=6)

            if option == "1":
                AdminQuery.show_products()

            elif option == "2":
                UserQueries.show_products()

            elif option == "3":
                AdminQuery.show_products()
                product_name = input("Enter product name: ")
                product_quantity = int(input("Enter product quantity: "))
                UserQueries.add_product_to_cart((product_name, product_quantity))

            elif option == "4":
                UserQueries.show_products()
                product_name = input("Enter product name: ")
                UserQueries.delete_from_cart((product_name,))

            elif option == "5":
                print("Bye")
                return self.main()

            else:
                print("Invalid option")
                return self.user_main()



    def admin_main(self):
        while True:
            option = get_user_option(menu=admin_menu,max_option=5)

            if option == "1":
                AdminQuery.show_products()
                product_name = input("Enter product name: ")
                product_price = float(input("Enter product price: "))
                product_quantity = int(input("Enter product quantity: "))
                AdminQuery.add_product_to_magazine((product_name, product_price, product_quantity))


            elif option == "2":
                AdminQuery.show_products()
                product_id = int(input("Enter product ID: "))
                AdminQuery.delete_product_from_magazine(product_id)


            elif option == "3":
                AdminQuery.show_products()
                product_id = int(input("Enter product ID: "))
                new_name = input("Enter new product name: ")
                new_price = float(input("Enter new product price: "))
                new_quantity = int(input("Enter new product quantity: "))
                AdminQuery.update_product_in_magazine((new_name, new_price, new_quantity, product_id))


            elif option == "4":
                AdminQuery.show_products()

            elif option == "5":
                print("Bye")
                return self.main()

            else:
                print("Invalid option")
                return self.admin_main()



if __name__ == '__main__':
    execute_tables()
    Menu().main()