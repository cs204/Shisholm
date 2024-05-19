def hello(hi):
    hi = hi.casefold()
    if hi=="здравствуйте": return "$0"
    if hi[0]=='з': return "$20"
    return('$100')


text = input('Приветствие: ')
print(hello(text))
