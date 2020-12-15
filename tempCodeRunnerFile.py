class Torradeira:
  def __init__(self, tempo):
    self.tempo = 0
    self.calorAtual = 0
    self.calorMaximo = 100

  def torrar(self):
    self.tempo += 1    
    if self.calorAtual < self.calorMaximo:      
      self.calorAtual += 1 + self.calorAtual