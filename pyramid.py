import math as m


X = lambda Sn1, Sn2, high: high / 3 * (Sn1 + Sn2 + m.sqrt(Sn1 * Sn2))



def main():
    Sn1 = float(input("Введите площадь нижнего основания "))
    Sn2 = float(input("Введите площадь верхнего основания "))
    high = float(input("Введите высоту усечённой пирамиды "))
    print(f"ОбЪём усечённой пирамиды составляет {X ( Sn1, Sn2, high )} кубических единиц")

if __name__ == "__main__":
    main()