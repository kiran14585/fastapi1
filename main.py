from fastapi import FastAPI


app =  FastAPI()

@app.get("/")
def test():
    
    return "<h1 style='color:blue'>Happy birthday Shabeeb!</h1>"

    
