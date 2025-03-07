# Initial Task:
## Assignments
bangla = 84
english = 87
math = 92

## Calculating the average
average = (bangla + english + math) / 3
# Printing two times
for _ in range(2):
    print(average)

# improvement:

## take inputs
bangla = int(input("Grades for Bangla: "))
english = int(input("Grades for English: "))
math = int(input("Grades for Math: "))

## Calculating Average
average = (bangla + english + math) / 3

## Printing floating average
print(average)
## Printing int Average
average = int(average)
print(average)