import global_constants
from road_vehicle import CourierCar

consist = CourierCar(id = 'foxley',
                     base_numeric_id = 190,
                     title = 'Foxley [Courier Tram]',
                     tram_type = 'ELTR',
                     power = 240, # custom HP
                     vehicle_life = 40,
                     intro_date = 1903)

consist.add_unit(capacity = 15,
                 vehicle_length = 4,
                 effects = ['EFFECT_SPRITE_ELECTRIC, 0, 0, 10'],
                 repeat = 2)

consist.add_model_variant(intro_date=0,
                          end_date=global_constants.max_game_date,
                          spritesheet_suffix=0)
