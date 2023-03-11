# from html.parser import HTMLParser
# h = HTMLParser()
# h.unescape('수입&#40;사용소비&#41; 심사진행')

import html

print(html.unescape('수입&#40;사용소비&#41; 심사진행'))