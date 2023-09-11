from road_vehicle import BoxTruckConsist
from base_platforms.trucks import DieselConventionalCabSemiTractorTruckGen4A


def main(roster_id):
    consist = BoxTruckConsist(
        roster_id=roster_id,
        id="quickset_box",
        base_numeric_id=350,
        name="Quickset",
        gen=4,
    )

    consist.add_unit(base_platform=DieselConventionalCabSemiTractorTruckGen4A)

    consist.add_unit(base_platform=None, vehicle_length=7)

    return consist
