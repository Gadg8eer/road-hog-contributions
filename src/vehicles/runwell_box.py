from road_vehicle import BoxTruckConsist
from base_platforms.trucks import SteamCaboverSemiTractorTruckGen2A


def main(roster_id):
    consist = BoxTruckConsist(
        roster_id=roster_id,
        id="runwell_box",
        base_numeric_id=890,
        name="Runwell",
        gen=2,
    )

    consist.add_unit(base_platform=SteamCaboverSemiTractorTruckGen2A)

    consist.add_unit(base_platform=None, vehicle_length=5)

    return consist
