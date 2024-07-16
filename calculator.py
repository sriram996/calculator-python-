def add(a,b):
    print(a+b);
def subtract(a,b):
    print(max(a,b)-min(a,b));
def multiply(a,b):
    print(a*b);
def division(a,b):
    print(a/b);
def power(a,b):
    print(a**b);
def integer_division(a,b):
    print(a//b);
def remainder(a,b):
    print(a%b);
while True:
    print('----CALCULATOR------');
    print('CHOOSE ANY ONE OPERATION');
    print('\n1. ADDITION');
    print('\n2. SUBTRACTION');
    print('\n3. MULTIPLICATION');
    print('\n4. DIVISION');
    print('\n5. EXPONENTIAL');
    print('\n6. APPROXIMATE DIVISION');
    print('\n7. DIVISON(REMAINDER)');
    print('\n8. EXIT\n');
    
    c=int(input('Enter ur choice: '))
    if(c==1):
        a=int(input('enter first number: '));
        b=int(input('enter second number: '));
        add(a,b);
        
    elif(c==2):
        a=int(input('enter first number: '));
        b=int(input('enter second number: '));
        subtract(a,b);
        
    elif(c==3):
        a=int(input('enter first number: '));
        b=int(input('enter second number: '));
        multiply(a,b);
        
    elif(c==4):
        a=int(input('enter first number: '));
        b=int(input('enter second number: '));
        division(a,b);
        
    elif(c==5):
        a=int(input('enter first number: '));
        b=int(input('enter second number: '));
        power(a,b);
        
    elif(c==6):
        a=int(input('enter first number: '));
        b=int(input('enter second number: 