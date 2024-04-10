from dataclasses import dataclass

from pygrype.core.decorators.to_json import to_json

@dataclass
@to_json
class CVSSMetrics:
    baseScore: float
    exploitabilityScore: float
    impactScore: float
