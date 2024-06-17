encodes = [-14,5,1,19,-55,-21,2,-55,-20,11,5,10,16,-55,-3,10,11,16,4,1,14,-55,-30,14,11,9]

def generate_url(encodes=[]):
    if not encodes:
        return ""
    
    return get_char(encodes[0])[0] + generate_url(encodes[1:])
    
def get_char(encode, chars=[]):
    chars.append(chr(0o144 + encode))
    return chars

link = generate_url(encodes)
print(link)