# Bem-Vindo(a)

### 👑 Documentação - Word Puzzle Game

#### Importações

A primeira coisa feita foi alterar a posição do import para o início do código. Mesmo que não cause nenhum problema específico, é uma boa prática deixar importações sempre no início.

```bash
#Program: CSE 110 - W04 Prove - Word Puzzle
#Author: Bruno de Sousa Teixeira

import random
```

### Início do código
#### Guess

A variável `guess` foi deletada, pois com as atualizações feitas, ela não será mais necessária.

```diff
- guess = ""
```

#### Hint
A variável `hint` foi alterada de Tupla para Lista.

```diff
- hint = (" _ ") *len(secret_word)
+ hint = ["_"] * len(secret_word) 
```

Como vamos fazer alterações na lista durante a execução do código, não poderiamos deixar ela como Tupla.

#### Exibição das dicas

Como removemos da variavel `hint` os espaços que ficavam entre os underlines, foi usado o método `join`, que funciona da seguinte forma:

```diff
- print(f"Your hint is{hint}")
+ print(f"Your hint is {" ".join(hint)} ({len(secret_word)} letters)")
```

O join pega todos os elementos da lista `hint` e coloca numa única string, colocando um delimitador entre eles, que nesse caso foi definido como o espaço "` `", se fosse colocado um `, `, por exemplo, o resultado seria: "_, _, _, _, _" <br>
Além disso, eu coloquei a quantia de letras da palavras, mas é mais pra melhorar a legibilidade, pode ser removido sem problemas.

### Entrando no while

#### Estrutura

Uma das alterações foi no while

```diff
- while guess != secret_word:
+ while True:
```

Como removemos a variável guess, essa parte teve de ser atualizada. <br>
Além disso, maior alteração foi em como o código estava organizado e a remoção dos `elif` <br>
Primeiro, a parte de verificar se a pessoa digitou `quit` foi colocada abaixo da variável `guess`, porque o código primeiro verificava se a palavra digitada era igual à palavra secreta, mas caso a pessoa digitasse `quit` seria uma verificação inútil. E, como na verificação do quit tem um `break`, não precisamos verificar a cada iteração se a variável `guess` é diferente da variável `secret_word`

```diff
- guess = input("What is your guess? ").lower()
- if secret_word == guess:
-    print(f"Congratulations! The secret word was {secret_word}.")
-    if guess_count == 1:
-      print("You took just 1 guess! ")
-    else:
-      print(f"You took {guess_count} guesses. ")
-
-  elif guess == "quit":
-    print("Thank you for playing with us. Bye! ")
-    break

+    guess = input("What is your guess? ").lower()
+  
+    if(guess == "quit"):
+        print("Thank you for playing with us. Bye! ")
+        break
```

Outra alteração foi na parte de verificar se a quantia de letras na palavra digitada é igual a quantia de letras na palavra secreta. Antes, o código tinha um input dentro do elif para o usuário digitar a palavra novamente, mas estava dando um problema do código pedir para digitar a palavra duas vezes. Para resolver isso, removemos a parte do input e a adição no `guess_count`

```diff
-  elif len(guess) != len(secret_word):
-    print(f"Your guess must be {len(secret_word)} letters long. Try again")
-    guess = input("What is your guess? ").lower()
-    guess_count += 1
```

Após isso ser removido, colocamos no lugar das duas ultimas linhas a instrução `continue`, ele para a iteração atual que está sendo realizada e vai para a próxima iteração, ou seja, ele para a execução do código e volta para o início do while, então qualquer código que venha depois do `continue` não será executado. Como nós já temos uma variável `guess` que pega uma palavra pelo input, o `continue` funciona perfeitamente.

```diff
+ if(len(guess) != len(secret_word)):
+        print(f"Your guess must be {len(secret_word)} letters long. Try again")
+        continue
```

Saindo desse bloco, adicionamos na quantia de palpites realizados mais 1

```diff
+ guess_count += 1 
```

Então, até agora nosso while está assim:

```bash
    while True:
        guess = input("What is your guess? ").lower()
    
        if(guess == "quit"):
            print("Thank you for playing with us. Bye! ")
            break
    
        if(len(guess) != len(secret_word)):
            print(f"Your guess must be {len(secret_word)} letters long. Try again")
            continue
    
        guess_count += 1 
```

Agora, está faltando fazer a verificação se a palavra digitada é igual a palavra secreta, e comparado ao código original, praticamente nada foi alterado

