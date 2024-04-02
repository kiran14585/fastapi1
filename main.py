from fastapi import FastAPI
from fastapi.responses import HTMLResponse



app =  FastAPI()

@app.get("/")
def test():
    return "<h1 style='color:blue'>Happy birthday Shabeeb!</h1>"

    

    
