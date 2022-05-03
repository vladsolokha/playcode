numbers = [x for x in range(101)]

for i, num in enumerate(numbers):
    print('%d is i and %d is num' % (i, num))
    if num % 3 == 0:
        numbers[i] = "fizz"
    if num % 5 == 0:
        numbers[i] = "buzz"
    if num % 5 == 0 and num % 3 == 0:
        numbers[i] = "fizzbuzz"

print(numbers)