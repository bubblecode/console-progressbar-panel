
class COM_HEADER_LINE():
    def __init__(self, inner_width):
        self.inner_width = inner_width
    def __str__(self):
        return '.'+'_'*self.inner_width+'.'

class COM_MARK_SPLIT():
    def __init__(self, inner_width, mark=' '):
        self.inner_width = inner_width
        self.mark = mark
    def __str__(self):
        return '|'+self.mark*self.inner_width+'|'

class COM_INFORMATION():
    def __init__(self, inner_width):
        self.inner_width = inner_width
    
    def update(self, key, value):
        line_data = ' {} {}'.format(key ,value)
        return '|'+line_data+' '*(self.inner_width-len(line_data))+'|'
    def __str__(self):
        return 'This is a dynamic value component, you can use the .update(key, value) method instead'

class COM_STATIC_INFO():
    def __init__(self, inner_width, k, v):
        self.inner_width = inner_width
        self.key = k
        self.value = v
    def __str__(self):
        line_data = ' {} {}'.format(self.key ,self.value)
        return '|'+line_data+' '*(self.inner_width-len(line_data))+'|'

class COM_MODULE_SPLIT_LINE():
    def __init__(self, inner_width, info: str):
        self.inner_width = inner_width
        self.__info = info
    def __str__(self):
        tmp = '-'*int((self.inner_width-len(self.__info))/2) + self.__info
        return '|'+tmp+'-'*(self.inner_width-len(tmp))+'|'
