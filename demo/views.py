from ninja import Router
from demo.dtos.sum import SumIn, SumOut
from demo.usecases.sum import SumUseCase


api = Router(tags=["Demo"])


@api.get("/hello/")
def get_view(request):
    return {"message": "Hello World"}


@api.post("/sum/", response=SumOut)
def sum(request, data: SumIn):
    use_case = SumUseCase(data)

    return 200, use_case.execute()
