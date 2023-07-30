# Calculating number of tiles and the empty space
# The total length of wall = 100, length of each tiles = 5
# The wall must be start and end with black tiles
total_length = 100
tile_length = 5
number_tiles = (total_length/tile_length)-1
total_gap = (((total_length/tile_length)-number_tiles)*tile_length)
print("Number of Tiles = ",number_tiles)
print("Total Gap =",total_gap)
print("Gap at each End = ",total_gap/2)

