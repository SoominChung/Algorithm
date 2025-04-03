def solution(phone_book):
    phone_book = sorted(phone_book,key=lambda x: int(x))
    min_len = min(list(map(lambda x: len(x),phone_book)))
    max_len = max(list(map(lambda x: len(x),phone_book)))
    for length in range(min_len,max_len+1):
        longer_lengths = set(map(lambda x: x[:length],[i for i in phone_book if len(i)>length]))
        length_list = [i for i in phone_book if len(i) == length]
        for ll in length_list:
            if ll in longer_lengths:
                return False
    return True
