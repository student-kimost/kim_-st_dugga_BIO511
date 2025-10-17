

#Writen by Kim Öst
#BIO511

numbers = [15,-5,-12, 7, 10,-7,3,-10,4]

#a
def part_a():
    sum = 0
    for num in numbers:
        if abs(num) >= 10:
            sum += abs(num)
    
    print(sum)

#b

def part_b():
    cubes = []
    for num in numbers:
        if num < 0:
            cube = num ** 3
            cubes.append(cube)

    print(cubes)

#c
def part_c():
    tracker = set()

    for num in numbers:
        if abs(num) in tracker:
            print(abs(num))
            return None
        tracker.add(abs(num))
    print('No reapeats')

part_a()
part_b()
part_c()
