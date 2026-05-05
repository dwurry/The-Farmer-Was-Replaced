import Utils
import Pumpkin_Eater
import Mower
import CarrotTopper
import SunPower
import LumberJack
import Planters

def ProcessFullField():
	Utils.goto(0,0)
	change_hat(Hats.Dinosaur_Hat)
	hMove = East
	vMove = North
	while True:
		for x_row in range(row_max):
			for y_col in range (col_max):
				if x_row <(row_max/2):
					if y_col < (col_max/2) :
						if get_ground_type() != Grounds.soil:
							till() 
						if can_harvest() == False:
							plant(Entities.Pumpkin)
						if x_row==21 and y_col ==10:
							quick_print(x_row,  (row_max/2-1))
							quick_print(y_col,  (col_max/2-1))
						#if (x_row == 0 and y_col == 0):
							#harvest()
							#plant(Entities.Pumpkin)
					if y_col > (col_max/2)-1:
						if can_harvest():
							harvest()
						if (y_col + x_row) % 2 == 0:
							if get_ground_type() == Grounds.soil:
								harvest()
								till()
							plant(Entities.Tree)										
						if (y_col + x_row) % 2 != 0:
							if get_ground_type() != Grounds.soil:
								till()
							plant(Entities.Carrot)	
	
				if x_row > (row_max/2)-1 and x_row < (row_max/2)+(row_max/4)-1:
					if y_col < col_max:
						if (y_col + x_row) % 2 == 0:
							harvest()
							if get_ground_type() != Grounds.soil:
								till()
							plant(Entities.Carrot)										
						if (y_col + x_row) % 2 != 0:
							harvest()
							if get_ground_type() != Grounds.soil:
								till()
							plant(Entities.Carrot)			
							#plant(Entities.Cactus)
				if x_row > (row_max/2)+4 and  x_row < (row_max/2)+9:
					harvest()
					if get_ground_type() != Grounds.soil:
						till()
					plant(Entities.Sunflower)							
				if x_row >(row_max/2)+(row_max/4):
					harvest()
					if get_ground_type() == Grounds.soil:
						till()
					plant(Entities.Grass)
				move(hMove)
				#spawn_drone(ProcessFullField)
			move(vMove)
			if hMove ==East:
				hMove = West
			else:
				hMove = East
		if vMove ==North:
			vMove = South
		else:
			vMove = North
								

#ProcessFullField end


spawn_drone(Planters.pumpkinPatch)
do_a_flip()
do_a_flip()
do_a_flip()
do_a_flip()
do_a_flip()
spawn_drone(Utils.movement(get_world_size()/2,get_world_size()/2,0,0, Planters.pumpkin))
movement(get_world_size()/2,get_world_size()/2,0,0, Planters.pumpkin)

row_max = 32
col_max = 32
spawn_drone(LumberJack.mapJack)
spawn_drone(Mower.mower)
spawn_drone(CarrotTopper.topper)
spawn_drone(Pumpkin_Eater.mapPumpkinPatch)
spawn_drone(ProcessFullField)
spawn_drone(SunPower.sunPower)
for flips in range(10):
	do_a_flip()
spawn_drone(Pumpkin_Eater.mapPumpkinPatch)
spawn_drone(Mower.mower)
spawn_drone(CarrotTopper.topper)
spawn_drone(LumberJack.mapJack)
for flips in range(10):
	do_a_flip()
spawn_drone(Pumpkin_Eater.mapPumpkinPatch)
spawn_drone(LumberJack.mapJack)
for flips in range(10):
	do_a_flip()
spawn_drone(LumberJack.mapJack)
spawn_drone(Mower.mower)
spawn_drone(Mower.mower)
spawn_drone(Mower.mower)
spawn_drone(Mower.mower)

