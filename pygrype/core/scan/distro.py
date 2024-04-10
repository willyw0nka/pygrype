from dataclasses import dataclass
from typing import List, Optional


@dataclass
class Distro:
    name: str
    version: str
    idLike: Optional[List]
