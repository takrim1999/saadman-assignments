name = input("Name of Student\n>")
total = 0
for i in range(1,6):
    total += int(input(f"Mark of Subject {i}: "))
# assuming 40 is the pass mark
if total<200:
    print("Name: ",name)
    print("Result: Failed")
else:
    print("Name: ",name)
    print("Result: Passed")
    print("Percentage: ", round((total/5),2))
    