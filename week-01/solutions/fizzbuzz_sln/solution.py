def fizzbuzz(n: int)->list[str]:
    answer = []
    for i in range(1,n+1):
        if i % 3 == 0 and i % 5 == 0:
            answer.append("FizzBuzz")
        elif i % 3 == 0:
            answer.append("Fizz")
        elif i % 5 == 0:
            answer.append("Buzz")
        else:
            answer.append(str(i))
    return answer

def main():
    n = int(input("Enter a number: "))
    result = fizzbuzz(n)
    for item in result:
        print(item)

if __name__ == "__main__":
    main()