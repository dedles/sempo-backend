import numpy

# priv_key = "0x872d2472f24263877d0418f7463b631589e12322d4955d99009e605d007f37b6"
# b29_string = "5ES4LLB39EGGOMHOOC282S7N6FKBF92BR1DRNN09QB29NLSENA54F"
# emojis = '🍀🌼🌜🌎🌟🔥🌩❄️🌊😂😃😎😚🤗😮😬😱😇😈👹💀👻👽🤖😽🚀🎉♻️☎️🔮'

# em_key = "❄️😂🎉♻️🎉🤖👹🔮🌩👹😇😱🔥👻😮😃😚💀🍀😂🌊🌜🤗❄️🌎👹😃😚👹🍀😬🌼💀❄️😽🌼🎉👹🌎🌟🚀🌎🤖🍀🌎🍀👽😇🔥😇🔥😽🌩"

key_prefix = '0x'

b29_emoji_dict = {
    "0": "🍀",
    "1": "🌼",
    "2": "🌜",
    "3": "🌎",
    "4": "🌟",
    "5": "🔥",
    "6": "🌩",
    "7": "🌭",
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
    "R": "🌮",
    "S": "🔮"
} 

def convert_hex_to_b10(hex):
    return int(hex, 16)
    
def convert_b10_to_b29(b10):
    base29 = numpy.base_repr(b10, 29)
    return base29

def convert_b29_to_b10(b29):
    return int(b29, 29)

def convert_b10_to_hex(b10):
    return numpy.base_repr(b10, 16).lower()


def convert_b29_to_emoji(b29):
    arr = list(b29)
    em_string = ''
    for char in arr:
        em_string += b29_emoji_dict[char]
    return em_string

def convert_emoji_to_b29(em_string):
    arr = list(em_string)
    alnum = ''
    for char in arr:
        for key, value in b29_emoji_dict.items():
            if char == value:
                alnum += str(key)
    return alnum

def convert_key_to_emoji(key):
    key_arr = key.split(key_prefix)
    b10 = convert_hex_to_b10(key_arr[1])
    b29 = convert_b10_to_b29(b10)
    return convert_b29_to_emoji(b29)

def decrypt_emoji(em_key):
    b29 = convert_emoji_to_b29(em_key)
    base10 = convert_b29_to_b10(b29)
    hex = convert_b10_to_hex(base10)
    return key_prefix + hex
