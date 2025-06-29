def addition(a, b):
    return a + b


def subraction(a, b):
    return a - b


def multiplatin(a, b):
    return a * b


def divition(a, b):
    return a / b


culculate = {
    "+": addition,
    "-": subraction,
    "*": multiplatin,
    "/": divition
}


def culculateFunction():
    durum = True
    firstNum = float(input("Enter your first number : "))
    while durum:
        for i in culculate.keys():
            print(i)
        sign = input("Choose your calculation sign : ")
        secondNum = float(input("Enter your second number : "))

        res = culculate[sign](firstNum, secondNum)
        result = f"Your result is ( {firstNum} {sign} {secondNum} = {res} )"
        print(result)

        alinanCevap=input("Sonuc uzerinden devam etmek istiyor musun 'c' ye basin. Eger yeni bir hesaplama yaomak istiyorsaniz 'n' ye basin ")

        if alinanCevap =="c":
            firstNum = res
        elif alinanCevap == "n":
            durum=False
            culculateFunction()
        else:
            break

culculateFunction()