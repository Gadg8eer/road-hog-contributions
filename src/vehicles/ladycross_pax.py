from road_vehicle import PaxLocalTramConsist
from base_platforms.trams import SteamEngineTram2


def main(roster_id):
    consist = PaxLocalTramConsist(
        roster_id=roster_id,
        id="ladycross_pax",
        base_numeric_id=0,
        name="Ladycross",
        gen=1,
    )

    consist.add_unit(base_platform=SteamEngineTram2)

    consist.add_unit(
        base_platform=None,  # pax trams have no base platform by design currently
        vehicle_length=4,
        repeat=3,
    )

    return consist
