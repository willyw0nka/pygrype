# PyGrype
A python wrapper for Grype

![PyPI](https://img.shields.io/pypi/v/pygrype)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/pygrype)
![PyPI - License](https://img.shields.io/pypi/l/pygrype)


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

## Installation
install using `pip`

```bash
pip install pygrype
```

## Usage
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

