from fastapi import Body, Request, FastAPI
from fastapi.middleware.cors import CORSMiddleware
import json
from BingHelper import BingHelper
from CollegeHelper import CollegeHelper

app = FastAPI()

origins = [
    'null',
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
def resource(query):
    bingHelper = BingHelper()
    collegeHelper = CollegeHelper()
    
    school = collegeHelper.get_school_json(query)
    temp = (bingHelper.search(f"{query} scholarships")).json()
    
    mappy = []
    mappy.append({"name": school["name"]})
    mappy.append({"price": school["price"]})

    for values in temp["webPages"]["value"]:
        mappy.append({"url" : values["url"]})
    
    return mappy