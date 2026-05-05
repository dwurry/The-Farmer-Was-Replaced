import Utils

def Test():
	harvest()
	if get_ground_type() == Grounds.Grassland:
		till()
	else:
		till()
	if get_ground_type() == Grounds.soil:
		plant(Entities.Carrot)
		#do_a_flip()
		
def pumpkinHarvest():
	homeX = 0
	homeY = 0
	if get_ground_type() != Grounds.soil:
		harvest()
		till() 
	if can_harvest() == False:
		plant(Entities.Pumpkin)
	if (get_pos_x() == homeX and get_pos_y() == homeY):
		harvest()
		plant(Entities.Pumpkin)
		if get_water() < .5:
			use_item(Items.Water)

def pumpkin():
	if get_ground_type() != Grounds.soil:
		harvest()
		till() 
	if can_harvest() == False:
		plant(Entities.Pumpkin)
	
def pumpkinPatchHarvest():
	homeX = 0
	homeY = 0
	awayX = (get_world_size() / 2) -1
	awayY = homeY + 3
	quick_print("harvest patch:", homeX," ", homeY," ", awayX," ", awayY)
	Utils.movement(homeX,homeY,awayX,awayY,-1,pumpkinHarvest)
	
def pumpkinPatch1():
	homeX = 0
	homeY = (get_world_size() / 8) * 1
	awayX = (get_world_size() / 2) -1
	awayY = homeY + 3
	quick_print("patch1:", homeX," ", homeY," ", awayX," ", awayY)
	Utils.movement(homeX,homeY,awayX,awayY,-1,pumpkin)

def pumpkinPatch2():
	homeX = 0
	homeY = (get_world_size() / 8) * 2
	awayX = (get_world_size() / 2) -1
	awayY = homeY + 3
	quick_print("patch2:", homeX," ", homeY," ", awayX," ", awayY)
	Utils.movement(homeX,homeY,awayX,awayY,-1,pumpkin)
	
def pumpkinPatch3():
	homeX = 0
	homeY = (get_world_size() / 8) * 3
	awayX = (get_world_size() / 2) -1
	awayY = homeY + 3
	quick_print("patch3:", homeX," ", homeY," ", awayX," ", awayY)
	Utils.movement(homeX,homeY,awayX,awayY,-1,pumpkin)
			
def treesAndCactus():
	harvest()
	if (get_pos_y() + get_pos_x()) % 2 == 0:
		if get_ground_type() == Grounds.soil:
			till()
		plant(Entities.Tree)										
	else:					
		if get_ground_type() != Grounds.soil:
			till()
		plant(Entities.Cactus)
	if get_water() < .2:
		use_item(Items.Water)
#		use_item(Items.Fertilizer)
		
def forest1():
	homeX = get_world_size()/2
	homeY = 0
	awayX = get_world_size() -1
	awayY = homeY +1
	Utils.movement(homeX,homeY,awayX,awayY,-1,treesAndCactus)

def forest2():
	homeX = get_world_size()/2
	homeY = 2
	awayX = get_world_size() -1
	awayY = homeY +1
	Utils.movement(homeX,homeY,awayX,awayY,-1,treesAndCactus)
		
def forest3():
	homeX = get_world_size()/2
	homeY = 4
	awayX = get_world_size() -1
	awayY = homeY + 1
	Utils.movement(homeX,homeY,awayX,awayY,-1,treesAndCactus)
	
def forest4():
	homeX = get_world_size()/2
	homeY = 6
	awayX = get_world_size() -1
	awayY = homeY +1
	Utils.movement(homeX,homeY,awayX,awayY,-1,treesAndCactus)
		
def forest5():
	homeX = get_world_size()/2
	homeY = 8
	awayX = get_world_size() -1
	awayY = homeY +1
	Utils.movement(homeX,homeY,awayX,awayY,-1,treesAndCactus)
					
def forest6():
	homeX = get_world_size()/2
	homeY = 10
	awayX = get_world_size() -1
	awayY = homeY +1
	Utils.movement(homeX,homeY,awayX,awayY,-1,treesAndCactus)
					
def forest7():
	homeX = get_world_size()/2
	homeY = 12
	awayX = get_world_size() -1
	awayY = homeY +1
	Utils.movement(homeX,homeY,awayX,awayY,-1,treesAndCactus)
					
def forest8():
	homeX = get_world_size()/2
	homeY = 14
	awayX = get_world_size() -1
	awayY = homeY +1
	Utils.movement(homeX,homeY,awayX,awayY,-1,treesAndCactus)
										
