def max1(*args):
  _max_ = args[1]
  for i in args:
    if i > _max_:
      _max_ = i
  return _max_
