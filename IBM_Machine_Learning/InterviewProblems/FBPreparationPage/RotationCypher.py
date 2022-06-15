import math
# Add any extra import statements you may need here


# Add any helper functions you may need here


def rotationalCipher(input, rotation_factor):
  # Write your code here
  cypher_string = ""
  for c, value in enumerate(input):
    if 90 >= ord(value) >= 65:
      number_to_sum = umber_to_sum = rotation_factor % 26
      if (number_to_sum + ord(value)) > 90:
        cypher_string += "{}".format(chr(65 + number_to_sum - 1 - (90 - ord(value))))
      else:
        cypher_string += "{}".format(chr(ord(value) + number_to_sum))
    elif 122 >= ord(value) >= 97:
      number_to_sum = rotation_factor % 26
      if (number_to_sum + ord(value)) > 122:
        cypher_string += "{}".format(chr(97 + number_to_sum - 1 -(122 - ord(value))))
      else:
        cypher_string += "{}".format(chr(ord(value) + number_to_sum))
    elif 57 >= ord(value) >= 48:
      number_to_sum = umber_to_sum = rotation_factor % 10
      if (number_to_sum + ord(value)) > 57:
        cypher_string += "{}".format(chr(48 + number_to_sum - 1 -(57 - ord(value))))
      else:
        cypher_string += "{}".format(chr(ord(value) + number_to_sum))
    else:
      cypher_string += "{}".format(value)
  return cypher_string

cypher_string = rotationalCipher("All-convoYs-9-be:Alert1.", 4)
print(cypher_string)