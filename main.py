from fastapi import FastAPI

app = FastAPI()

# path -> WHERE
# query -> HOW

@app.get("/")
async def root():
    return {"message": "Hello World"}