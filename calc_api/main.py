from fastapi import FastAPI, Form, HTTPException, Request, Header
import calculator

app = FastAPI()

@app.post("/calculate")
def calculate(
    request: Request,
    Operation: str = Form(...),
    Data_A: float = Form(...),
    Data_B: float = Form(...),
    x_token: str | None = Header(default = None),
):
    print("Content-Type:", request.headers.get("content-type"))
    print("X-Token:", x_token)
    try:
        result = calculator.calculate(Operation, Data_A, Data_B)
    except ZeroDivisionError as exc:
        raise HTTPException(status_code = 400, detail = str(exc))
    except ValueError as exc:
        raise HTTPException(status_code = 400, detail = str(exc))
    return {"Result": round(result, 4)}

