while True:
    try:
        x,y = map(int,input("Дробь: ").split('/'))
        z = x/y
        if z<=0.01:
            print('E')
            break
        elif z>1:
            pass
        elif (z>=0.99) and (z<=1):
            print('F')
            break
        else:
            print(f"{z*100:,.0f}%")
            break

    except (ValueError,ZeroDivisionError):
        pass
