from road_vehicle import MetalHEQSBase, DieselVehicleUnit


def main(roster_id):
    consist = MetalHEQSBase(
        roster_id=roster_id,
        id="steeraway_metal",
        base_numeric_id=520,
        name="Steeraway",
        power=500,
        speed=45,
        gen=3,
        intro_date_offset=10,
    )  # introduce later than gen epoch by design

    consist.add_unit(
        base_platform=None,  # no base platform by design currently
        type=DieselVehicleUnit,
        capacity=0,
        vehicle_length=6,
    )

    consist.add_unit(
        base_platform=None,  # no base platform by design currently
        # capacity=50,
        vehicle_length=7,
        repeat=2,
    )

    return consist
