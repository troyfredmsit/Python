class Program():
	def __init__(self, *args, **kwargs):

		self.lang = input("What language?: ")
		self.version = float(input("Version: "))
		self.skill = input("What skill level?: ")
	def upgrade(self):
		new_version = float(input("What version? : "))
		print("We have updated the version for", self.lang)
		self.version = new_version
## Main Run area ##
p1 = Program()
# p2 = Program()

print(p1.version)
# print(p2.lang)
p1.upgrade()
print(p1.version)

inp = input("")