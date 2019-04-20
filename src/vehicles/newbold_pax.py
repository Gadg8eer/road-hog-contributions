from road_vehicle import PaxHauler, ElectricRoadVehicle

consist = PaxHauler(id='newbold_pax',
                    base_numeric_id=30,
                    name='Newbold',
                    tram_type='ELRL',
                    vehicle_life=40,
                    gen=3,
                    intro_date_offset=1)  # introduce later than gen epoch by design

consist.add_unit(type=ElectricRoadVehicle,
                 capacity=50,
                 vehicle_length=8,
                 effects=['EFFECT_SPRITE_ELECTRIC, 0, 0, 12'],
                 repeat=2)
