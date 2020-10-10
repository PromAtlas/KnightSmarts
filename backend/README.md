Enter this into the commandline: 

Install pipenv
```
pip install pipenv
pipenv shell
pip install -r requirements.txt
```

To run the project
```
cd src/
uvicorn main:app --reload
```