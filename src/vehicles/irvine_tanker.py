from road_vehicle import TankerFeldbahnConsist
from base_platforms.feldbahn import SteamEngineFeldbahnGen2B, WagonFeldbahnA


def main(roster_id):
    consist = TankerFeldbahnConsist(
        roster_id=roster_id,
        id="irvine_tanker",
        base_numeric_id=1130,
        name="Irvine",
        gen=3,
    )

    consist.add_unit(base_platform=SteamEngineFeldbahnGen2B)

    consist.add_unit(base_platform=WagonFeldbahnA, repeat=12)

    return consist
