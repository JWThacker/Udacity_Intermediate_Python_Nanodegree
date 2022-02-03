class User():
    def __init__(self, id, name):
        self._id = id
        self._name = name
        self.reviews = []

    def sell_product(self, name, description, price):
        available = True
        return Product(name, description, price, self._name, available)
        
    def buy_product(self,product):
        if product.available:
            product.available = False
        else:
            print(f"{product.name} is no longer available.")

    def write_review(self, review, product):
        user_review = Review(review, self._name, product)
        self.reviews.append(user_review)
        product.reviews.append(user_review)
        return user_review 

class Product():
    def __init__(self, name, description, price, seller_name, available):
        self.name = name
        self.description = description
        self.price = price
        self.available = available
        self.seller = seller_name
        self.reviews = []

class Review():
    def __init__(self, description, user, product):
        self.description = description
        self.user = user 
        self.product = product

def main():
    brianna = User(1, 'Brianna')
    mary = User(2, "Mary")

    keyboard = brianna.sell_product('Keyboard', 'A nice mechanical keyboard', 100)
    print(keyboard.available) #True
    mary.buy_product(keyboard)
    print(keyboard.available) #False
    review = mary.write_review('This is the best keyboard ever!', keyboard)
    print(review in mary.reviews) #True
    print(review in keyboard.reviews) #True
    brianna.buy_product(keyboard) #keyboard is no longer availale

if __name__ == "__main__":
    main()
