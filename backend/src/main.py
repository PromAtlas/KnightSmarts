from fastapi import Body, Request, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from BingHelper import BingHelper
from CollegeHelper import CollegeHelper

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
def resource():
    query = "university of central florida"
    bingHelper = BingHelper()
    collegeHelper = CollegeHelper()
    
    school = collegeHelper.get_school_json(query)
    temp = (bingHelper.search(f"{query} scholarships")).json()
    
    mappy = []
    mappy.append(school["name"])
    mappy.append(school["price"])

    for values in temp["webPages"]["value"]:
        mappy.append({"url" : values["url"]})
    
    return mappy