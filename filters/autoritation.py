from filter import *

class Autoritation(Filter):

    def execution(self, id):
        print('Autoritation is OK for'+ id)

if __name__ == '__main__':
    
    autoritation = Autoritation()
    autoritation.execution('xXPacoStarXx')