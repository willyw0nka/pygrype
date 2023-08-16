from dataclasses import dataclass
from typing import List


@dataclass
class Distro:
    name: str
    version: str
    idLike: List
