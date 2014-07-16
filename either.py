def left(x):
  """
  Haskell: Left 5
  Python: left(5)
  """
  return lambda left_f, junk: left_f(x)


def right(x):
  """
  Haskell: Right True
  Python: right(True)
  """
  return lambda junk, right_f: right_f(x)


def either(f, g, e):
  """
  Haskell: either f g e
  Haskell: case e of
            (Left x) -> f x
            (Right y) -> g y
  Python: either(f, g, e)

  >>> x = left(42)
  >>> y = right("hello")
  >>> either(lambda x: x * 2, lambda x: len(x), x)
  84
  >>> either(lambda x: x * 2, lambda x: len(x), y)
  5
  """
  return e(f, g)
