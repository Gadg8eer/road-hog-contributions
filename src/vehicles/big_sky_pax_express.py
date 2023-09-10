from road_vehicle import PaxExpressCoachConsist, DieselVehicleUnit

# !! unused ??
# for each generation, bus and coach variants have same power and intro date
# coaches faster, lower capacity than equivalent bus


def main(roster_id):
    consist = PaxExpressCoachConsist(
        roster_id=roster_id,
        id="big_sky_pax_express",
        base_numeric_id=620,
        name="Big Sky",
        power=220,
        speed=90,
        gen=4,
        intro_date=1990,
    )

    consist.add_unit(
        base_platform=None,  # coaches have no base platform by design currently
        type=DieselVehicleUnit,
        vehicle_length=7,
    )

    return consist
