# PyGrype

![PyPI](https://img.shields.io/pypi/v/pygrype)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/pygrype)
![PyPI - License](https://img.shields.io/pypi/l/pygrype)

A python wrapper for [Anchore Grype](https://github.com/anchore/grype)

## Status
Supported commands

- [ ] ~~completion~~
- [x] db
    - [ ] check
    - [x] delete
    - [ ] diff
    - [ ] import
    - [x] list
    - [ ] status
    - [x] update
- [ ] ~~help~~
- [x] scan
- [x] version

## Getting started
### Prerequisites
PyGrype relies on either an existing grype binary, or a local Docker install.

[Install grype binary following the official instructions](https://github.com/anchore/grype#installation).

[Install Docker following the official instructions](https://docs.docker.com/get-docker/)

### Installation
install using `pip`
```bash
pip install pygrype
```

## Usage

Pygrype is wrapper around the `grype` binary, and can be used in two ways: using a local binary, or using the official Docker container.

### Using Local Binary
Instantiate `Grype` without any arguments. This will use the default binary backend, and will look for the `grype` binary in the system path.

```python3
from pygrype import Grype
grype = Grype()
```
or specify the binary
```python3
from pygrype import Grype, GrypeBinaryBackend
binary_backend = GrypeBinaryBackend(path='/opt/grype')
grype = Grype(backend=binary_backend)
```

### Using Docker
Instantiate `Grype` with the `GrypeDockerBackend` backend. This will use the [official grype Docker container](https://hub.docker.com/r/anchore/grype) to run scans. The backend will use the latest version of the container by default, but you can specify a specific version using the optional `tag` argument.

```python3
from pygrype import Grype, GrypeDockerBackend
docker_backend = GrypeDockerBackend(tag="v0.79.2")
grype = Grype(backend=docker_backend)
```

## Full example
```python3
from pygrype import Grype

grype = Grype()

version_info = grype.version()

print(f'Using grype {version_info.version}')

images = [
    'alpine:3.12',
    'ubuntu:18.04',
    'debian:9'
]

for image in images:
    scan = grype.scan(image)
    criticals = len(list(filter(lambda x: x.vulnerability.severity.lower() == 'critical', scan.matches)))
    print(f'{image} has {len(scan.matches)} vulnerabilities ({criticals} critical)')
```
Example output
```
Using grype 0.62.3
alpine:3.12 has 23 vulnerabilities (3 critical)
ubuntu:18.04 has 18 vulnerabilities (0 critical)
debian:9 has 213 vulnerabilities (23 critical)
```

