# Your code below:
toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]

prices = [2, 6, 1, 3, 2, 7, 2]


num_two_dollar_slices = prices.count(2)
num_pizzas = len(toppings)

print("We sell", num_pizzas, "different kinds of pizza!")



pizzas_and_prices = list(zip(prices, toppings))
pizzas_and_prices.sort()
pizzas_and_prices.pop(-1)
pizzas_and_prices = pizzas_and_prices + [(2.5, "peppers")]

pizzas_and_prices.sort()

print(pizzas_and_prices)



cheapest_pizza = pizzas_and_prices[0]

priciest_pizza = pizzas_and_prices[-1]

three_cheapest = pizzas_and_prices[0:3]
print(three_cheapest)



