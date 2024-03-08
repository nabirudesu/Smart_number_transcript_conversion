from numbers_to_words import dinar_number_to_arabic_words
def centime_to_dinar(centime_input):
    dinar=centime_input/100
    return dinar

def numbers_to_words_conversion(dinar_number):
    arabic_word= dinar_number_to_arabic_words(dinar_number)
    return arabic_word +" "+"دينار جزائري"

def arabic_words_to_voice(arabic_words):
    voice= arabic_words
    # the logic is still to be done late
    # this can be moved to another folder where we create all the voice methods
    return voice

def voice_to_arabic_words(voice):
    arabic_words=str(voice)
    # the logic is still to be done late
    # whisper ai to transcript voice to text
    # use arabic autocorrector to correct misspelling ot wrong words 
    # extract if there is any number in the returned sentece and extract
    # convert the number extracted to words and return the full sentence
    # apply auto corrector again for any misspelling
    # verify that every word used exists in the array of words
    # this can be moved to another folder where we create all the voice methods
    return arabic_words

print(numbers_to_words_conversion(95000))
