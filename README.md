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
    - [ ] list
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
from pygrype.grype import Grype
grype = Grype()
```
or specify the binary
```python3
from pygrype.grype import Grype
grype = Grype(path='/opt/grype')
```

## Full example
```python3
from pygrype.grype import Grype

image = 'alpine:3.12'
grype = Grype('/opt/grype')

version = grype.version()
print('Using Grype version {version}'.format(version=version['version']))

print('Updating DB...')
grype.db.update()

scan = grype.scan(image)
print('Image {image} has {matches} vlunerabilities'.format(
    image=image,
    matches=len(scan['matches'])))
```

