def multiple(number):
    # input("Enter list of numbers: ")
    factors = []
    count = 2
    while number != 1:
        if number % count == 0:
            factors.append(count)
            number /= count
            count = 1
        count += 1
    return factors


if __name__ == '__main__':
    result = multiple(10000)
    print(result)

