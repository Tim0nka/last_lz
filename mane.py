import pyramid as p
import Arhimed as A


def main():
    user_choise = int(input("Выберите функцию, которую хотите использовать 1 или 2: "))
    if user_choise == 1:
        base_1 = float(input("Введите площадь нижнего основания "))
        base_2 = float(input("Введите площадь верхнего основания "))
        height = float(input("Введите высоту усечённой пирамиды "))
        print(f"ОбЪём усечённой пирамиды составляет {p.X(base_1, base_2, height)} кубических единиц")
    elif user_choise == 2:
        massivny = float(input("Введите массу: "))
        vobyem = float(input("Введите объём погружённой части: "))
        povny = float(input("Введите плотность: "))
        A.Arhimed(massivny, vobyem ,povny)
    else:
        print('выберите из 1 или 2')



if __name__ == "__main__":
    main()