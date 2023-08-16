from dataclasses import dataclass

from pygrype.core.scan.match_details_found import MatchDetailsFound
from pygrype.core.scan.match_details_searched_by import MatchDetailsSearchedBy


@dataclass
class MatchDetails:
    type: str
    matcher: str
    searchedBy: MatchDetailsSearchedBy
    found: MatchDetailsFound
