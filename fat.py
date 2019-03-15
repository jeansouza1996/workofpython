def main():
    n = int(input("Digite o valor de n: "))
    fat = 1
    i = 2

    result = []

    while i <= n:
        result.append(fat)
        fat = fat*i
        i = i + 1

    result.append(fat)
    
    print (result)

main()