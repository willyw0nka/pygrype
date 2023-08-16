from dataclasses import dataclass
from typing import List

from pygrype.core.scan.location import Location
from pygrype.core.scan.upstream import Upstream


@dataclass
class Artifact:
    id: str
    name: str
    version: str
    type: str
    locations: List[Location]
    language: str
    licenses: List[str]
    cpes: List[str]
    purl: str
    upstreams: List[Upstream]
