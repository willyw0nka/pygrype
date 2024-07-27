import subprocess
from os import PathLike
from subprocess import CompletedProcess
from typing import Protocol, Union


class GrypeBackendProtocol(Protocol):

    def ensure_backend(self) -> None:
        ...

    @property
    def executable_string(self) -> str:
        ...

    def execute(self, *args) -> CompletedProcess:
        ...


def execute(executable_string: Union[str, bytes, PathLike], *args) -> CompletedProcess:
    return subprocess.run(
        args=[executable_string, *args],
        capture_output=True
    )
