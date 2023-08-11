import json
import logging
import shutil
import subprocess
from typing import Dict, List

from pygrype.grype_db import _GrypeDB

class Grype:
    path: str
    db: _GrypeDB

    def __init__(self, path: str = 'grype') -> None:
        if not shutil.which(path):
            logging.error(f'Grype was not found at: {path}')
            raise Exception(f'Grype was not found at: {path}')
        self.path = path
        self.db = _GrypeDB(self.path)

        version = self.version()['version']
        logging.info(f'Using Grype {version}')

    def version(self) -> Dict:
        c = subprocess.run(
            args=[self.path, 'version', '--output', 'json'],
            capture_output=True)        
        return json.loads(c.stdout)

    def scan(self, target: str, add_cpes_if_none: bool = False, by_cve: bool = False, config: str = None, distro: str = None, exclude: List[str] = None,
             fail_on: str = None, file: str = None, name: str = None, only_fixed: bool = False, only_notfixed: bool = False, platform: str = None,
             scope: str = None, show_supressed: bool = False) -> Dict:
        
        args = [self.path, target, '--output', 'json']

        if add_cpes_if_none:
            args.append('--add-cpes-if-none')
        if by_cve:
            args.append('--by-cve')
        if config:
            args += ['--config', config]
        if distro:
            args += ['--distro', distro]
        if exclude:
            args += ['--exclude', ','.join(exclude)]
        if fail_on:
            args += ['--fail-on', fail_on]
        if file:
            args += ['--file', file]
        if name:
            args += ['--name', name]
        if only_fixed:
            args.append('--only-fixed')
        if only_notfixed:
            args.append('--only-notfixed')
        if platform:
            args += ['--platform', platform]
        if scope:
            args += ['--scope', scope]
        if show_supressed:
            args.append('--show-supressed')

        logging.debug(f'Running: {args}')

        c = subprocess.run(
            args=args,
            capture_output=True
        )
        return json.loads(c.stdout)


g = Grype(path='grype')

g.db.update()
print('done')
s = g.scan(target='alpine', only_fixed=True)
print(s)
