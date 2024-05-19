Fruits = {"Apple":{'calories':130},
          "Avocado":{'calories':50},
          "Lime":{'calories':20},
          "Banana":{'calories':110},
          "Grapes":{'calories':90}

}

A = str(input("Фрукт: "))

if A in Fruits:
    cal = (Fruits.get(A)).get('calories')
    print("Калории: "+ str(cal))
