from dataclasses import dataclass
from typing import List, Optional

from pygrype.core.scan.package import Package
from pygrype.core.scan.searched_by_distro import Distro


@dataclass
class MatchDetailsSearchedBy:
    namespace: str
    cpes: Optional[List[str]]
    Package: Optional[Package]
    distro: Optional[Distro]
