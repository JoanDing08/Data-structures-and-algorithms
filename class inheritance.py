class vehicle():
  def __init__(self,brand,model):
    self.brand=brand
    self.model=model
  def info(self):
    print(f"Brand: {self.brand}\nModel: {self.model}")

class car(vehicle):
  def __init__(self,brand,model,doors):
    super().__init__(brand,model)
    self.doors=doors
  def information(self):
    print(f"Door number: {self.doors}")


c1=car("vauxhall","corsa","4")
c1.information()
