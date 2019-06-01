from road_vehicle import PaxLocalTramConsist, ElectricRoadVehicle

consist = PaxLocalTramConsist(id='northbeach_pax',
                       base_numeric_id=690,
                       name='Northbeach',
                       vehicle_life=40,
                       gen=4,
                       intro_date_offset=1)  # introduce later than gen epoch by design

consist.add_unit(type=ElectricRoadVehicle,
                 capacity=60,
                 vehicle_length=8,
                 effects=['EFFECT_SPRITE_ELECTRIC, 0, 0, 12'],
                 repeat=2)
