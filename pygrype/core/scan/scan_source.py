from dataclasses import dataclass
from typing import Union

from pygrype.core.decorators.to_json import to_json
from pygrype.core.scan.target import Target


@dataclass
@to_json
class ScanSource:
    type: str
    target: Union[Target, str]
