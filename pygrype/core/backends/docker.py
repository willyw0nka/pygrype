import subprocess
from subprocess import CompletedProcess

from pygrype.core.backends.base import execute

DOCKER_EXE = 'docker'
IMAGE_NAME = 'anchore/grype'


class GrypeDockerBackend:

    def __init__(self, tag: str = "latest") -> None:
        self.tag: str = tag
        super().__init__()

    @property
    def docker_image(self) -> str:
        return f"{IMAGE_NAME}:{self.tag}"

    def ensure_backend(self) -> None:
        try:
            # Check if Docker is installed
            subprocess.run(
                [DOCKER_EXE, '--version'],
                check=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )
        except subprocess.CalledProcessError:
            raise Exception("Docker is not installed or not available in the PATH.")

        try:
            # Ensure the required Docker image is available
            subprocess.run(
                [DOCKER_EXE, 'pull', self.docker_image],
                check=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )
        except subprocess.CalledProcessError:
            raise Exception(f"Failed to pull the required Docker image '{self.docker_image}'.")

    @property
    def executable_string(self) -> str:
        return DOCKER_EXE

    def execute(self, *args) -> CompletedProcess:
        docker_args = ['run', '--rm', '-e', 'GRYPE_DB_CACHE_DIR=/var/tmp/', '-v',
                       '/var/run/docker.sock:/var/run/docker.sock', '-v', '/var/tmp/grype_cache:/var/tmp/',
                       self.docker_image] + list(args)

        return execute(self.executable_string, *docker_args)
