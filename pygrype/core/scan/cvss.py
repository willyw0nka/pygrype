from dataclasses import dataclass
from typing import Optional

from pygrype.core.scan.cvss_metrics import CVSSMetrics


@dataclass
class CVSS:
    source: Optional[str]
    type: Optional[str]
    version: str
    vector: str
    metrics: CVSSMetrics
