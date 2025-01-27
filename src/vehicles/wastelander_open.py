from road_vehicle import OpenTruckConsist


def main(roster_id):
    consist = OpenTruckConsist(
        roster_id=roster_id,
        id="wastelander_open",
        base_numeric_id=1010,
        name="Wastelander",
        roadveh_flag_tram=True,
        power=90,
        gen=4,
        intro_date=1870,
    )

    consist.add_unit(capacity=0, vehicle_length=4)

    consist.add_unit(capacity=10, vehicle_length=3, repeat=2)

    consist.add_unit(capacity=10, vehicle_length=3)

    return consist
