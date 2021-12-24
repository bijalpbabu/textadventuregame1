_world = {}
starting_position = (0, 0)
 
def load_tiles(level):

    if(level == 1):
        mapTxt = "map1.txt"
        title = "Batman Meets Joker"
    if(level == 2):
        title = "Batman Meets Bane"
        mapTxt = "map2.txt"
    if(level == 3):
        title = "Batman Meets Superman"
        mapTxt = "map3.txt"  

    print("============ > Level ", level, " ", title)    

    """Parses a file that describes the world space into the _world object"""
    with open(mapTxt, 'r') as f:
        rows = f.readlines()
    x_max = len(rows[0].split('|')) # Assumes all rows contain the same number of tabs
    for y in range(len(rows)):
        cols = rows[y].split('|')
        for x in range(x_max):
            tile_name = cols[x].replace('\n', '') # Windows users may need to replace '\r\n'
            if tile_name == 'StartingRoom':
                global starting_position
                starting_position = (x, y)
            _world[(x, y)] = None if tile_name == '' else getattr(__import__('tiles'), tile_name)(x, y)

def tile_exists(x, y):
    return _world.get((x, y))