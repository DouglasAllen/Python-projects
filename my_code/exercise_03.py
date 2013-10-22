def is_a_vowel(c):
  vowels = "AEIOUaeiou"  
  return c in vowels
  
def main():
  print(is_a_vowel("X"))
  print(is_a_vowel("O"))
  print(is_a_vowel("e"))
  
if __name__ == "__main__":
  main()  