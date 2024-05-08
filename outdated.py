month_list = ["январь", "февраль", "март", "апрель",
     "май", "июнь", "июль", "август", "сентябрь", "октябрь",
     "ноябрь", "декабрь"]
number_list = ['1','2','3','4','5','6','7','8','9','01','02','03','04','05','06','07','08','09','10','11','12']
while True:
    try:
        date = list((input("Дата: ").split('.')))
        if len(date)==1:
            date = list(date[0].split())
        
        year = int(date[2])
        month =date[1]
        day = int(date[0])
        break
    except ValueError:
        pass
    
if int(day)<=31 and ((month in month_list) or (month in number_list)):
    print(f"{year:02}",end="-")
    if month in month_list:
        print(f"{(int(month_list.index(month)+1)):02}",end="-")
    if month in number_list:
        print(f"{int(month):02}",end="-")
    print(f"{int(day):02}")