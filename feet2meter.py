
def feet2meter(v):
    v = str(v)
    v =float(v[:-2])
    res = v / 3.281
    return(res)

v = feet2meter(input("Сколько футов:"))
print(f"Это будет {v:.2f} метров.")
# def main():
#     v = feet2meter(input('Сколько футов:'))
# print(f'Это будет {v:.2f} метров.')
# def feet2meter(v):
#     v = v.rstrip("ft")
# v = float(v)
# v = v * 0.304
# return v

# main()
