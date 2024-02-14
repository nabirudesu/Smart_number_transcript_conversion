def match_ones(dinar_number,repetetif_ones_words):
    match dinar_number:
        case 0:
            return('صفر')
        case 1:
            return(repetetif_ones_words[0])
        case 2:
            return(repetetif_ones_words[1])
        case 3:
            return(repetetif_ones_words[2])
        case 4:
            return(repetetif_ones_words[3])
        case 5:
            return(repetetif_ones_words[4])
        case 6:
            return(repetetif_ones_words[5])
        case 7:
            return(repetetif_ones_words[6])
        case 8:
            return(repetetif_ones_words[7])
        case 9:
            return(repetetif_ones_words[8])
    print('أحاد')
def match_tens(dinar_number,repetetif_ones_words,repetitif_tens_words):
    match dinar_number:
        case 10:
            return(repetetif_ones_words[9])
        case 11:
            return(repetetif_ones_words[10])
        case 12:
            return(repetetif_ones_words[11])
        case _ if dinar_number < 10:
            return(match_ones(dinar_number,repetetif_ones_words))
        case _:
            match dinar_number / 10:
                case 1:
                    return(repetitif_tens_words[0])
                case 2:
                    return(repetitif_tens_words[1])
                case 3:
                    return(repetitif_tens_words[2])
                case 4:
                    return(repetitif_tens_words[3])
                case 5:
                    return(repetitif_tens_words[4])
                case 6:
                    return(repetitif_tens_words[5])
                case 7:
                    return(repetitif_tens_words[6])
                case 8:
                    return(repetitif_tens_words[7])
                case 9:
                    return(repetitif_tens_words[8])   
                case _:
                    match dinar_number // 10:
                        case 1:
                            return(match_ones(dinar_number%10,repetetif_ones_words)+' '+repetitif_tens_words[0])
                        case 2:
                            return(match_ones(dinar_number%10,repetetif_ones_words)+' و '+repetitif_tens_words[1])
                        case 3:
                            return(match_ones(dinar_number%10,repetetif_ones_words)+' و '+repetitif_tens_words[2])
                        case 4:
                            return(match_ones(dinar_number%10,repetetif_ones_words)+' و '+repetitif_tens_words[3])
                        case 5:
                            return(match_ones(dinar_number%10,repetetif_ones_words)+' و '+repetitif_tens_words[4])
                        case 6:
                            return(match_ones(dinar_number%10,repetetif_ones_words)+' و '+repetitif_tens_words[5])
                        case 7:
                            return(match_ones(dinar_number%10,repetetif_ones_words)+' و '+repetitif_tens_words[6])
                        case 8:
                            return(match_ones(dinar_number%10,repetetif_ones_words)+' و '+repetitif_tens_words[7])
                        case 9:
                            return(match_ones(dinar_number%10,repetetif_ones_words)+' و '+repetitif_tens_words[8])                

def match_hundreds(dinar_number,repetetif_ones_words,repetitif_tens_words,repetitif_hundreds_words):
    if dinar_number<100:
        return(match_tens(dinar_number,repetetif_ones_words,repetitif_tens_words))
    else:
        match dinar_number / 100:
            case 1:
                return(repetitif_hundreds_words[0])
            case 2:
                return(repetitif_hundreds_words[1])
            case 3:
                return(repetitif_hundreds_words[2])
            case 4:
                return(repetitif_hundreds_words[3])
            case 5:
                return(repetitif_hundreds_words[4])
            case 6:
                return(repetitif_hundreds_words[5])
            case 7:
                return(repetitif_hundreds_words[6])
            case 8:
                return(repetitif_hundreds_words[7])
            case 9:
                return(repetitif_hundreds_words[8])   
            case _:
                match dinar_number//100:
                    case 1:
                        return(repetitif_hundreds_words[0]+' و '+match_tens(dinar_number%100,repetetif_ones_words,repetitif_tens_words))
                    case 2:
                        return(repetitif_hundreds_words[1]+' و '+match_tens(dinar_number%100,repetetif_ones_words,repetitif_tens_words))
                    case 3:
                        return(repetitif_hundreds_words[2]+' و '+match_tens(dinar_number%100,repetetif_ones_words,repetitif_tens_words))
                    case 4:
                        return(repetitif_hundreds_words[3]+' و '+match_tens(dinar_number%100,repetetif_ones_words,repetitif_tens_words))
                    case 5:
                        return(repetitif_hundreds_words[4]+' و '+match_tens(dinar_number%100,repetetif_ones_words,repetitif_tens_words))
                    case 6:
                        return(repetitif_hundreds_words[5]+' و '+match_tens(dinar_number%100,repetetif_ones_words,repetitif_tens_words))
                    case 7:
                        return(repetitif_hundreds_words[6]+' و '+match_tens(dinar_number%100,repetetif_ones_words,repetitif_tens_words))
                    case 8:
                        return(repetitif_hundreds_words[7]+' و '+match_tens(dinar_number%100,repetetif_ones_words,repetitif_tens_words))
                    case 9:
                        return(repetitif_hundreds_words[8]+' و '+match_tens(dinar_number%100,repetetif_ones_words,repetitif_tens_words))

