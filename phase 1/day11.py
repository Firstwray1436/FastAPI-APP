"""🔵 Day 11 — Setup + First FastAPI App (STRICT)
🎯 Goal

You run a FastAPI server + open /docs successfully

⚙️ Step 1 — Create project

Open terminal:

mkdir fastapi-app
cd fastapi-app
⚙️ Step 2 — Create virtual environment
python -m venv venv

Activate:
Windows:
venv\Scripts\activate
⚙️ Step 3 — Install FastAPI
pip install fastapi uvicorn
⚙️ Step 4 — Create file

Create main.py

⚙️ Step 5 — Write code (DON’T CHANGE)

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, backend started"}

⚙️ Step 6 — Run server
python -m uvicorn main:app --reload
⚙️ Step 7 — Open in browser

Go to:

👉 http://127.0.0.1:8000

👉 http://127.0.0.1:8000/docs

🧠 What you should see
/ → JSON response
/docs → Swagger UI (interactive API)
⚙️ Step 8 — Create GitHub repo
Go to GitHub → New repo → fastapi-app
Then run:
git init
git add .
git commit -m "Day 11: FastAPI setup"
git branch -M main
git remote add origin <your-repo-link>
git push -u origin main



🧠 1. git init
git init

👉 Meaning:

“Start tracking this folder with Git”

creates a hidden .git folder
Git now tracks changes in this project


🧠 2. git add .
git add .

👉 Meaning:

“Stage all files for commit”

. = everything in this folder
prepares files to be saved

Think:

“I am selecting files to include in next save point”


3. git commit -m "Day 11: FastAPI setup"
git commit -m "Day 11: FastAPI setup"

👉 Meaning:

“Create a snapshot of current code”

-m = message
message = what you did

Think:

“Save this version with a label”


🧠 4. git branch -M main
git branch -M main

👉 Meaning:

“Rename current branch to main”

Git default branch used to be master
now standard is main

Think:

“Set main working branch name”

🧠 5. git remote add origin <repo-link>
git remote add origin <repo-link>

👉 Meaning:

“Connect my local project to GitHub repo”

origin = name of remote (default)
<repo-link> = your GitHub URL

Think:

“Link my laptop code to GitHub”


🧠 6. git push -u origin main
git push -u origin main

👉 Meaning:

“Upload my code to GitHub”

origin = GitHub repo
main = branch
-u = remember this connection for future

"""
#⚙️ Full flow (simple)
#Step	Meaning
#git init	start Git
#git add .	select files
#git commit	save snapshot
#git remote	connect GitHub
#git push	upload code




from fastapi import FastAPI

app=FastAPI()    #intializing app

@app.get("/")     # get-use to request data from 
def root():       #function define
    return{"message":"hello, backend started"}  #  json responses are like dictionary always return/can return

@app.get("/items/{item_id}")     
def get_item(item_id: int):
    return{
        "item_id":item_id,
        "message":f"you requested item{item_id}"
    }

@app.get("/search")
def search_item(keyword:str,limit:int):
    return{
        "keyword":keyword,"limit":limit       
     }

