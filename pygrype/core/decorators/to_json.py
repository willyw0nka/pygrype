import json
from dataclasses import asdict
from typing import Type, TypeVar

T = TypeVar('T')

def to_json(cls: Type[T]) -> Type[T]:
    def to_json_func(self: T):
        return json.dumps(asdict(self))
    cls.to_json = to_json_func
    return cls
