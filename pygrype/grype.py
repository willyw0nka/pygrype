import json
import logging
import shutil
import subprocess
from typing import Dict, List

from pygrype.grype_db import _GrypeDB


class Grype:
    """A class representing the Grype vulnerability scanner."""

    path: str
    db: _GrypeDB

    def __init__(self, path: str = 'grype') -> None:
        """Initialize the Grype object.

        Args:
            path (str, optional): The path to the Grype executable. Defaults to 'grype'.
        
        Raises:
            Exception: If Grype is not found at the specified path.
        """
        if not shutil.which(path):
            logging.error(f'Grype was not found at: {path}')
            raise Exception(f'Grype was not found at: {path}')
        self.path = path
        self.db = _GrypeDB(self.path)

        version = self.version()['version']
        logging.info(f'Using Grype {version}')

    def version(self) -> Dict:
        """Get the version of Grype.

        Returns:
            Dict: A dictionary containing the version information.
        """
        c = subprocess.run(
            args=[self.path, 'version', '--output', 'json'],
            capture_output=True)        
        return json.loads(c.stdout)

    def scan(self, target: str, add_cpes_if_none: bool = False, by_cve: bool = False, config: str = None, distro: str = None, exclude: List[str] = None,
             fail_on: str = None, file: str = None, name: str = None, only_fixed: bool = False, only_notfixed: bool = False, platform: str = None,
             scope: str = None, show_supressed: bool = False) -> Dict:
        """Scan a target for vulnerabilities using Grype.

        Args:
            target (str): The target to scan.
            add_cpes_if_none (bool, optional): Whether to add Common Platform Enumerations (CPEs) if none are found. Defaults to False.
            by_cve (bool, optional): Whether to group vulnerabilities by CVE. Defaults to False.
            config (str, optional): The path to the Grype configuration file. Defaults to None.
            distro (str, optional): The target distribution. Defaults to None.
            exclude (List[str], optional): A list of vulnerability IDs to exclude. Defaults to None.
            fail_on (str, optional): The severity level at which to fail the scan. Defaults to None.
            file (str, optional): The path to the file containing the target. Defaults to None.
            name (str, optional): The name of the target. Defaults to None.
            only_fixed (bool, optional): Whether to only show fixed vulnerabilities. Defaults to False.
            only_notfixed (bool, optional): Whether to only show vulnerabilities that are not fixed. Defaults to False.
            platform (str, optional): The target platform. Defaults to None.
            scope (str, optional): The scope of the scan. Defaults to None.
            show_supressed (bool, optional): Whether to show suppressed vulnerabilities. Defaults to False.

        Returns:
            Dict: A dictionary containing the scan results.
        """
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
