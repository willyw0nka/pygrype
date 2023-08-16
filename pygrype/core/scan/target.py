from dataclasses import dataclass
from typing import List

from pygrype.core.scan.layer import Layer


@dataclass
class Target:
    userInput: str
    imageID: str
    manifestDigest: str
    mediaType: str
    tags: List[str]
    imageSize: int
    layers: List[Layer]
    manifest: str
    config: str
    repoDigests: List[str]
    architecture: str
    os: str
