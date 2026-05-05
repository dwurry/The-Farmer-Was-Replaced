import Utils

def planter():
	
	harvest()
	if get_ground_type() != Grounds.soil:
		till()
	plant(Entities.Cactus)
	if get_water() < .2:
		use_item(Items.Water)
	curX = get_pos_x()
	curY = get_pos_y()
	if curX == 0 and curY == 0:
		sort = True	

def sorter():
	if measure() > measure(East):
		swap(East)
	if curY !=0 and measure() < measure(South):
		swap(South)
		
def cactusPlant():
	get_pos_x()
	curY = get_pos_y()	
	Utils.movement(0, curY, get_world_size(), curY, 1,planter)

def cactusSort():
	get_pos_x()
	curY = get_pos_y()	
	Utils.movement(0, curY, get_world_size(), curY, 32,sorter)

def sortField():
	for i in range (get_world_size()):
		spawn_drone(cactusSort)
		move(North)	
		
def setField():
	for i in range (get_world_size()):
		spawn_drone(cactusPlant)
		move(North)
		
	
clear()
setField()
sortField()
