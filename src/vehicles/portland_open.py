from road_vehicle import OpenTramConsist, ElectricVehicleUnit


def main(roster_id):
    consist = OpenTramConsist(
        roster_id=roster_id, id="portland_open", base_numeric_id=860, name="Portland", gen=2
    )

    consist.add_unit(
        base_platform=None,  # no base platform by design currently
        type=ElectricVehicleUnit,
        vehicle_length=8,
        cargo_length=3,
        repeat=2,
    )

    return consist
