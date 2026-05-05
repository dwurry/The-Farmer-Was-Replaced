def goto(x, y):
	moves = 0
	HorizontalMovement = West
	VerticalMovement = South
	curX = get_pos_x()
	if(curX <= x):
		HorizontalMovement = East 
		moves = x - curX
	else:
		moves = curX - x
		
	for moveHorzontal in range (moves):
		move(HorizontalMovement)

	curY = get_pos_y()
	if(curY <= y):
		VerticalMovement = North
		moves = y- curY
	else:
		moves = curY - y
	
	for moveWest in range(moves):
		move(VerticalMovement)
#Goto(x,y) end

def randomFlips(x):
	for f in range(random() * x):
		do_a_flip()
	
def randomPets(x):
	for f in range(random() * x):
		pet_the_piggy()

def randomHat(x):
	for h in range (random() * x):
		if h > 1:
			print("change_hat(Hats.Dinosaur_Hat)")

def movement(homeX, homeY, awayX, awayY, loops, plantMethod):
#	clear() #This prevents drown spawn
	goto(homeX,homeY)
	movingAway = True
	hMove = East  #horizontalMovement
	vMove = North #verticalMovement
	goalX = awayX
	goalY = awayY
	loop = 0
		
	while loops > 0 and loops != -1:  #-1 signals an infinate loop
		
		plantMethod()
		# set up initila movement
		curX = get_pos_x()
		curY = get_pos_y()
		
		if (curX < goalX):
			fromX = curX
			toX = goalX
			hMove = East
		else:
			fromX = goalX
			toX = curX
			hMove = West
			
		if(curY < goalY):
			vMove = North
		else:
			vMove = South

		if(fromX < toX):
			move(hMove) 
			curX = get_pos_x()
			
		elif(curX == goalX and curY == goalY):
			#Retrun to home
			if curX != homeX or curY != homeY:
				#quick_print("calling goto home:",homeX,homeY,curX,curY)
				if (curX == homeX):
					goalX = flipGoal(goalX, homeX, awayX)
				if (curY == homeY):
					goalY = flipGoal(goalY, homeY, awayY)
					if loops != -1 and loops != 0:
						loops = loops -1		
				goto(homeX, homeY)
			
		elif(curX == goalX):
			goalX = flipGoal(goalX, homeX, awayX)
			#if curX = homeX and curY != homeY:
			move(vMove)
				
# end movement()

def flipGoal(goal, home, away):  # FlipGoalX
	if(goal == away):
		goal = home
	else:
		goal = away
	return goal	
