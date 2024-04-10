from dataclasses import dataclass


@dataclass
@to_json
class CVSSMetrics:
    baseScore: float
    exploitabilityScore: float
    impactScore: float
