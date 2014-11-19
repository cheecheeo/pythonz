from collections import namedtuple

def apply(f, x):
  return f(x)

def swap(x, y):
  return (y, x)

def typedtuple(typename, funFieldNames):
  """
  Typed namedtuples.

  >>> Foo = typedtuple('Foo', ['name', (int, 'value'), (str, 'string_value')])
  >>> x = Foo('hello', '42', 'world bar')
  >>> x
  Foo(name='hello', value=42, string_value='world bar')
  >>> x.__dict__
  OrderedDict([('name', 'hello'), ('value', 42), ('string_value', 'world bar')])

  >>> Bar = typedtuple('Bar', ['name', 'value', 'simple'])
  >>> Bar('hello', '42')
  Bar(name='hello', value='42', simple=None)

  >>> Baz = typedtuple('Baz', [])
  >>> Baz()
  Baz()
  """

  def functionify(stringOrTuple):
    return stringOrTuple if type(stringOrTuple) == type(()) else (lambda x: x, stringOrTuple)

  withFunctions = map(functionify, funFieldNames)
  namesAndFunctions = dict(map(lambda t: swap(t[0], t[1]), withFunctions))

  fieldNames = map(lambda x: x[-1], withFunctions)
  types = map(lambda x: x[0], withFunctions)

  nt = namedtuple(typename, fieldNames)

  def factory(*args, **kwargs):
    typedArgs = map(apply, types, args)
    typedKWArgs = dict((name, namesAndFunctions[name](arg)) for (name, arg) in kwargs)

    return nt(*typedArgs, **typedKWArgs)

  return factory
