import time

def mine_block(last_block, data):
  timestamp = time.time_ns()
  last_hash =last_block.hash
  hash = f'{timestamp}-{last_hash}'
  return Block(timestamp, last_hash, hash, data)

def genesis():
  return Block(1, 'genesis_last_hash', 'genesis_hash', [])

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