from fastapi import FastAPI
from api.events.routing import router as events_router

app = FastAPI()


app.include_router(events_router, prefix="/events", tags=["events"])


@app.get("/")
def read_root():
    return {"Hello": "World"}
