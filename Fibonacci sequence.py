import sys
sys.set_int_max_str_digits(1000000)
n = int(input("숫자"))
def fibonacci(n):
    checklist = [0,1]
    for i in range(2,n+1):
        new_checklist = checklist[i-1] + checklist[i-2]
        checklist.append(new_checklist)
    return checklist[n]

print(fibonacci(n))