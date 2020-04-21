againBreak = "again"
while againBreak == "again":
    print('type m for multiplication, d for division with decimals, s for subtraction,')
    op = input(' a for addition, sq for squares or adv for advanced calculations:').lower()
    if (op == 'adv'):
        print('type ex for exponents, dr for division with remanders,')
        op = input('or pm for geometric perimeter calculations:').lower()
    first = input('type the first number:')
    second = input('type the second number (leave blank if not applicable):')
    dec = input('is your number a decimal? (y/n):').lower()
    if dec in ('yes', 'y') and second not in ('', None):
          num1 = float(first)
          num2 = float(second)
    elif dec in ('no', 'n') and second not in ('', None):
        num1 = int(first)
        num2 = int(second)
    elif dec in ('no', 'n') and second in ('', None):
        num1 = int(first)
    elif dec in ('yes', 'y') and second in ('', None):
        num1 = int(first)
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
        num3 = num1 % num2
        num4 = num1 // num2
        num4 = str(num4)
        num3 = str(num3)
        ans = dv + " R" + m
    elif op in ('pm'):
        num3 = num1 * 2
        num4 = num2 * 2
        ans = num3 + num4
    elif op in ('sq'):
        num3 = num1 ** 2
        ans = num3
    else:
        ans = "typeError, invalid operation"
    ans = str(ans)
    print(ans)
    againBreak = input('type "again" to go again, or type anything else to quit:').lower()
print("Goodbye!")    
      
      
    
      
