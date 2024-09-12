from typing import Union
from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

# query params
# @app.get('/query') # http://127.0.0.1:8000/query?limit=10&view=true
# def read_query(limit, view): # tidakada nilai default, jadi jika query tidak dimasukan ( http://127.0.0.1:8000/query) akan error

#     if view:
#         return {f'you have limit {limit} on view'}
#     else:
#         return {f'you have limit {limit}'}

# query params
# @app.get('/query') # http://127.0.0.1:8000/query?limit=10&view=true
# def read_query(limit=10, view:bool=True): # diberi nilai default

#     if view:
#         return {f'you have limit {limit} on view'}
#     else:
#         return {f'you have limit {limit}'}

# query params menggunakan optional
@app.get('/query') # http://127.0.0.1:8000/query?limit=10&view=true
def read_query(limit=10, view:bool=True, sort: Optional[str] = None): # diberi nilai default

    if view:
        return {f'you have limit {limit} on view'}
    else:
        return {f'you have limit {limit}'}


# by id
@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}



class Item(BaseModel):
    title: str
    body: str
    published_at: Optional[bool]

# create data
@app.post('/items')
def crate_item(item:Item):
    return{'data': f"items is created with title is {item.title}"}

# mengubah alamat url/port
# if __name__ == '__main__':
#     uvicorn.run(app, host='localhost', port=2024)
