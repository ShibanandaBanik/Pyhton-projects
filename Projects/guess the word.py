import random
words = ('leather','eat','create','phone','python')

chance = 3


def main():

     global chance

     while chance != 0:
          chosen_word = random.choice(words)
          if chosen_word =='leather':
               print("Obtained from an animal and used in accessories.")
               uinput = input('Enter word:')
               if uinput == chosen_word:
                    print('congratulations')
               else:
                    print('try again')
                    chance = chance - 1
                    print(f'you have {chance} chances left')
          elif chosen_word == 'eat':
               print('A verb with 3 letters only.')
               uinput = input('Enter word:')
               if uinput == chosen_word:
                    print('congratulations')
               else:
                    print('try again')
                    chance = chance - 1
                    print(f'you have {chance} chances left')
          elif chosen_word == 'create':
               print('To make somrthing')
               uinput = input('Enter word:')
               if uinput == chosen_word:
                    print('congratulations')
               else:
                    print('try again')
                    chance = chance - 1
                    print(f'you have {chance} chances left')
          elif chosen_word == 'phone':
               print('Used for communications.')
               uinput = input('Enter word:')
               if uinput == chosen_word:
                    print('congratulations')
               else:
                    print('try again')
                    chance = chance - 1
                    print(f'you have {chance} chances left')
          elif chosen_word == 'python':
               print('The language ChatGPT is built with.')
               uinput = input('Enter word:')
               if uinput == chosen_word:
                    print('congratulations')
               else:
                    print('try again')
                    chance = chance - 1
                    print(f'you have {chance} chances left')
          

main()