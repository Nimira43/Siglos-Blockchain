class Block:
  def __init__(self, data):
    self.data = data
  
  def __repr__(self):
    return f'Block - data: {self.data}'               

block = Block('Block')
print(block)
print(f'block.py __name__: {__name__}')