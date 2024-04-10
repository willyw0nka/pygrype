from dataclasses import dataclass
from typing import List, Optional

from pygrype.core.decorators.to_json import to_json
from pygrype.core.scan.package import Package
from pygrype.core.scan.searched_by_distro import Distro

@dataclass
@to_json
class MatchDetailsSearchedBy:
    namespace: str
    cpes: Optional[List[str]]
    Package: Optional[Package]
    distro: Optional[Distro]
