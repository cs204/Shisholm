print("Какой ответ на главный вопрос жизни, вселенной и всего такого? ", end="")

try:
    answer = input()
    answer = str(answer.casefold())
    if (str(answer)=="сорок два") or (int(answer)==42) :
        print('Да')
    else:
        print("Нет")
except ValueError:
    pass
