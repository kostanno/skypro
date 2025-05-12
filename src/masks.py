from typing import Union

from unicodedata import numeric


def mask_account_card(get_mask_card):
    num = ""
    byk = ""
    for i in get_mask_card:
        if  i.isdigit():
            num+=i
        if   i.isalpha():
            byk+=i
    return byk,num




def get_mask_account(get_card:str)-> str:


    return  f'{byk} {num[:4]} {num[5:7] + 2 * "*"} {4 * "*"} {num[-4:]}'
        # else:
        #      len(get_card) == 20:
        #           return  f'{byk} {2 * "*" + num[-4:]}'



# sa=mask_account_card("Visa Platinum 7000792289606361")
sds=get_mask_account("Visa Platinum 7000792289606361")
print(sds)



#
#
# def get_mask_card_number(num_card: Union[int]) -> str:
#     """функция маскировки номера банковской карты"""
#     mask_num_card = str(num_card)

#     if len(mask_num_card) == 16:
#         return (f"{mask_num_card[:4]} {mask_num_card[5:7] + 2 * "*"} {4 * "*"} {mask_num_card[-4:]}")
#     else:
#         return (f"Неправильный ввод вы ввели {len(mask_num_card)} цифр")


# def get_date(date):
#     new_date=date[:10]
#
#     return "".join(reversed(new_date))
#
# a=get_date("2024-03-11T02:26:18.671407")
# print(a)


