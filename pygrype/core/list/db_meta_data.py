from dataclasses import dataclass


@dataclass
@to_json
class DBMetaData:
    built: str
    version: int
    url: str
    checksum: str
