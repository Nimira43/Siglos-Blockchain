import hashlib
import json

def crypto_hash(data):
  stringified_data = json.dumps(data)

  return hashlib.sha256(stringified_data.encode('utf-8')).hexdigest()

def main():
  print(f"crypto_hash(['tree', 5, 'five']): {crypto_hash(['tree', 5, 'five'])}")

if __name__ == '__main__':
  
  main()