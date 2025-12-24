from fastapi import FastAPI
import uvicorn

from titanic.routes import router


def main():
    print("Hello from titanic!")

    app = FastAPI()

    app.include_router(router)

    uvicorn.run(app, port=10000)


if __name__ == "__main__":
    main()
