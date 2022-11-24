from steel import main_steel
from cast_iron import main_cast_iron
import time
def main():
    start_time=time.time()
    choise=int(input("1 - выгрузить чугун, 2 - выгрузить сталь, 3 - выгрузить и сталь и чугун\n"))
    year, month_inp = (input("Введите год и номер месяцa, с которого выгружаем (через пробел)\n")).split()

    if choise==1:
        main_cast_iron(year, month_inp)
        print(f"Затраченное время на выгрузку чугуна: {time.time() - start_time} сек")
    elif choise==2:
        main_steel( year, month_inp)
        print(f"Затраченное время на выгрузку стали: {time.time() - start_time} сек")
    elif choise==3:
        main_steel(year, month_inp)
        main_cast_iron(year, month_inp)
        print(f"Затраченное время на выгрузку стали и чугуна: {time.time() - start_time} сек")

main()