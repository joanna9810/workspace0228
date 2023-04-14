import queue
my_menu = { 'lasagna': 14.75,
  'moussaka': 21.15,
  'sushi': 16.05,
  'paella': 21,
  'samosas': 14
}

my_orders = queue.SimpleQueue()
my_orders.put("bibimbab")
my_orders.get("samosas")
print(my_orders)

for key, value in my_menu.items():
    print(f"the price of the {key} is {value}")
