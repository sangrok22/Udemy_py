def add(n1, n2):
    return n1+n2
def sub(n1, n2):
    return n1-n2
def mul(n1, n2):
    return n1*n2
def div(n1, n2):
    return n1/n2

operations = {
    '+' : add,
    '-' : sub,
    '*' : mul,
    "/" : div
}
def calculator():
    num1 = int(input("What's the first number?: "))

    for symbol in operations:
        print(symbol)

    should_continue = True
    while should_continue:
        operations_ch = input("Pick an operation: ")
        num2 = int(input("What's the second number?: "))
        answer = operations[operations_ch](num1, num2)
        print( f"{num1} {operations_ch} {num2} = {answer}")
        
        if input(f"Type 'y' to continue with{answer}, or type 'n' to restart: ") == 'y':
            num1 = answer
        else:
            should_continue = False
            calculator()

calculator()