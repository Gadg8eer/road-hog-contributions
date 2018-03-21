from road_vehicle import CoveredHopperHauler

consist = CoveredHopperHauler(id='ribble_covered_hopper',
                              base_numeric_id=360,
                              name='Ribble [Covered Hopper Truck]',
                              semi_truck_so_redistribute_capacity=True,
                              vehicle_life=40,
                              intro_date=1978)

consist.add_unit(capacity=0,
                 vehicle_length=2,
                 semi_truck_shift_offset_jank=2,
                 effects=['EFFECT_SPRITE_DIESEL, -2, 1, 10'])

consist.add_unit(capacity=40,
                 vehicle_length=7)

