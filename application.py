from fastapi import FastAPI

from api.authors.views import router as authors_router

app = FastAPI()
app.include_router(authors_router)


@app.get('/')
async def root():
    return {
        "application": "Library API",
        "version": 0.0,
    }
