from productos import Product
from validations import validate_inputs

products = Product()
list_products = [{
    'name' : "prueba",
    'brand' : "brand test",
    'category': "category test",
    'price' : 1,
    'amount' : 2,
    'warranty' : 3
}]

validate_strings = lambda x: len(x) > 0
validate_number = lambda x: x> 0


while True:
    print("1. Inventory management")
    print("2. Sales registration and inquiry")
    print("3. Reports module")
    print("0. Exit")
    opcion_menu = validate_inputs(str,"Choose an option: ", validate_strings)
    match opcion_menu:
        case '1':
            print("1. Registrar Producto")
            print("2. Consultar Producto")
            print("3. Actualizar Producto")
            print("4. Eliminar Producto")
            print("0. Back")
            opcion_submenu = validate_inputs(str,"Choose an option: ", validate_strings)
            match opcion_submenu:
                case '1':
                    name = validate_inputs(str,"Type the name: ", validate_strings).lower()
                    brand = validate_inputs(str,"Type the brand: ", validate_strings).lower()
                    category = validate_inputs(str,"Type the category: ", validate_strings).lower()
                    price = validate_inputs(float,"Type the price: ", validate_number)
                    amount = validate_inputs(int,"Type the amount: ", validate_number)
                    warranty = validate_inputs(int,"Type the warranty (In monts): ", validate_number)
                    list_products = products.create_product(list_products, name, brand, category, price, amount, warranty)
                        
                case '2':
                    name = validate_inputs(str,"Type the product name to search: ", validate_strings).lower()
                    products.consult_product(list_products,name)
                case '3':
                    name = validate_inputs(str,"Type the product name to update: ", validate_strings).lower()
                    print(products.update_product(list_products,name))
                case '4':
                    name = validate_inputs(str,"Type the product name to update: ", validate_strings).lower()
                    print(products.delete_product(list_products,name))
                case _ :
                    print("\033[31mIvalid option\033[0m") 
        case '0':
            break        
        case _ :
            print("\033[31mIvalid option\033[0m") 
            
