def convert():
  bad = ["а", "о", "про", "об", "от", "до", "и", "но", "для", "из", "то", "у", "за"]
  very_bad = ["с", "в", "к"]
  syllables = []
  words_in_line = []
  print("Начинаем")
  line = int(input())
  wordlist = []
  append = open("da.txt", "a", encoding='utf-8')  
  read = open("da.txt", encoding="utf-8").read().split("\n")
  #print(read)
  glasniy = "ауеыоэяиюё"
  for i in range(line):
      line_read = input().lower().split()
      words_in_line.append(len(line_read))
      for word in line_read:
        wordlist.append(''.join(filter(lambda c: c.isalpha(), word)))

  arrays = []
  for i in range(len(read)):
    arrays.append(read[i][read[i].find(" ") + 1:])
    read[i] = read[i][:read[i].find(" ")] 
  for word in wordlist:
      syllable = []
      if word not in read and word not in bad and word not in very_bad:
            print("Введите, пожалуйста, ударение слова", word, "(пример: клОун).")
            s = input()
            arr = []
            for g in s:
              if g.lower() == g and g.lower() in glasniy:
                arr.append('0')
              elif g.lower() != g and g.lower() in glasniy:
                arr.append('1')
            append_str = word + " [" +  ', '.join(arr) + "]\n" 
            #print(append_str)
            #append_str = arr.join()
            append.write(append_str)
            read.append(word)
            arrays.append(arr)
            #print(arrays)
            for g in arr:
              syllable.append(g)
      elif word in read and word not in bad and word not in very_bad:
            for g in range(len(read)):

              if word == read[g]:
                #print(type(arrays[g][1:-1]))
                for q in arrays[g][1:-1].split(", "):
                  syllable.append(q)
      elif word not in very_bad:
          syllable.append("0")
      syllables.append(syllable)
  endd = 0
  index1 = []
  end_array = []
  indx = 0
  while indx < len(words_in_line): 
    for i in range(words_in_line[indx]):
      index1 = index1 + syllables[endd]
      endd += 1
    end_array.append(index1)
    index1 = []
    indx += 1
  append.close()
  for i in end_array:
    print(i)
  return end_array, line

def check (slogi):
    an = True
    am = True
    d = True
    h = True
    y = True
    for i in range(0, len(slogi), 3):
        if slogi[i] == '1':
            an = False
            am = False
    for i in range(1, len(slogi), 3):
        if slogi[i] == '1':
            d = False
            an = False
    for i in range(2, len(slogi), 3):
        if slogi[i] == '1':
            d = False
            am = False
    for i in range(0, len(slogi), 2):
        if slogi[i] == '1':
            y = False
    for i in range(1, len(slogi), 2):
        if slogi[i] == '1':
            h = False
    #print("daktil", d, "anapest", an, "amfibrahi", am, "horei", h, "yamb", y)
    if (d == True and am == True and an == True and y == True and h == True):
        return "А где ударения? ._."
    elif (d == True):
        return "Дактиль."
    elif (am == True):
        return "Амфибрахий."
    elif (an == True):
        return "Анапест."
    elif (y == True):
        return "Ямб."
    elif (h == True):
        return "Хорей."
    else:
        return "Иррегулярный размер. 'Опять что то невразумительное. Неужели нельзя без этих фокусов?'"

def check_2 (a):
    for i in a:
        if i.count('0') // i.count('1') <= 2:
            return 2
        else:
            return 3

#print("Двух/Трех сложный", check_2(test_2d))
test_2d, n = convert()
#print("Convert done")

if check_2(test_2d) == 2:
    for i in test_2d:
        if len(i) % 2 == 1:
            i.pop(len(i) - 1)
else:
    for i in test_2d:
        if len(i) % 3 == 1:
            #print("Удаляем 1 символ")
            i.pop(len(i) - 1)
        if len(i) % 3 == 2:
            #print("Удаляем 2 символа")
            i.pop(len(i) - 1)
            i.pop(len(i) - 2)

#for i in range(n):
    #print("Строка номер", i, test_2d[i])

for i in range(n):
    #print("Строка:", test_2d[i])
    print(check(test_2d[i]))