def match_thousands(dinar_number,repetetif_ones_words,repetitif_tens_words,repetitif_hundreds_words,repetitif_thousands_words):
    match dinar_number/1000:
        case 1:
            return(repetitif_thousands_words[0])
        case 2:
            return(repetitif_thousands_words[1])
        case 3:
            return(repetetif_ones_words[2]+''+repetitif_thousands_words[3])
        case 4:
            return(repetetif_ones_words[3]+''+repetitif_thousands_words[3])
        case 5:
            return(repetetif_ones_words[4]+''+repetitif_thousands_words[3])
        case 6:
            return(repetetif_ones_words[5]+''+repetitif_thousands_words[3])
        case 7:
            return(repetetif_ones_words[6]+''+repetitif_thousands_words[3])
        case 8:
            return(repetetif_ones_words[7]+''+repetitif_thousands_words[3])
        case 9:
            return(repetetif_ones_words[8]+''+repetitif_thousands_words[3])
        case _:
            match dinar_number//1000:
                case 1:
                    return(repetitif_thousands_words[0]+' و '+match_hundreds(dinar_number%1000,repetetif_ones_words,repetitif_tens_words,repetitif_hundreds_words))
                case 2:
                    return(repetitif_thousands_words[1]+' و '+match_hundreds(dinar_number%1000,repetetif_ones_words,repetitif_tens_words,repetitif_hundreds_words))
                case 3:
                    return(repetetif_ones_words[2]+' '+repetitif_thousands_words[3]+' و '+match_hundreds(dinar_number%1000,repetetif_ones_words,repetitif_tens_words,repetitif_hundreds_words))
                case 4:
                    return(repetetif_ones_words[3]+' '+repetitif_thousands_words[3]+' و '+match_hundreds(dinar_number%1000,repetetif_ones_words,repetitif_tens_words,repetitif_hundreds_words))
                case 5:
                    return(repetetif_ones_words[4]+' '+repetitif_thousands_words[3]+' و '+match_hundreds(dinar_number%1000,repetetif_ones_words,repetitif_tens_words,repetitif_hundreds_words))
                case 6:
                    return(repetetif_ones_words[5]+' '+repetitif_thousands_words[3]+' و '+match_hundreds(dinar_number%1000,repetetif_ones_words,repetitif_tens_words,repetitif_hundreds_words))
                case 7:
                    return(repetetif_ones_words[6]+' '+repetitif_thousands_words[3]+' و '+match_hundreds(dinar_number%1000,repetetif_ones_words,repetitif_tens_words,repetitif_hundreds_words))
                case 8:
                    return(repetetif_ones_words[7]+' '+repetitif_thousands_words[3]+' و '+match_hundreds(dinar_number%1000,repetetif_ones_words,repetitif_tens_words,repetitif_hundreds_words))
                case 9:
                    return(repetetif_ones_words[8]+' '+repetitif_thousands_words[3]+' و '+match_hundreds(dinar_number%1000,repetetif_ones_words,repetitif_tens_words,repetitif_hundreds_words))

