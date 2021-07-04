class Kisi:
	def __init__(self,ad,yas):
		self.ad = ad
		self.yas = yas
	
	def karsilama(self):
		print("Hoş geldin ", self.ad)

	def ugurlama(self):
		print("Gule gule", self.ad)

kisi1 = Kisi("Cahit", 35)
kisi1.karsilama()

