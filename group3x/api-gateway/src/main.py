from typing import Optional

import services
from fastapi import Body, FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# root
@app.get("/")
def root() -> JSONResponse:
    return JSONResponse(status_code=200, content={"test": "system is running 🥳"})


# books
@app.get("/books")
async def get_books() -> JSONResponse:
    books: Optional[list] = services.get_books()
    return JSONResponse(status_code=200, content=books)


# book/{id}
@app.get("/book/{id}")
async def get_book(id: int = 0) -> JSONResponse:
    book: Optional[dict] = services.get_book_by_id(id)
    return JSONResponse(status_code=200, content=book)


# book
@app.post("/book")
async def input(body: dict = Body(...)) -> JSONResponse:
    new_id: int = services.add_book(body)
    return JSONResponse(status_code=201, content=jsonable_encoder({"new_book_id": new_id}))


# bundesland/{name}
@app.get("/bundesland/{name}")
async def get_bundesland(name: str = "") -> JSONResponse:
    bundesland: Optional[dict] = services.get_bundesland_by_name(name)
    return JSONResponse(status_code=200, content=bundesland)