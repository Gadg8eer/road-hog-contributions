from road_vehicle import PaxLocalBusConsist, DieselVehicleUnit

# for each generation, bus and coach variants have same power and intro date
# coaches faster, lower capacity than equivalent bus


def main(roster_id):
    consist = PaxLocalBusConsist(
        roster_id=roster_id,
        id="thunder_pax",
        base_numeric_id=40,
        name="Thunder",
        power=160,
        speed=45,
        gen=3,
        intro_date_offset=-4,
    )  # introduce earlier than gen epoch by design

    consist.add_unit(
        base_platform=None,  # buses have no base platform by design currently
        type=DieselVehicleUnit,
        vehicle_length=7,
    )

    return consist
