from dataclasses import dataclass

from pygrype.core.scan.target import Target


@dataclass
class ScanSource:
    type: str
    target: Target
