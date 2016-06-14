import global_constants
from road_vehicle import RVConsist, CourierCar

consist = RVConsist(vehicle_type = CourierCar,
                id = 'goldmire',
                base_numeric_id = 200,
                title = 'Goldmire [Courier Truck]',
                replacement_id = '-none',
                power = 250, # custom power
                speed = 75,
                vehicle_life = 40,
                intro_date = 1971)

consist.add_unit(weight = 8,
                capacity = 25,
                        capacity_mail = 50,
                vehicle_length = 6,
                visual_effect = 'VISUAL_EFFECT_DIESEL')

consist.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=0)
