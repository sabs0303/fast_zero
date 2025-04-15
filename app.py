# fast
from fastapi import FastAPI

app = FastAPI()


@app.get('/')  # raiz do site
def read_root():
    return {'message': 'Olha o Pamonheiro!'}
