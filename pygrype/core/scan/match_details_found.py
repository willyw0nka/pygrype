from dataclasses import dataclass
from typing import List, Optional


@dataclass
class MatchDetailsFound:
    vulnerabilityID: str
    versionConstraint: str
    cpes: Optional[List[str]]
