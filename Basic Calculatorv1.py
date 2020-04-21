againBreak = "again"
while againBreak == "again":
    first = input('type the first number:')
    print('type m for multiplication, d for division with decimals, s for subtraction,')
    op = input(' a for addition, ex for exponents, or dr for division with remanders:').lower()
    second = input('type the second number:')
    dec = input('is your number a decimal? (y/n):').lower()
    if dec in ('yes', 'y'):
          num1 = float(first)
          num2 = float(second)
    elif dec in ('no', 'n'):
        num1 = int(first)
        num2 = int(second)
    else:
        print("typeError, wrong input")
    if op in ('m'):
        ans = num1 * num2
    elif op in ('d'):
        ans = num1 / num2
    elif op in ('s'):
        ans = num1 - num2
    elif op in ('a'):
        ans = num1 + num2
    elif op in ('ex'):
        ans = num1 ** num2
    elif op in ('dr'):
        m = num1 % num2
        dv = num1 // num2
        dv = str(dv)
        m = str(m)
        ans = dv + " R" + m
    else:
        ans = "typeError, invalid operation"
    ans = str(ans)
    print(ans)
    againBreak = input('type "again" to go again, or type anything else to quit:').lower()
print("Goodbye!")    
      
      
    
      
