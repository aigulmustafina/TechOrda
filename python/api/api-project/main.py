from fastapi import FastAPI, HTTPException, Header
from pydantic import BaseModel
import prometheus_client
from prometheus_client import Counter, Histogram, Gauge, generate_latest, REGISTRY

app = FastAPI()
metrics_app = prometheus_client.make_asgi_app()
app.mount("/metrics", metrics_app)

elements_list = []

c = Counter("http_requests_total", "Number of HTTP requests received", ["method", "endpoint"])
h = Histogram("http_requests_milliseconds", "Duration of HTTP requests in milliseconds", ["method", "endpoint"])
gsum = Gauge("last_sum_n", "Value stores last result of sum_n")  
gfibo = Gauge("last_fibo", "Value stores last result of Fibonacci sequence")
gsize = Gauge("list_size", "Value stores current list size")
gcalc = Gauge("last_calculator", "Value stores last result of calculator")
ccalc = Counter("errors_calculator_total", "Number of errors in calculator")

def sanitize_endpoint(endpoint: str) -> str:
    return endpoint.replace("/", "_").replace("-", "_")

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/sum1n/{n}")
def get_sum1n(n: int):
    total_sum = 0
    sanitized_endpoint = sanitize_endpoint(f"/sum1n/{n}")
    c.labels(method="GET", endpoint=sanitized_endpoint).inc()
    h.labels(method="GET", endpoint=sanitized_endpoint).observe(0.2)
    for i in range(1, n + 1):
        total_sum += i
    gsum.set(total_sum)
    return f"result: {total_sum}"

@app.get("/fibo")
def get_fibo(n: int):
    fib1, fib2 = 0, 1
    for i in range(n - 2):
        fib1, fib2 = fib2, fib1 + fib2
    sanitized_endpoint = sanitize_endpoint(f"/fibo/{n}")
    c.labels(method="GET", endpoint=sanitized_endpoint).inc()
    h.labels(method="GET", endpoint=sanitized_endpoint).observe(0.2)
    gfibo.set(fib2)
    return f"{n}-th number in Fibonacci sequence is {fib2}"

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
    sanitized_endpoint = sanitize_endpoint("/list")
    c.labels(method="GET", endpoint=sanitized_endpoint).inc()
    h.labels(method="GET", endpoint=sanitized_endpoint).observe(0.2)
    gsize.set(len(elements_list))
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
            result = int(num1) * int(num2)
        else:
            raise TypeError('Invalid operator')

        return result
    except (ValueError, ZeroDivisionError) as e:
        raise e

@app.post("/calculator")
def calculator(item: Expression):
    expression = item.expr
    sanitized_endpoint = sanitize_endpoint("/calculator")
    c.labels(method="GET", endpoint=sanitized_endpoint).inc()
    h.labels(method="GET", endpoint=sanitized_endpoint).observe(0.2)

    try:
        result = calculate(expression)
        gcalc.set(result)
        return f"result: {result}"
    except ZeroDivisionError:
        ccalc.inc()
        raise HTTPException(status_code=403, detail="zerodiv")
    except ValueError:
        ccalc.inc()
        raise HTTPException(status_code=400, detail="invalid")
