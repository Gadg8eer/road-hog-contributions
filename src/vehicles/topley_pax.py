from road_vehicle import PaxLocalBusConsist, DieselVehicleUnit

# for each generation, bus and coach variants have same power and intro date
# coaches faster, lower capacity than equivalent bus


def main(roster_id):
    consist = PaxLocalBusConsist(
        roster_id=roster_id,
        id="topley_pax",
        base_numeric_id=60,
        name="Topley",
        power=360,
        speed=55,
        gen=5,
        intro_date_offset=-7,
    )  # introduce earlier than gen epoch by design

    consist.add_unit(
        base_platform=None,  # buses have no base platform by design currently
        type=DieselVehicleUnit,
        vehicle_length=7,
    )

    return consist
