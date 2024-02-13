from num2words import num2words

def centime_to_dinar(centime_input):
    dinar=centime_input/100
    return dinar

def dinar_number_to_arabic_words(dinar_number):
    arabic_word= num2words(dinar_number,lang='ar')
    return arabic_word +" "+"دينار جزائري"

def arabic_words_to_voice(arabic_words):
    voice= arabic_words
    # the logic is still to be done late
    # this can be moved to another folder where we create all the voice methods
    return voice

def voice_to_arabic_words(voice):
    arabic_words=str(voice)
    # the logic is still to be done late
    # this can be moved to another folder where we create all the voice methods
    return arabic_words

