from dataclasses import dataclass
from typing import List, Optional

from pygrype.core.decorators.to_json import to_json

@dataclass
@to_json
class Distro:
    name: str
    version: str
    idLike: Optional[List]
