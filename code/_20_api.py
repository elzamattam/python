import fastapi
import uvicorn

app = fastapi.FastAPI()

@app.get('/ping')
def ping():
    return { "message": "Ping successful" }

uvicorn.run(app, host='localhost', port=1000)


# https://localhost:1000/ping