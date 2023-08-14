import subprocess

class _GrypeDB:
    path: str

    def __init__(self, path: str) -> None:
        """Initialize the _GrypeDB object.

        Args:
            path (str): The path to the Grype executable.
        """
        self.path = path

    # def check(self) -> None:
    #     """Check the status of the Grype database."""
    #     raise NotImplementedError

    def delete(self) -> int:
        """Delete the Grype database.

        Returns:
            Int: the return code of the command.
        """
        process = subprocess.run(
            args=[self.path, 'db', 'delete'],
            capture_output=True)
        return process.returncode

    # def diff(self) -> None:
    #     """Show the differences between the current and previous Grype databases."""
    #     raise NotImplementedError

    # def import_db(self) -> None:
    #     """Import the Grype database."""
    #     raise NotImplementedError

    # def list(self) -> None:
    #     """List all available Grype databases."""
    #     raise NotImplementedError

    # def status(self) -> None:
    #     """Show the status of the Grype database."""
    #     raise NotImplementedError

    def update(self) -> int:
        """Update the Grype database.

        Returns:
            Int: the return code of the command.
        """
        process = subprocess.run(
            args=[self.path, 'db', 'update'],
            capture_output=True)
        return process.returncode
