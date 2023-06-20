def calculation(num1, num2, operator):
    if operator == "ADD":
        result = float(num1) + float(num2)
        print(f"{num1} + {num2} = {result}")
        return result
    elif operator == "SUB":
        result = float(num1) - float(num2)
        print(f"{num1} - {num2} = {result}")
        return result
    elif operator == "MUL":
        result = float(num1) * float(num2)
        print(f"{num1} * {num2} = {result}")
        return result
    elif operator == "DIV":
        result = float(num1) / float(num2)
        print(f"{num1} / {num2} = {result}")
        return result
    else:
        print("Operator is incorrect")