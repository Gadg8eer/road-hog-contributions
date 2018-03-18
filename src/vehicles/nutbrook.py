from road_vehicle import FruitVegHauler

consist = FruitVegHauler(id='nutbrook',
                         base_numeric_id=960,
                         title='Nutbrook [Fruit Tram]',
                         tram_type='ELRL',
                         vehicle_life=40,
                         intro_date=1940)

consist.add_unit(capacity=36,
                 vehicle_length=8,
                 effects=['EFFECT_SPRITE_ELECTRIC, 0, 0, 10'],
                 repeat=2)

