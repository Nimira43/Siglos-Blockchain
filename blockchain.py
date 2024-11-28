from block import Block, mine_block, genesis

class Blockchain:
  def __init__(self):
    self.chain = [genesis()]

  def add_block(self, data):
    last_block = self.chain[-1] 
    self.chain.append(mine_block(last_block, data))

  def __repr__(self):
    return f'Blockchain: {self.chain}'

def main():
  blockchain = Blockchain()
  blockchain.add_block('one') 
  blockchain.add_block('two') 
  print(blockchain)
  print(f'blockchain.py __name__: {__name__}')

if __name__ == '__main__':
  main()