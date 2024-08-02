import json
import subprocess
from typing import List

from pygrype.core.backends.base import GrypeBackendProtocol
from pygrype.core.list.db_meta_data import DBMetaData


class _GrypeDB:
    path: str

    def __init__(self, backend: GrypeBackendProtocol) -> None:
        """Initialize the _GrypeDB object.

        Args:
            backend (GrypeBackendProtocol): .
        """
        self.backend = backend

    # def check(self) -> None:
    #     """Check the status of the Grype database."""
    #     raise NotImplementedError

    def delete(self) -> int:
        """Delete the Grype database.

        Returns:
            Int: the return code of the command.
        """
        process = self.backend.execute('db', 'delete')
        return process.returncode

    # def diff(self) -> None:
    #     """Show the differences between the current and previous Grype databases."""
    #     raise NotImplementedError

    # def import_db(self) -> None:
    #     """Import the Grype database."""
    #     raise NotImplementedError

    def list(self) -> List[DBMetaData]:
        """List all available Grype databases."""
        process = self.backend.execute('db', 'list', '-o', 'json')
        data = json.loads(process.stdout)
        databases = [
            DBMetaData(
                built=db['built'],
                version=db['version'],
                url=db['url'],
                checksum=db['checksum']) for db in data]

        return databases

    # def status(self) -> None:
    #     """Show the status of the Grype database."""
    #     raise NotImplementedError

    def update(self) -> int:
        """Update the Grype database.

        Returns:
            Int: the return code of the command.
        """
        process = self.backend.execute('db', 'update')
        return process.returncode
