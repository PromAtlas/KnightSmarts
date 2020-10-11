from fastapi import Body, Request, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from BingHelper import BingHelper

app = FastAPI()

origins = [
    "http://localhost:3000",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def ping():
    bingHelper = BingHelper()
    temp = (bingHelper.search("university of central florida scholarships")).json()
    mappy = []
    for values in temp["webPages"]["value"]:
        mappy.append({"url" : values["url"]})
    return mappy