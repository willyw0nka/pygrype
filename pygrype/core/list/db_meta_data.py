from dataclasses import dataclass


@dataclass
class DBMetaData:
    built: str
    version: int
    url: str
    checksum: str
