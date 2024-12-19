import mlflow


def calculator(a,b,operator=None):
    if operator == "add":
        return a + b
    if operator == "subtract":
        return a - b
    if operator == "multiply":
        return a * b
    if operator == "divide":
        if b!= 0:
            return a / b
        else:
            raise ValueError("Cannot divide by zero")
    else:
        raise ValueError("Invalid operator. Supported operators are 'add','subtract','multiply', 'divide'")


if __name__ == "__main__":
    a, b, opt = 100, 200, 'subtract'
    with mlflow.start_run():
        result = calculator(a, b, opt)
        print("The result is {}".format(result))
        mlflow.log_param("a", a)
        mlflow.log_param("b", b)
        mlflow.log_param("operator", opt)
        mlflow.log_metric("result", result)

        # $ mlflow ui
   
    