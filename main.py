from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

app = FastAPI()

# Enable CORS (so mobile or web clients can call your API)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or specify ["http://your-mobile-ip:port"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {"message": "API is running!"}


@app.post("/move")
async def receive_data(request: Request):
    data = await request.json()
    print("Received data:", data)

    return JSONResponse(content={"status": "success", "received": data})
