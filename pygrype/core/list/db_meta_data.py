from dataclasses import dataclass

from pygrype.core.decorators.to_json import to_json

@dataclass
@to_json
class DBMetaData:
    built: str
    version: int
    url: str
    checksum: str
