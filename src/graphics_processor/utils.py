from graphics_processor import graphics_constants
from graphics_processor import registered_pipelines


def make_colour_map(input, output, map_size):
    result = {}
    for i in range(map_size):
        result[input + i] = output + i
    return result

def get_container_recolour_maps():
    CC1 = graphics_constants.CC1
    CC2 = graphics_constants.CC2
    map_1 = make_colour_map(170, CC1, 8)
    map_1.update(make_colour_map(42, CC1, 8))

    map_2 = make_colour_map(170, CC2, 8)
    map_2.update(make_colour_map(42, CC2, 8))

    map_3 = make_colour_map(170, 8, 8)
    map_3.update(make_colour_map(42, 8, 8))

    return (map_1, map_2, map_3)

def get_bulk_cargo_recolour_maps():
    GRVL = {170: 6, 171: 4, 172: 7, 173: 8, 174: 21, 175: 11, 176: 12}
    IORE = {170: 75, 171: 76, 172: 123, 173: 122, 174: 124, 175: 74, 176: 104}
    CORE = {170: 1, 171: 32, 172: 25, 173: 27, 174: 34, 175: 56, 176: 59}
    AORE = {170: 42, 171: 123, 172: 74, 173: 125, 174: 162, 175: 126, 176: 78}
    SAND = {170: 108, 171: 64, 172: 65, 173: 197, 174: 36, 175: 196, 176: 197}
    COAL = {170: 1, 171: 1, 172: 2, 173: 2, 174: 3, 175: 4, 176: 5}
    CLAY = {170: 57, 171: 57, 172: 57, 173: 77, 174: 78, 175: 78, 176: 79}
    SCMT = {170: 104, 171: 3, 172: 2, 173: 70, 174: 71, 175: 72, 176: 3}
    PHOS = {170: 63, 171: 64, 172: 192, 173: 65, 174: 193, 175: 64, 176: 194}

    # we just return a fixed-order tuple here, don't worry about the labels...
    # ...we have to manually specify the spriterow<->cargo label mapping in the wagon definition anyway
    # GRVL is also reused for generic unknown cargos, and is in position 0 for this reason
    # (there is no mapping for unknown cargos, just uses first spriteset)
    return (GRVL, IORE, CORE, AORE, SAND, COAL, CLAY, SCMT, PHOS)


class GraphicsProcessorFactory(object):
    # simple class which wraps graphics_processor, which uses pixa library
    # pipeline_name refers to a pipeline class which defines how the processing is done
    # may be reused across consists, so don't store consist info in the pipeline, pass it to pipeline at render time
    # this is kind of factory-pattern-ish, but don't make too much of that, it's not important
    def __init__(self, pipeline_name, options):
        self.pipeline_name = pipeline_name
        self.options = options
        self.pipeline = registered_pipelines[pipeline_name]


def get_composited_cargo_processors(template, copy_block_top_offsets, paste_top_offset):
    # handles compositing (spritesheet extension and recoloring) for bulk (mineral) cargos and piece goods cargos
    # also provides optional 2CC recolor
    bulk_cargo_recolour_maps = get_bulk_cargo_recolour_maps()
    piece_cargo_maps = []
    graphics_options_master = {'template': '',
                               'bulk_cargo_recolour_maps': bulk_cargo_recolour_maps,
                               'piece_cargo_maps': piece_cargo_maps,
                               'copy_block_top_offsets': copy_block_top_offsets,
                               'paste_top_offset': paste_top_offset,
                               'num_rows_per_unit': graphics_constants.load_states_num_rows_per_unit}

    graphics_options_1 = dict((k, v) for (k, v) in graphics_options_master.items())
    graphics_options_1['template'] = template
    graphics_options_2 = dict((k, v) for (k, v) in graphics_options_1.items())
    graphics_options_2['swap_company_colours'] = True
    graphics_processor_1 = GraphicsProcessorFactory('extend_spriterows_for_composited_cargos_pipeline', graphics_options_1)
    graphics_processor_2 = GraphicsProcessorFactory('extend_spriterows_for_composited_cargos_pipeline', graphics_options_2)
    return (graphics_processor_1, graphics_processor_2)
