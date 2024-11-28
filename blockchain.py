class Block:
  def __init__(self, data):
    self.data = data

class Blockchain:
  def __init__(self):
    self.chain = []

  def add_block(self, data):
    self.chain.append(Block(data)  