import pygame, my, input, ui, map, building, mob, random
pygame.init()

class Handler:
	"""Keep the main.runGame() function nice and tidy"""
	def __init__(self):
		my.ticks = 0
		my.tick = []
		for i in range(20):
			my.tick.append(False)
		my.map = map.Map()
		for x in range(my.MAPXCELLS):
			for y in range(my.MAPYCELLS):
				if my.map.map[x][y] == 'tree':
					map.Tree((x, y))
		my.input = input.Input()
		my.camera = map.Camera()
		my.hud = ui.Hud()
		my.mode = 'look' 
		my.resources = {'wood': my.STARTRESOURCES['wood'], 
						'iron': my.STARTRESOURCES['iron'], 'cheese': my.STARTRESOURCES['cheese']}
		my.maxResources = {'wood': my.STARTMAXRESOURCES['wood'], 
						'iron': my.STARTMAXRESOURCES['iron'], 'cheese': my.STARTMAXRESOURCES['cheese']}
		my.updateSurf = True
		my.gameRunning = True

		for i in range(3):
			mob.Human((random.randint(5, 30), random.randint(5, 25)), 'woodcutter')
		for i in range(5):
			mob.Human((random.randint(5, 25), random.randint(5, 25)), 'builder')


	def update(self):
		my.ticks += 1
		for i in range(1, 19):
			if my.ticks % i == 0:
				my.tick[i] = True
			else:
				my.tick[i] = False
		my.input.get()
		my.map.update()
		building.updateBuildings()
		mob.updateMobs()
		my.camera.update()
		my.hud.update()

		pygame.display.update()
		my.FPSCLOCK.tick(my.FPS)
		pygame.display.set_caption('Real time strategy' + ' ' * 10 + 'FPS: ' + str(int(my.FPSCLOCK.get_fps())))
		my.input.checkForQuit()

		for key in my.resources.keys():
			if my.resources[key] > my.maxResources[key]:
				my.resources[key] = my.maxResources[key]
			if my.resources[key] < 0:
				my.resources[key] = 0