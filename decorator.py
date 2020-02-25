def my_decorator(func):
  def wrap_func():
    print('*************')
    func()
    print('*************')
  return wrap_func

#my_decorator calls the above function and passes the hello function as the input. The my_decorator function then runs the wrap_func and the hello function is called within the wrap_func. the output is printed

@my_decorator
def hello():
  print('helloooo')

@my_decorator
def bye():
  print('See you later')

hello()
bye()