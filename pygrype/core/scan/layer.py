from dataclasses import dataclass

from pygrype.core.decorators.to_json import to_json

@dataclass
@to_json
class Layer:
    mediaType: str
    digest: str
    size: int
