from road_vehicle import CoveredHopperHauler, DieselRoadVehicle

consist = CoveredHopperHauler(id='mcdowell_covered_hopper',
                              base_numeric_id=280,
                              name='McDowell',
                              semi_truck_so_redistribute_capacity=True,
                              vehicle_life=40,
                              gen=4,
                              intro_date=2007)

consist.add_unit(type=DieselRoadVehicle,
                 capacity=0,
                 vehicle_length=2,
                 semi_truck_shift_offset_jank=2,
                 effects=['EFFECT_SPRITE_DIESEL, -2, 1, 10'])

consist.add_unit(capacity=40,
                 vehicle_length=7)
