from fastapi import FastAPI, HTTPException, Header
from pydantic import BaseModel

app = FastAPI()

elements_list = []

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/sum1n")
def get_sum1n(n:int):
    total_sum = 0
    for i in range(1, n+1):
        total_sum += i
    return f"result: {total_sum}" 

@app.get("/fibo")
def get_fibo(n:int):
    fib1, fib2 = 0, 1  
    for i in range(n - 2):  
        fib1, fib2 = fib2, fib1 + fib2
    return f"{n}-th number in Fibonacchi sequence is {fib2}"

@app.post("/reverse")
def reverse_str(string: str = Header()):
    return f"Reversed {string} is {''.join(reversed(list(string)))}"

class Element(BaseModel):
    element: str

class Expression(BaseModel):
    expr: str

@app.put("/list")
def update_list(item: Element):
    elements_list.append(item.element)

@app.get("/list")
def get_list():
    return elements_list

def calculate(expression: str):
    expr_parts = expression.split(',')
    num1, operator, num2 = expr_parts[0], expr_parts[1], expr_parts[2]
    result = 0
    try: 
        if operator == '+':
            result = int(num1) + int(num2)
        elif operator == "-":
            result = int(num1) - int(num2)
        elif operator == '/':
            result = int(num1) / int(num2)
        elif operator == '*':
            result == int(num1) * int(num2)
        else:
            raise TypeError('Invalid operator')
        
        return result
    except (ValueError, ZeroDivisionError) as e:
        raise e
    


@app.post("/calculator")
def calculator(item: Expression):
    expression = item.expr

    try:
        result = calculate(expression)
        return f"result: {result}"
    except ZeroDivisionError:
        raise HTTPException(status_code=403, detail="zerodiv")
    except ValueError:
        raise HTTPException(status_code=400, detail="invalid")
    

    