from validations import validate_inputs
validate_strings = lambda x: len(x) > 0
validate_number = lambda x: x> 0
class Product:
    def create_product(self, list_products , name, brand, category, price, amount, warranty):
        if self.product_exists(list_products, name, amount):            
            print("\033[32mThe product exists, the amount has add to the stock\033[0m")
        else:
            product = {
                'name' : name,
                'brand' : brand,
                'category' : category,
                'price' : price,
                'amount' : amount,
                'warranty' : warranty
            }
            list_products.append(product)
            print(f"Producto creado {product}")
            
        return list_products
    
    
    def product_exists(self, products, name, amount):
        for product in products:
            if product['name'] == name:
                product['amount'] += amount
                return True
        return False
    
    def consult_product(self, list_products ,name):
        product_found = self.search_product(list_products, name)
           
        if product_found is None or len(list_products) < 1:
            print("The product does not exist")
        else: 
            print(f"{'Product name':<15}|{'Brand':<10}|{'Category':<10}|{'Price':<10}|{'Amount':<10}|{'Warranty':<10}")
            print(f"{product_found['name']:<15}|{product_found['brand']:<10}|{product_found['category']:<10}|{product_found['price']:<10}|{product_found['amount']:<10}|{product_found['warranty']:<10}")
            
    def search_product(self, list_products, name):
        for product in list_products:
            if product['name'] == name:
               return product
        return None
        
    def update_product(self,list_products, name=None):
        product_found = self.search_product(list_products,name)
        if product_found is None or len(list_products) < 1:
            return "\033[31mThe product does not exist\033[0m"
        else:
             while True:
                print("What do you want to update?")
                print('1- Product name')
                print('2- Product brand')
                print('3- Product category')
                print('4- Product price')
                print('5- Product amount')
                print('6- Product warranty')
                print('0- Back')
                opcion_update = validate_inputs(str,"Choose an option: ", validate_strings)
                match opcion_update:
                    case '1':
                        change = validate_inputs(str,"type de new name: ", validate_strings)
                        product_found['name'] = change
                        return f"\033[32mName updateded to: {change} \033[0m"
                    case '2':
                        change = validate_inputs(str,"type de new brand: ", validate_strings)
                        product_found['brand'] = change
                        return f"\033[32mBrand updateded to: {change} \033[0m"
                    case '3':
                        change = validate_inputs(str,"type de new category: ", validate_strings)
                        product_found['category'] = change
                        return f"\033[32mCategory updateded to: {change} \033[0m"
                    case '4':
                        change = validate_inputs(int,"type de new price: ", validate_number)
                        product_found['price'] = change
                        return f"\033[32mPrice updateded to: {change} \033[0m"
                    case '5':
                        change = validate_inputs(int,"type de new amount: ", validate_number)
                        product_found['amount'] = change
                        return f"\033[32mStock updateded to: {change} \033[0m"
                    case '6':
                        change = validate_inputs(int,"type de new warranty: ", validate_number)
                        product_found['warranty'] = change
                        return f"\033[32mWarranty updateded to: {change} \033[0m"
                    case '0':
                        print("Back")
                        break
                    
    def delete_product(self, list_products, name):
        product_found = self.search_product(list_products,name)
        if product_found is None or len(list_products) < 1:
            return "\033[31mThe product does not exist\033[0m"
        else:
            product_name = product_found['name']
            list_products.remove(product_found)
            return f"\033[32mProduct deleted: {product_name}\033[0m"