from dataclasses import dataclass


@dataclass
class Layer:
    mediaType: str
    digest: str
    size: int
