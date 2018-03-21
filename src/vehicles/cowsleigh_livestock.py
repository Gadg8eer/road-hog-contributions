from road_vehicle import LivestockHauler

consist = LivestockHauler(id='cowsleigh_livestock',
                          base_numeric_id=900,
                          name='Cowsleigh [Livestock Truck]',
                          vehicle_life=40,
                          intro_date=1911)

consist.add_unit(capacity=14,
                 vehicle_length=6,
                 effect_spawn_model='EFFECT_SPAWN_MODEL_STEAM',
                 effects=['EFFECT_SPRITE_STEAM, -5, 0, 12'])

consist.add_unit(capacity=10,
                 vehicle_length=4)

