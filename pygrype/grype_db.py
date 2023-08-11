import subprocess

class _GrypeDB:
    path: str

    def __init__(self, path: str) -> None:
        self.path = path

    def check(self) -> None:
        pass

    def delete(self) -> None:
        subprocess.run(
            args=[self.path, 'db', 'delete'],
            capture_output=True)

    def diff(self) -> None:
        pass

    def import_db(self) -> None:
        pass

    def list(self) -> None:
        pass

    def status(self) -> None:
        pass

    def update(self) -> None:
        subprocess.run(
            args=[self.path, 'db', 'update'],
            capture_output=True)
