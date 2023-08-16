from pygrype import Grype
from pygrype.core.grype_version import GrypeVersion


def test_version():
    grype = Grype()
    version_info = grype.version()

    assert type(version_info) is GrypeVersion
