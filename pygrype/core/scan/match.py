from dataclasses import dataclass
from typing import List

from pygrype.core.scan.artifact import Artifact
from pygrype.core.scan.match_details import MatchDetails
from pygrype.core.scan.vulnerability import Vulnerability


@dataclass
class Match:
    vulnerability: Vulnerability
    relatedVulnerabilities: List[Vulnerability]
    matchDetails: List[MatchDetails]
    artifact: Artifact
