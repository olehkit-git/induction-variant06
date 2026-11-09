def isDivide(number: int) -> bool:
    expression = 3 ** (2 * number + 1) + 2 ** (number + 2)
    return expression % 7 == 0

def main() -> None:
    badList: list[int] = []

    for number in range(1, 101):
        if not isDivide(number=number):
            badList.append(number)

    if not badList:
        print("Контрприкладів не знайдено")
    else:
        print(f"Знайдено контрприклади: {badList}")

if __name__ == "__main__":
    main()