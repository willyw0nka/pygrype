from dataclasses import dataclass


@dataclass
class CVSSMetrics:
    baseScore: float
    exploitabilityScore: float
    impactScore: float
