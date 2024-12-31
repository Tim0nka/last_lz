def Arhimed(m, V, po):
    if po > 1:
        print("Предмет не является плавучим")
    elif po == 1:
        print("Предмет является частично плавучим")
    else:
        print("Предмет является плавучим")



def main():
    massivny = float(input("Введите массу: "))
    vobyem = float(input("Введите объём погружённой части: "))
    povny = float(input("Введите плотность: "))
    Arhimed(massivny, vobyem ,povny)

if __name__ == "__main__":
    main()