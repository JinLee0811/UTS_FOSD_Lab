def vowel_count(segement):
    count = 0
    for c in segement:
        if c in "aeiou":
            count += 1
    return count


def match(
    word,
):  # z를 기준으로 쪼개고 그 뒤에 모음이 2개 있을경우 True 뱉고 False로 종료
    for segement in word.split("z"):
        if vowel_count(segement) == 2:
            return True
    return False


def word_count(sentence):  # 공백을 기준으로 쪼개기
    count = 0
    for word in sentence.split(" "):
        if match(word):
            count += 1
    return count


def show_match():  # 받은 인풋을 일단 소문자로 바꾸고 위의 함수 과정 진행
    sentence = input("Sentence: ")

    while sentence != "*":
        print(f"Matching words = {word_count(sentence.lower())}")
        sentence = input("Sentence: ")


show_match()
