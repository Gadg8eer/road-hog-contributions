import global_constants
from road_vehicle import EngineConsist, BoxHauler

consist = EngineConsist(id = 'colbiggan',
              base_numeric_id = 880,
              title = 'Colbiggan [Box Tram]',
              roadveh_flag_tram = True,
              replacement_id = '-none',
              power = 300,
              vehicle_life = 40,
              intro_date = 1940)

consist.add_unit(BoxHauler(consist = consist,
                        weight = 12,
                        capacity = 0,
                        vehicle_length = 3,
                        effects = ['EFFECT_SPRITE_ELECTRIC, 0, 0, 10'],
                        spriterow_num = 0))

consist.add_unit(BoxHauler(consist = consist,
                        weight = 4,
                        capacity = 24,
                        vehicle_length = 4,
                        spriterow_num = 1), repeat=4)

consist.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=0)