```diff
if secret_word == guess:
    print(f"Congratulations! The secret word was {secret_word}.")
    if guess_count == 1:
        print("You took just 1 guess! ")
    else:
        print(f"You took {guess_count} guesses. ")
+   break
```

Única coisa adicionada foi o `break` porque como tiramos a verificação do while, será ele quem vai parar a execução do código se o jogador acertar a palavra.

#### Atualização das dicas

Agora, a maior alteração. Antes, era mostrado usando vários prints quais letras estavam corretas ou quais letras existiam na palavra, mas estavam no local incorreto, agora, nós vamos fazer isso tudo pela variável `hint`

```bash
    for i, letter in enumerate(guess):
```

Essa parte continua o mesmo

```bash
    if(guess[i] == secret_word[i]):
        hint[i] = letter.upper()
```

Primeiro, é verificado se a letra na posição da palavra digitada `i` é igual a letra na posição `i` da `secret_word`. Se for, ele altera o elemento na posição `i` da variável `hint` para a letra correta.

```bash
    elif letter in secret_word and guess[i] != secret_word[i]:
        if hint[i] != letter.upper():
            hint[i] = letter.lower()
```

Essa parte é executada quando a letra não está na posição correta, mas pode ser que ela exista na palavra. Primeiro, o elif verifica se a letra está presente em qualquer posição da palavra e depois confirma que a letra não está na posição correta. Se essas duas condições forem verdadeiras, ele faz outra verificação para ver se a letra que está na mesma posição nas dicas, é maiuscula. Se for maiuscula, quer dizer que a letra já tinha sido encontrada anteriormente, então não podemos alterá-la. Se a condição for falsa, o código coloca na posição `i` das dicas a letra em minúscula para indica ao jogador que a letra está na palavra secreta, mas não na posição correta. <br>
Por último, nós saimos do bloco for e colocamos a dica no console

```bash
    print(f"Your hint is: {" ".join(hint)}")
```

O código completo fica

```bash
    if secret_word == guess:
        print(f"Congratulations! The secret word was {secret_word}.")
        if guess_count == 1:
            print("You took just 1 guess! ")
        else:
            print(f"You took {guess_count} guesses. ")
        break
    else:
        print("Your guess was incorrect! ")

        for i, letter in enumerate(guess):
            if(guess[i] == secret_word[i]):
                hint[i] = letter.upper()
            elif letter in secret_word and guess[i] != secret_word[i]:
                if hint[i] != letter.upper():
                    hint[i] = letter.lower()

        print(f"Your hint is: {" ".join(hint)}")
```

## Visão geral das alterações

```diff
#Program: CSE 110 - W04 Prove - Word Puzzle
#Author: Bruno de Sousa Teixeira

+ import random

print("Welcome to the Word Puzzle Game!")
print("I have a secret word that you need to find out what it is!")
+ print("Uppercase letter = correct position")
+ print("Lowercase letter = exists, but not in the correct position\n")

secret_words = ("newsletter", "office", "garbage", "mortgage", "advice", "selfish", "happiness", "squirrel", "character", "jaguar", "apple", "computer", "giraffe", "airplane", "school")

secret_word = random.choice(secret_words)
guess_count = 0
- guess = ""
- hint = (" _ ") *len(secret_word)
+ hint = ["_"] * len(secret_word) 

- print(f"Your hint is{hint}")
+ print(f"Your hint is {" ".join(hint)} ({len(secret_word)} letters)")

- while guess != secret_word:
+ while True:
    guess = input("What is your guess? ").lower()
  
+   if(guess == "quit"):
+       print("Thank you for playing with us. Bye! ")
+       break
+  
+   if(len(guess) != len(secret_word)):
+       print(f"Your guess must be {len(secret_word)} letters long. Try again")
+       continue
+  
+   guess_count += 1 

+   if secret_word == guess:
+       print(f"Congratulations! The secret word was {secret_word}.")
+       if guess_count == 1:
+           print("You took just 1 guess! ")
+       else:
+           print(f"You took {guess_count} guesses. ")
+       break
+   else:
+       print("Your guess was incorrect! ")
+
+       for i, letter in enumerate(guess):
+           if(guess[i] == secret_word[i]):
+               hint[i] = letter.upper()
+           elif letter in secret_word and guess[i] != secret_word[i]:
+               if hint[i] != letter.upper():
+                   hint[i] = letter.lower()
+
+       print(f"Your hint is: {" ".join(hint)}")
```