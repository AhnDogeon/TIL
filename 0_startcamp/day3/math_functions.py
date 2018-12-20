def average(numbers):
    return sum(numbers) / len(numbers)

def cube(x):
    return x * x * x

# # 1. 평균값을 구하시오
# my_score = [79, 84, 66, 93]
# print(my_score)
# print(average(my_score))

# print(cube(3))



def main():
    my_score = [79, 84, 66, 93]
    print(average(my_score))
    print(cube(3))

if __name__ == '__main__':
    main()