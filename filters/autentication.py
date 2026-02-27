from filter import *

class Autentication(Filter):

    def execution(self, id):
        print('Autentication is OK for'+ id)

if __name__ == '__main__':
    
    autentication = Autentication()
    autentication.execution('xXPacoStarXx')