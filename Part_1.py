

#Writen by Kim Öst
#BIO511

numbers = [15,-5,-12, 7, 10,-7,3,-10,4]

#a
def part_a(nums = numbers):
    sum = 0
    for num in nums:
        if abs(num) >= 10:
            sum += abs(num)
    
    print(sum)

#b

def part_b(nums = numbers):
    cubes = []
    for num in nums:
        if num < 0:
            cube = num ** 3
            cubes.append(cube)

    print(cubes)

#c
def part_c(nums = numbers):
    tracker = []

    for num in nums:
        if abs(num) in tracker:
            print(abs(num))
            return None
        tracker.append(abs(num))
    print('No reapeats')

part_a()
part_b()
part_c()
