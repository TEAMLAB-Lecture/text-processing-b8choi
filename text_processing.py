#######################
# Test Processing I   #
#######################

"""
NLP에서 흔히하는 전처리는 소문자 변환, 앞뒤 필요없는 띄어쓰기를 제거하는 등의 텍스트 정규화 (text normalization)입니다. 
이번 숙제에서는 텍스트 처리 방법을 파이썬으로 배워보겠습니다. 
"""


def normalize(input_string):
    input_string = input_string.lower().strip()

    normalized_string = ''
    if input_string != '':
        words = input_string.split()
        for s in words[:-1]:
            normalized_string += s + ' '
        normalized_string += words[-1]

    return normalized_string


def no_vowels(input_string):
    vowels = 'aeiouAEIOU'

    no_vowel_string = ''
    for c in input_string:
        if c not in vowels:
            no_vowel_string += c

    return no_vowel_string
