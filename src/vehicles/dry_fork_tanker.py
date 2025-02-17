from road_vehicle import TankerFeldbahnConsist
from base_platforms.feldbahn import DieselEngineFeldbahnGen3A, WagonFeldbahnA


def main(roster_id):
    consist = TankerFeldbahnConsist(
        roster_id=roster_id,
        id="dry_fork_tanker",
        base_numeric_id=1150,
        name="Dry Fork",
        gen=3,
    )

    consist.add_unit(base_platform=DieselEngineFeldbahnGen3A)

    consist.add_unit(base_platform=WagonFeldbahnA, repeat=5)

    return consist
