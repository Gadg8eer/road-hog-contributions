from road_vehicle import MailTruckConsist, DieselVehicleUnit


def main(roster_id):
    consist = MailTruckConsist(
        roster_id=roster_id,
        id="tallyho_mail",
        base_numeric_id=450,
        name="Tallyho",
        power=90,
        gen=2,
        intro_date_offset=-1,
    )  # introduce earlier than gen epoch by design

    consist.add_unit(
        base_platform=None,  # mail trucks have no base platform by design currently
        type=DieselVehicleUnit,
        vehicle_length=6,
    )

    return consist
