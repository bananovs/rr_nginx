from fastapi import FastAPI, File
from random import randint
import os
import uvicorn

app = FastAPI()

@app.post("/")
def read_root():
    bashCommandName = 'echo $NAME'
    output = subprocess.check_output(['bash','-c', bashCommandName]) 
    return {"status_code": "200", "status": "succesful", "answer": output}

if __name__ == "__main__":
    uvicorn.run('main:app',
        host="0.0.0.0", 
        port=int(os.environ.get("PORT", 8080)),
        log_level="debug",
        http="h11",
        use_colors=True,
        workers=3
    )
