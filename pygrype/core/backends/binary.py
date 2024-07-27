import shutil
from subprocess import CompletedProcess

from pygrype.core.backends.base import execute
from pygrype.core.exceptions import GrypeNotAvailableException
from pygrype.logging import get_logger

logger = get_logger()


class GrypeBinaryBackend:
    def __init__(self, binary_path: str = 'grype') -> None:
        self._binary_path = binary_path

    def ensure_backend(self) -> None:
        if not shutil.which(self._binary_path):
            err = f'Grype was not found at: {self._binary_path}'
            logger.error(err)
            raise GrypeNotAvailableException(err)

    @property
    def executable_string(self) -> str:
        return self._binary_path

    def execute(self, *args) -> CompletedProcess:
        return execute(self.executable_string, *args)
