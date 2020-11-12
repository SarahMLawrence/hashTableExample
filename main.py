example_string = "hello"

def my_hashing_func(input_string, table_size):
  # numerical representation of example_string
  bytes_representation = input_string.encode()
  sum = 0
  for byte in bytes_representation:
    sum += byte
  return sum % table_size

print(my_hashing_func(example_string, 10))