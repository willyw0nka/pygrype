from dataclasses import dataclass
from typing import List, Optional

from pygrype.core.decorators.to_json import to_json

@dataclass
@to_json
class MatchDetailsFound:
    vulnerabilityID: str
    versionConstraint: str
    cpes: Optional[List[str]]
