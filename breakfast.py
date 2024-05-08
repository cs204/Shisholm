menu = {
  "кофе": 20.00,
  "чай": 10.00,
  "булочка": 5.00,
  "салат": 30.40,
  "пирожное": 45.50
}

summ=0


try:
    while True:
        choice = (str(input('Блюдо: '))).casefold()
        if choice in list(menu):
            summ+=menu.get(choice)
except EOFError:
    (print(f"\nСумма: {summ:.2f}"))
