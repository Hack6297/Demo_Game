from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
app = Ursina()
window.title = 'Demo Game'
player = FirstPersonController()

#-------------------------------Make Map------------------------------
ground1 = Entity(model='cube', scale=(100,-2,100), texture='grass_demo', texture_scale=(10,10), collider='box', position=(0,-3,0))
wall1 = Entity(model='cube', scale=(1,10,100), texture='wall_demo', collider='box', position=(-50, -2, 0))
wall2 = Entity(model='cube', scale=(1,10,100), texture='wall_demo', collider='box', position=(50, -2, 0))
wall3 = Entity(model='cube', scale=(100,10,1), texture='wall_demo', collider='box', position=(0, -2, -50))
wall4 = Entity(model='cube', scale=(100,10,1), texture='wall_demo', collider='box', position=(0, -2, 50))

ground2 = Entity(model='cube', scale=(30,1,30), texture='solid_demo', texture_scale=(30,30), collider='box', position=(0,-3,0))
wall5 = Entity(model='cube', scale=(1,5,30), texture='wall_demo', collider='box', position=(-15, -2, 0))
wall6 = Entity(model='cube', scale=(1,5,30), texture='wall_demo', collider='box', position=(15, -2, 0))
wall7 = Entity(model='cube', scale=(30,5,1), texture='wall_demo', collider='box', position=(0, -2, -15))
wall8 = Entity(model='cube', scale=(30,5,1), texture='wall_demo', collider='box', position=(0, -2, 15))

wall9 = Entity(model='cube', scale=(7.5,5,1), texture='wall_demo', collider='box', position=(-7.5, -2, 7.5))
wall10 = Entity(model='cube', scale=(7.5,5,1), texture='wall_demo', collider='box', position=(7.5, -2, 7.5))

wall11 = Entity(model='cube', scale=(7.5,5,1), texture='wall_demo', collider='box', position=(-7.5, -2, -7.5))
wall12 = Entity(model='cube', scale=(7.5,5,1), texture='wall_demo', collider='box', position=(7.5, -2, -7.5))

wall13 = Entity(model='cube', scale=(7.5,5,1), texture='wall_demo', collider='box', position=(-7.5, -2, 0))
wall14 = Entity(model='cube', scale=(7.5,5,1), texture='wall_demo', collider='box', position=(7.5, -2, 0))

sky = Sky()
#--------------------------------------------------------------

# Add a placeholder entity at the center of the solid demo area

# PlaceholderEnemy class similar to main4_fixed_collision.py
class PlaceholderEnemy(Entity):
	def __init__(self, position):
		super().__init__(
			model='cube',
			texture='placeholderdemo',
			scale=(1.5, 1.5, 1.5),
			color=color.red,
			collider='box',
			position=(5, 0, 2)
		)
		self.health = 100
		self.speed = 3.2
		self.text_entity = Text('PLACEHOLDER', parent=self, scale=8, color=color.white, billboard=True, y=2)
		self.chase_player = True

	def update(self):
		if self.chase_player:
			direction = (player.position - self.position).normalized()
			self.position += direction * self.speed * time.dt
			self.y = 0  # Keep at proper height
			self.look_at(player.position)

	def take_damage(self, amount=10):
		self.health -= amount
		self.color = color.yellow if self.health > 0 else color.gray
		self.text_entity.text = f'HP: {self.health}' if self.health > 0 else 'DEFEATED'
		if self.health <= 0:
			self.chase_player = False
			self.text_entity.text = 'DEFEATED'
			self.color = color.gray

# Instantiate the placeholder enemy
placeholder_enemy = PlaceholderEnemy(position=(0, 2, 0))

# Ursina calls update() on all Entities automatically




app.run()