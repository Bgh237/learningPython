#Allows us to pass mulitple args to a decorator

def my_decorator(func):
  def wrap_func(*args, **kwargs):
    print('*************')
    func(*args, **kwargs)
    print('*************')
  return wrap_func
#my_decorator calls the above function and passes the hello function as the input. The my_decorator function then runs the wrap_func and the hello function is called within the wrap_func. the output is printed
@my_decorator
def hello(greeting, emoji=':p'):
  print(greeting, emoji)

hello('hiiii')