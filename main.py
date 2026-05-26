from fastapi import FastAPI

app=FastAPI(title="ShopAssistent")

@app.get("/")
async def root():
    return {"message":"Wel come to shop assistent"}

def main():
    print("Hello from shopassistent!")


if __name__ == "__main__":
    main()
