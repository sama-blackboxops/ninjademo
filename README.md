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
