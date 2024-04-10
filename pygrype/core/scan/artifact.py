from dataclasses import dataclass
from typing import List

from pygrype.core.decorators.to_json import to_json
from pygrype.core.scan.location import Location
from pygrype.core.scan.upstream import Upstream


@dataclass
@to_json
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
