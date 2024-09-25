from demo.dtos.sum import SumIn, SumOut


class SumUseCase:
    def __init__(self, data: SumIn) -> SumOut:
        self.data = data

    def execute(self):
        result = self.data.a + self.data.b

        return SumOut(result=result)
