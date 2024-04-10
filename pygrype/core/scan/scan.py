from dataclasses import dataclass
from typing import List

from pygrype.core.decorators.to_json import to_json
from pygrype.core.scan.distro import Distro
from pygrype.core.scan.match import Match
from pygrype.core.scan.scan_source import ScanSource

@dataclass
@to_json
class Scan:
    matches: List[Match]
    source: ScanSource
    distro: Distro
    # descriptor: GrypeScanDescriptor
