import Utils

def planter():
	
	if get_ground_type() != Grounds.soil:
		till()
	if measure() == None or measure() < 6:
		harvest()
		plant(Entities.Cactus)
	if get_water() < .2:
		use_item(Items.Water)
	curX = get_pos_x()
	curY = get_pos_y()
	if curX == 0 and curY == 0:
		sort = True	

def sorter():
	curY = get_pos_y()
	measureC = measure()
	measureE= measure(East)
	measureS= measure(South)
	if measureC == None:
		measureC = 0
	if curY !=0 and measureS !=None and measureC < measureS:
		swap(South)
	if measureE!=None and measureC > measureE:
		swap(East)
				
def cactusPlant():
	get_pos_x()
	curY = get_pos_y()	
	Utils.movement(0, curY, get_world_size(), curY, 13,planter)

def cactusSort():
	get_pos_x()
	curY = get_pos_y()	
	Utils.movement(0, curY, get_world_size(), curY, 35,sorter)

def sortField():
	for i in range (get_world_size()):
		spawn_drone(cactusSort)
		move(North)	
		
def setField():
	for i in range (get_world_size()):
		spawn_drone(cactusPlant)
		move(North)
		
while True:	
	for i in range (5):
		do_a_flip()
	clear()
	Utils.goto(0,0)
	setField()
	for i in range (25):
		do_a_flip()
	Utils.goto(0,0)
	sortField()
	for i in range (55):
		do_a_flip()
	Utils.goto(31,30)
	harvest()
