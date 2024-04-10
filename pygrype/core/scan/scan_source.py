from dataclasses import dataclass
from typing import Union

from pygrype.core.scan.target import Target


@dataclass
class ScanSource:
    type: str
    target: Union[Target, str]
