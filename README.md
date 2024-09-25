# Django Ninja Demo App
This is a demo app to show how to use Django Ninja to build a web API.

## How to write views
You can write views using only a function approach.

```python
from ninja import Router

api = Router(tags=["Demo"])

@api.get("/hello/")
def get_view(request):
    return {"message": "Hello World"}

```

## What are dtos?
DTOs are Data Transfer Objects. They are used to define the input/output structure of the API. They are what you call
serializer in Django Rest Framework. They use pydantic internally to define the structure which means they are
performant, and gives us validation for free.

```python
from ninja import Schema
from typing import Optional
from ninja import Router

class ItemIn(Schema):
    name: str
    description: Optional[str] = None
    price: float
    quantity: int

class ItemOut(Schema):
    name: str
    description: str = None
    price: float
    quantity: int


app = Router()

@app.post("/items/", response=ItemOut)
def create_item(request, item: ItemIn):
    itemout = usecase.execute(item)
    return 200, itemout
```

In the above example, `ItemIn` is used to define the input structure of the API, and `ItemOut` is used to define the output of the endpoint.


## What are Usecases?
Usecases are the business logic of the application. They are used to define the business logic of the application. They also go by the name of services in Django Rest Framework.

Ideologically, the controller/view should be as thin as possible and should only be used to handle the request and response. The business logic should be handled by the usecases.

```python
from ninja import Schema
from typing import Optional
from ninja import Router

class ItemIn(Schema):
    name: str
    description: Optional[str] = None
    price: float
    quantity: int

class ItemOut(Schema):
    name: str
    description: str = None
    price: float
    quantity: int

class ItemUsecase:
    def __init__(self, item: ItemIn):
        self.item = item

    def execute(self) -> ItemOut:
        # do some business logic
        return ItemOut(**self.item.dict())

app = Router()



@app.post("/items/", response=ItemOut)
def create_item(request, item: ItemIn):
    usecase = ItemUsecase(item)

    itemout = usecase.execute(item)
    return 200, itemout
```

In the above example, `ItemUsecase` is used to define the business logic of the application and `ItemIn` and `ItemOut` are used to define the input and output structure of the API.
