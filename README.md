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
PyGrype relies on an existing grype binary. [Install grype following the official instructions](https://github.com/anchore/grype#installation).

### Installation
install using `pip`
```bash
pip install pygrype
```

## Usage
Instantiate `Grype` using the default path
```python3
from pygrype import Grype
grype = Grype()
```
or specify the binary
```python3
from pygrype import Grype
grype = Grype(path='/opt/grype')
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

