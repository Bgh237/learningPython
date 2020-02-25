from time import time

def performance(func):
  def wrapper(*args, **kwargs):
    start = time()
    result = func(*args, **kwargs)
    finish = time()
    print(f'It took {finish-start} seconds')
    return result
  return wrapper



@performance
def long_time():
  for i in range(100000000):
    i*5

long_time()