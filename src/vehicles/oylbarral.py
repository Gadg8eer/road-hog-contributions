import global_constants
from road_vehicle import Tanker

consist = Tanker(id = 'oylbarral',
                 base_numeric_id = 320,
                 title = 'Oylbarral [Tanker Tram]',
                 roadveh_flag_tram = True,
                 tram_type = 'ELTR',
                 vehicle_life = 40,
                 intro_date = 1945)

consist.add_unit(capacity = 0,
                 vehicle_length = 4,
                 effects = ['EFFECT_SPRITE_ELECTRIC, 0, 0, 10'],
                 always_use_same_spriterow = True)

consist.add_unit(capacity = 36,
                 vehicle_length = 6,
                 repeat = 2)

consist.add_model_variant(intro_date=0,
                          end_date=global_constants.max_game_date,
                          spritesheet_suffix=0,
                          graphics_processor=consist.graphics_processors[0])
