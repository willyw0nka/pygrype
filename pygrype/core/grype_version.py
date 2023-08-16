from dataclasses import dataclass


@dataclass
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
