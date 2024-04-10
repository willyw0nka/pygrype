from dataclasses import dataclass

from pygrype.core.decorators.to_json import to_json

@dataclass
@to_json
class GrypeVersion:
    version: str
    syft_version: str
    git_commit: str
    git_description: str
    build_date: str
    go_version: str
    compiler: str
    platform: str
    application: str
    supported_db_schema: int
