from ninja import Schema


class SumIn(Schema):
    a: int
    b: int


class SumOut(Schema):
    result: int
