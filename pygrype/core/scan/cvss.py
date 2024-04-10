from dataclasses import dataclass
from typing import Optional

from pygrype.core.decorators.to_json import to_json
from pygrype.core.scan.cvss_metrics import CVSSMetrics


@dataclass
@to_json
class CVSS:
    source: Optional[str]
    type: Optional[str]
    version: str
    vector: str
    metrics: CVSSMetrics
