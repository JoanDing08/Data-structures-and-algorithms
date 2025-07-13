#Give the child to implement a class on his own
#could be any other than what is discussed in the session.
#Example - Car, Student, Bank Account etc.

class app():
  def __init__(self,name,size):
    self.name=name
    self.size=size
  def information(self):
    print(f"Game: {self.name}\nDownload size: {self.size}")

class game(app):
  def __init__(self,name,size,genre):
    super().__init__(name,size)
    self.genre=genre
  def info(self):
    app.information(self)
    print(f"Genre: {self.genre}")
  
game1=game("Tetris","356.7MB","Puzzle")
game1.info()
