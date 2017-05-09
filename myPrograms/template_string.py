#!/usr/bin/env
# -*- coding:gbk -*-
import string

form = string.Template("""\
Dear $name,
Please send back my $item or pay me $amount
otherwise, I am not gonna take actions.
Yours sincerely,
$sender
""")
formatter = {'name': 'Mr.John', 'item': 'bluetooth speaker',
            'amount': '500.00', 'sender': 'Shaofeng Zhang'}

print(form.substitute(**formatter))
print(form.substitute(formatter))  # this also works

encoding_codecs = ['utf-8', 'ascii', 'big5', 'gb2312',
                   'gbk', 'utf-16', 'unicode-escape',
                   'raw-unicode-escape']

source_string = "少峰很厉害"

for i in encoding_codecs:
    try:
        decoded_string = source_string.decode(i)
        print("\033[1;36m decoded_string.%s : %r\033[0m" % (i, repr(decoded_string)))
    except UnicodeDecodeError:
        print("\033[1;31m %s can not decode %r \033[0m" % (i, repr(source_string)))
