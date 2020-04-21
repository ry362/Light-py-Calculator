againBreak = "again"
while againBreak in ("again", "go", "restart"):
    print('type m for multiplication, d for division with decimals, s for subtraction,')
    op = input(' a for addition, sq for squares or adv for advanced calculations:').lower()
    if (op == 'adv'):
        print('type ex for exponents, dr for division with remanders,')
        op = input('or pmr for geometric rectangle perimeter calculations:').lower()
    if op in ('m'):
        first = input('type the number you want to multiply:')
        second = input('type the number you want to multiply by:')
    elif op in ('d'):
        first = input('type the number you want to divide:')
        second = input('type the number you want to divide by:')
    elif op in ('s'):
        first = input('type the number you want to subtract from:')
        second = input('type the number you want to subtract:')
    elif op in ('a'):
        first = input('type the number you want to add to:')
        second = input('type the number you want to add to the first number:')
    elif op in ('ex'):
        first = input(':')
        second = input(first + ' to the power of:')
    elif op in ('dr'):
        first = input('type the number you want to divide:')
        second = input('type the number you want to divide by:')
    elif op in ('pmr'):
        first = input('type the length of the rectangle:')
        second = input('type the width of the rectangle:')
    elif op in ('sq'):
        first = input('type the number you want to square:')
    else:
        ans = "typeError, invalid operation"
    dec = input('Is one, or both of your numbers decimals? (y/n):').lower()
    if dec in ('yes', 'y') and op not in ('sq'):
        num1 = float(first)
        num2 = float(second)
    elif dec in ('no', 'n') and op not in ('sq'):
        num1 = int(first)
        num2 = int(second)
    elif dec in ('no', 'n') and op in ('sq'):
        num1 = int(first)
    elif dec in ('yes', 'y') and op in ('sq'):
        num1 = float(first)
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
    elif op in ('pmr'):
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
    againBreak = input('type "again, go, or restart" to go again, or type anything else to quit:').lower()
print("Goodbye!")    
      
      
    
      
