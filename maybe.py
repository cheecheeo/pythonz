"""
Haskell: Nothing
Python: nothing
"""
nothing = lambda nothing_v, junk: nothing_v


def just(x):
  """
  Haskell: Just True
  Python: just(true)
  """
  return lambda junk, just_f: just_f(x)


def maybe(x, f, m):
  """
  Haskell: maybe x f m
  Haskell: case m of
            Nothing -> x
            (Just j) -> f j
  Python: maybe(x, f, m)

  >>> x = nothing
  >>> y = just("hello")
  >>> maybe(42, lambda x: len(x), x)
  42
  >>> maybe(42, lambda x: len(x), y)
  5
  """
  return m(x, f)
