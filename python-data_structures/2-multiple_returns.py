def multiple_returns(sentence):
  
  result = ()
  length = len(sentence)
  first = sentence[0]
  
  if length >= 1:
    result = (length, first)
    return result
  else:
    first = None
    result = (length, first) 
    return result
  