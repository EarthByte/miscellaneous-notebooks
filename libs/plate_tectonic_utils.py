#
#---------function definitions----------
#---------you might want to move along to the main() funtion section. more fun over there---------------
#
#function: assign colour by plate id
def get_colour_by_plateid(plate_id):
    from matplotlib import colors
    converter = colors.ColorConverter()
    plateid_colours = {
        0: list(converter.to_rgba('yellow',alpha=1.0)),
        1: list(converter.to_rgba('aqua',alpha=1.0)),
        2: list(converter.to_rgba('seagreen',alpha=1.0)),
        3: list(converter.to_rgba('fuchsia',alpha=1.0)),
        4: list(converter.to_rgba('slategray',alpha=1.0)),
        5: list(converter.to_rgba('lime',alpha=1.0)),
        6: list(converter.to_rgba('indigo',alpha=1.0)),
        7: list(converter.to_rgba('red',alpha=1.0)),
        8: list(converter.to_rgba('orange',alpha=1.0)),
        9: list(converter.to_rgba('lightsalmon',alpha=1.0)),
        10: list(converter.to_rgba('navy',alpha=1.0)),
    }
    return plateid_colours[plate_id%11]
