import os
import platform
from .component import *
class ProgressBar():
    def __init__(self, name, total_length, inner_width=29, moniter=[], **kwargs):
        self.__total = total_length
        self.__total = total_length
        self.__moniter = dict(zip(moniter, ['' for i in moniter]))
        self.__paramdict = kwargs
        self.inner_width = inner_width
        self.__len_progress = self.inner_width-2-1-len(str(total_length))*2-1
        self.__cla = 'clear' if platform.system().upper() == 'LINUX' else 'cls'
        # initialization module
        self.header = COM_HEADER_LINE(self.inner_width)
        self.blank  = COM_MARK_SPLIT(self.inner_width, mark=' ')
        self.line   = COM_MARK_SPLIT(self.inner_width, mark='_')
        self.info   = COM_INFORMATION(self.inner_width)
        self.s_moniter= COM_MODULE_SPLIT_LINE(self.inner_width, 'moniter')
        self.s_parameter= COM_MODULE_SPLIT_LINE(self.inner_width, 'parameter')
        self.name = COM_STATIC_INFO(self.inner_width, 'name', name)
        self.params = []
        for k in kwargs.keys():
            self.params.append(COM_STATIC_INFO(self.inner_width, k, kwargs[k]))
    def update(self, i, **monite):
        if i > self.__total:
            i = self.__total
        progress = round((i/self.__total)*self.__len_progress)
        os.system(self.__cla)
        print(self.header)
        print(self.name)
        print(self.s_parameter)
        for pa in self.params:
            print(pa)
        print(self.blank)
        print(self.s_moniter)
        for j in monite.keys():
            assert j in self.__moniter.keys(), 'Error: There is no variable named {}.'.format(j)
            print(self.info.update(j, monite[j]))
        print(self.line)
        str_progress = '['+'='*progress+'-'*(self.__len_progress-progress)+'] {}/{}'.format(i, self.__total)
        print('\r|'+str_progress+' '*(self.inner_width-len(str_progress))+'|')
        print(self.line)
    def __len__(self):
        return self.__total + 1