def match_ten_thousands(dinar_number,repetetif_ones_words,repetitif_tens_words,repetitif_hundreds_words,repetitif_thousands_words):
    if dinar_number<10000:
        return(match_thousands(dinar_number,repetetif_ones_words,repetitif_tens_words,repetitif_hundreds_words,repetitif_thousands_words))
    if dinar_number == 10000:
        return(repetetif_ones_words[9]+' '+repetitif_thousands_words[3])
    elif 10000< dinar_number<11000:
        return(match_tens(dinar_number//1000,repetetif_ones_words,repetitif_tens_words)+' '+repetitif_thousands_words[3]+' و '+match_hundreds(dinar_number%1000,repetetif_ones_words,repetitif_tens_words,repetitif_hundreds_words))
    elif dinar_number%1000 ==0:
        return(match_tens(dinar_number//1000,repetetif_ones_words,repetitif_tens_words)+' '+repetitif_thousands_words[0])
    else:
        return(match_tens(dinar_number//1000,repetetif_ones_words,repetitif_tens_words)+' '+repetitif_thousands_words[0]+' و '+match_hundreds(dinar_number%1000,repetetif_ones_words,repetitif_tens_words,repetitif_hundreds_words))

def match_hundered_thousands(dinar_number,repetetif_ones_words,repetitif_tens_words,repetitif_hundreds_words,repetitif_thousands_words):
    if dinar_number%100000==0:
        return(match_hundreds((dinar_number//100000)*100,repetetif_ones_words,repetitif_tens_words,repetitif_hundreds_words)+' ألف ')
    if dinar_number%100000<1000:
        return(match_hundreds((dinar_number//100000)*100,repetetif_ones_words,repetitif_tens_words,repetitif_hundreds_words)+' ألف و '+match_hundreds(dinar_number%100000,repetetif_ones_words,repetitif_tens_words,repetitif_hundreds_words))
    else:
        return(match_hundreds((dinar_number//100000)*100,repetetif_ones_words,repetitif_tens_words,repetitif_hundreds_words)+' و '+match_ten_thousands(dinar_number%100000,repetetif_ones_words,repetitif_tens_words,repetitif_hundreds_words,repetitif_thousands_words))
    


def dinar_number_to_arabic_words(dinar_number):
    repetetif_ones_words=['واحد','اثنان','ثلاثة','أربعة','خمسة','ستة','سبعة','ثمانية','تسعة','عشرة','أحد عشر','اثنا عشر']
    repetitif_tens_words=['عشر','عشرون','ثلاثون','أربعون','خمسون','ستون','سبعون','ثمانون','تسعون']
    repetitif_hundreds_words=['مائة','مئتان','ثلاثمائة','أربعمائة','خمسمائة','ستمائة','سبعمائة','ثمانمائة','تسعمائة']
    repetitif_thousands_words=['ألف','الفان','ألفا','آلاف']
    repetitif_millions_words=['مليون','مليونا','ملايين']
    repetitif_billions_words=['مليار','مليارا','مليارات']
    # we use the lenght of the number to determin the method we'll use
    match len(str(dinar_number)):
        case 1:
            print(match_ones(dinar_number,repetetif_ones_words))
        case 2:
            print(match_tens(dinar_number,repetetif_ones_words,repetitif_tens_words))
            print('عشرات')
        case 3:
            print(match_hundreds(dinar_number,repetetif_ones_words,repetitif_tens_words,repetitif_hundreds_words))
            print('مئات')
        case 4:
            print(match_thousands(dinar_number,repetetif_ones_words,repetitif_tens_words,repetitif_hundreds_words,repetitif_thousands_words))
            print('آلاف')
        case 5:
            print(match_ten_thousands(dinar_number,repetetif_ones_words,repetitif_tens_words,repetitif_hundreds_words,repetitif_thousands_words))
            print('عشرات الآلاف')
        case 6:
            print(match_hundered_thousands(dinar_number,repetetif_ones_words,repetitif_tens_words,repetitif_hundreds_words,repetitif_thousands_words))
            print('مئات الآلاف')
        case 7:
            print('ملايين')
        case 8:
            print('عشرات الملايين')
    
    ones=1
    tens=10
    hundreds=100
    thousands=1000
    ten_thousands=10000
    hundred_thousands=100000
    miliions=1000000
    ten_millions=10000000    
    
    #"hundred_millions=100000000   biliions=1000000000    ten_biliions=10000000000    hundred_biliions=100000000000"

dinar_number=int(input("entre a number between 1 and 999 : \n"))

dinar_number_to_arabic_words(dinar_number)