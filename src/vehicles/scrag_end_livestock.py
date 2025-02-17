from road_vehicle import LivestockTramConsist
from base_platforms.trams import SteamEngineTram1


def main(roster_id):
    consist = LivestockTramConsist(
        roster_id=roster_id,
        id="scrag_end_livestock",
        base_numeric_id=710,
        name="Scrag End",
        gen=1,
    )

    consist.add_unit(base_platform=SteamEngineTram1)

    consist.add_unit(
        base_platform=None,  # no base platform by design currently
        vehicle_length=4,
        repeat=3,
    )

    return consist
