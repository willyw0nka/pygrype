from dataclasses import dataclass
from typing import Optional

from pygrype.core.decorators.to_json import to_json

@dataclass
@to_json
class Location:
    path: str
    layerID: Optional[str] = None
