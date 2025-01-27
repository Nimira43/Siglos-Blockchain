import hashlib

def crypto_hash(data):
  return hashlib.sha256(data.encode('utf-8'))

def main():
  print(f"crypto_hash('test): {crypto_hash('test')}")

if __name__ == '__main__':
  main()