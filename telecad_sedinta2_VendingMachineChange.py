#create a product dictionary, containing both mames and prices for each product
products_number = int(input('How many products: '))
i = 1
products_prices = {}
while i <= products_number:
    product = input("Give a product: ")
    product_price = int(input("Give the price: "))
    products_prices[product] = product_price
    i += 1

#ask customer to choose a product
print("This are our products: ", products_prices, '\nWhat do you want?')
choice = input("I want: ")

price = products_prices[choice]
cash = int(input('$$$Bill: '))
change = cash - price
print('Change:', change)

coins = [5, 10, 100, 150]
rest_of_payment = []


while change != 0:
    for coin in coins[::-1]:
        if change // coin != 0:
            for i in range(change//coin):
                rest_of_payment.append(coin)
                change %= coin
print(rest_of_payment)