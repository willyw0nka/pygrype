from dataclasses import dataclass
from typing import Optional

@dataclass
class Location:
    path: str
    layerID: Optional[str] = None
