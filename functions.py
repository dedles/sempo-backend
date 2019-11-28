import numpy

# priv_key = "0x872d2472f24263877d0418f7463b631589e12322d4955d99009e605d007f37b6"
# b29_string = "5ES4LLB39EGGOMHOOC282S7N6FKBF92BR1DRNN09QB29NLSENA54F"
# emojis = '🍀🌼🌜🌎🌟🔥🌩❄️🌊😂😃😎😚🤗😮😬😱😇😈👹💀👻👽🤖😽🚀🎉♻️☎️🔮'

# em_key = "❄️😂🎉♻️🎉🤖👹🔮🌩👹😇😱🔥👻😮😃😚💀🍀😂🌊🌜🤗❄️🌎👹😃😚👹🍀😬🌼💀❄️😽🌼🎉👹🌎🌟🚀🌎🤖🍀🌎🍀👽😇🔥😇🔥😽🌩"

b29_emoji_dict = {
    "0": "🍀",
    "1": "🌼",
    "2": "🌜",
    "3": "🌎",
    "4": "🌟",
    "5": "🔥",
    "6": "🌩",
    "7": "❄️",
    "8": "🌊",
    "9": "😂",
    "A": "😃",
    "B": "😎",
    "C": "😚",
    "D": "🤗",
    "E": "😮",
    "F": "😬",
    "G": "😱",
    "H": "😇",
    "I": "😈",
    "J": "👹",
    "K": "💀",
    "L": "👻",
    "M": "👽",
    "N": "🤖",
    "O": "😽",
    "P": "🚀",
    "Q": "🎉",
    "R": "♻️",
    "S": "🔮"
} 

def convert_key_to_emoji(key):
    key_arr = key.split('0x')
    b29 = convert_hex_to_29(key_arr[1])
    return convert_b29_to_emoji(b29)

def convert_hex_to_29(hex):
    base10 = int(hex, 16)
    base29 = numpy.base_repr(base10, 29)
    return base29

def convert_b29_to_emoji(b29):
    arr = list(b29)
    new_string = ''
    for char in arr:
        new_string += b29_emoji_dict[char]
    return new_string

def decrypt_emoji(em_key):
    arr = list(em_key)
    alnum = ''
    for char in arr:
        for key, value in b29_emoji_dict.items():
            if char == value:
                alnum += str(key)
                
    base10 = int(alnum, 29)
    hex = numpy.base_repr(base10, 16).lower()
    return '0x' + hex

# print(decrypt_emoji(em_key))
