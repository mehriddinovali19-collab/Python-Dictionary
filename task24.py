def most_common_char(text: str) -> str:
    char_count ={} # shu yangi dict ichida har bir char ning necha marta uchraganini saqlayman
    for char in text: # text ichidagi har bir char ni tekshirib chiqaman
        if char in char_count: # agar char char_count dict ichida mavjud bo'lsa, uning qiymatini 1 ga oshiraman
            char_count[char] += 1
        else:
            char_count[char] = 1 # agar char char_count dict ichida mavjud bo'lmasa, uni dict ga qo'shaman va qiymatini 1 ga tenglayman
    most_common = max(char_count, key=char_count.get) # max funksiyasi yordamida char_count dict ichidagi eng ko'p uchragan char ni topaman, key parametri yordamida char_count.get funksiyasini chaqiraman, bu funksiya char ni qabul qiladi va uning qiymatini qaytaradi, shuning uchun max funksiyasi char_count dict ichidagi eng katta qiymatga ega bo'lgan char ni qaytaradi key = char_count.get ning vazifasi char_count dict ichidagi har bir char ning qiymatini olish va max funksiyasi yordamida eng katta qiymatga ega bo'lgan char ni topishdir, bu yerda char_count.get char ni qabul qiladi va uning qiymatini qaytaradi, shuning uchun max funksiyasi char_count dict ichidagi eng katta qiymatga ega bo'lgan char ni qaytaradi
    return most_common
text = "hello world"
print(most_common_char(text))