# is_a_vowel_funtion.py
def is_a_vowel(c):
  vowels = "AEIOUaeiou"  
  return c in vowels
  
if __name__ == "__main__":
  print(is_a_vowel("X"))
  print(is_a_vowel("O"))
  print(is_a_vowel("e"))