def carrot():
	harvest()
	if get_ground_type() != Grounds.soil:
		till()
	plant(Entities.Carrot)
	if get_water() < .2:
		use_item(Items.Water)
	
def carrotPatch1():
	homeX = 0
	homeY = get_world_size()/2
	awayX = get_world_size() -1
	awayY = homeY
	Utils.movement(homeX, homeY, awayX, awayY, -1,carrot)
	
def carrotPatch2():
	homeX = 0
	homeY = get_world_size()/2 + 1
	awayX = get_world_size() -1
	awayY = homeY
	Utils.movement(homeX, homeY, awayX, awayY, -1,carrot)

def sunFlower():
	harvest()
	if get_ground_type() != Grounds.soil:
		till()
	plant(Entities.Sunflower)
	if get_water() < .2:
		use_item(Items.Water)
		
	
def powerPatch():
	homeX = 0
	homeY = get_world_size()/2 + 2
	awayX = get_world_size() -1
	awayY = homeY
	Utils.movement(homeX, homeY, awayX, awayY, -1,sunFlower)

def hay():
	harvest()
	if get_ground_type() == Grounds.soil:
		till()
	if get_water() < .2:
		use_item(Items.Water)

def medow1():
	homeX = 0
	homeY = get_world_size() - 1
	awayX = get_world_size() -1
	awayY = homeY
	Utils.movement(homeX, homeY, awayX, awayY, -1,hay)
	
def medow2():
	homeX = 0
	homeY = get_world_size() - 2
	awayX = get_world_size() -1
	awayY = homeY
	Utils.movement(homeX, homeY, awayX, awayY, -1,hay)

def medow3():
	homeX = 0
	homeY = get_world_size() - 3
	awayX = get_world_size() -1
	awayY = homeY
	Utils.movement(homeX, homeY, awayX, awayY, -1,hay)
		
def medow4():
	homeX = 0
	homeY = get_world_size() - 4
	awayX = get_world_size() -1
	awayY = homeY
	Utils.movement(homeX, homeY, awayX, awayY, -1,hay)
	
def medow5():
	homeX = 0
	homeY = get_world_size() - 5
	awayX = get_world_size() -1
	awayY = homeY
	Utils.movement(homeX, homeY, awayX, awayY, -1,hay)
	
def forest9():
	homeX = 0
	homeY = get_world_size() - 6
	awayX = get_world_size() -1
	awayY = homeY
	Utils.movement(homeX,homeY,awayX,awayY,-1,treesAndCactus)
					
def forest10():
	homeX = 0
	homeY = get_world_size() - 7
	awayX = get_world_size() -1
	awayY = homeY
	Utils.movement(homeX,homeY,awayX,awayY,-1,treesAndCactus)
	
def forest11():
	homeX = 0
	homeY = get_world_size() - 8
	awayX = get_world_size() -1
	awayY = homeY
	Utils.movement(homeX,homeY,awayX,awayY,-1,treesAndCactus)

def forest12():
	homeX = 0
	homeY = get_world_size() - 9
	awayX = get_world_size() -1
	awayY = homeY
	Utils.movement(homeX,homeY,awayX,awayY,-1,treesAndCactus)

def forest13():
	homeX = 0
	homeY = get_world_size() - 10
	awayX = get_world_size() -1
	awayY = homeY
	Utils.movement(homeX,homeY,awayX,awayY,-1,treesAndCactus)
	
def forest14():
	homeX = 0
	homeY = get_world_size() - 11
	awayX = get_world_size() -1
	awayY = homeY
	Utils.movement(homeX,homeY,awayX,awayY,-1,treesAndCactus)
	
def forest15():
	homeX = 0
	homeY = get_world_size() - 12
	awayX = get_world_size() -1
	awayY = homeY
	Utils.movement(homeX,homeY,awayX,awayY,-1,treesAndCactus)
	
def forest16():
	homeX = 0
	homeY = get_world_size() - 13
	awayX = get_world_size() -1
	awayY = homeY
	Utils.movement(homeX,homeY,awayX,awayY,-1,treesAndCactus)
	
def forest17():
	homeX = 0
	homeY = get_world_size() - 14
	awayX = get_world_size() -1
	awayY = homeY
	Utils.movement(homeX,homeY,awayX,awayY,-1,treesAndCactus)
		
	
	
	
