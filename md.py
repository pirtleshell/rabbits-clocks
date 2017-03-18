# markdown tid bits
def url(src, alt, title):
    img_src = src
    if title:
        img_src += ' ' + title
    return '[{}]({})'.format(alt, img_src)

def image(src, alt='', title=''):
    return '!' + url(src, alt, title)
