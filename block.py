class Block:
  def __init__(self, timestamp, last_hash, hash, data):
    self.timeout = timestamp
    self.last_hash = last_hash
    self.hash = hash
    self.data = data
  
  def __repr__(self):
    return (
      '*** BLOCK=['
      f'TIMESTAMP = {self.timestamp}, '
      f'LAST HASH = {self.last_hash}, '
      f'HASH = {self.hash}, '
      f'DATA = {self.data}] '
    )               

def main():
  block = Block('Block')
  print(block)
  print(f'block.py __name__: {__name__}')

if __name__ == '__main__':
  main()