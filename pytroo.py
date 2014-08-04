# -*- encoding: utf-8 -*-

__author__="maldicion069"
__date__ ="$Aug 4, 2014 3:42:08 AM$"

#from analyzer.lexical import LexicalAnalyzer

import re

class LexicalAnalyzer:
    
    fin = "$#$"
    prx_l = re.compile('[^\W\d_]+')
    prx_n = re.compile('^-?[0-9]+$')
    prx_del = re.compile(" |\t")
    prx_del1 = re.compile("( |\t)|\\(|\\*|\\/|\\$|\\;|\\,|\\)") 
    prx_del2 = re.compile("( |\t)|\\(|([^\W\d_]+)|(-?[0-9]+$)")
    
    def __init__(self, **kwargs):
        self.tokenActual = ""
        self.tokenLectura = ""
        self.puntero = -1
        self.listaTokens = []
        self.palabrasReservadas = set()
        self.palabrasReservadasTipo = set()
        self.palabrasReservadasProp = set()
        self.state = 0
        self.__generatestates()
        self.states = {}
        self.lineaCodigo = ""
        self.__addpr(**kwargs)
        print self.palabrasReservadas
        print self.palabrasReservadasTipo
        
    def __state0(self):
        self.__inilexema()
        self.digito = 0
        self.valor = 0
        self.tokenLectura = self.readchar()
        if self.tokenLectura == 't':
            pass
        print self.tokenActual, self.tokenLectura
        if LexicalAnalyzer.prx_del.match(self.tokenLectura):
            self.state = 0
        elif LexicalAnalyzer.prx_l.match(self.tokenLectura):
            self.state = 1
        elif self.tokenLectura == ";":
            self.state = 9
        elif self.tokenLectura == "(":
            self.state = 14
        elif self.tokenLectura == ")":
            self.state = 15
        elif LexicalAnalyzer.prx_n.match(self.tokenLectura):
            self.state = 16
        elif self.tokenLectura == "/":
            self.state = 21
        elif self.tokenLectura == ",":
            self.state = 25
           
    def __state1(self):
        self.__concatenatechar(self.tokenLectura)
        self.tokenLectura = self.readchar()
        if self.tokenLectura == 't':
            pass
        print self.tokenActual, self.tokenLectura
        if LexicalAnalyzer.prx_n.match(self.tokenLectura):
            self.state = 3
        elif LexicalAnalyzer.prx_l.match(self.tokenLectura):
            self.state = 1
        elif LexicalAnalyzer.prx_del1.match(self.tokenLectura):
            self.state = 2
            
    def __state2(self):
        self.__retrocesopuntero()
        self.__diferprid(self.__dalexema())
        self.state = 0
        
    def __state3(self):
        self.__concatenatechar(self.tokenLectura)
        self.tokenLectura = readchar()
        if ((fnmatch.fnmatch(self.tokenLectura, LexicalAnalyzer.prx_n)) or 
            (fnmatch.fnmatch(self.tokenLectura, LexicalAnalyzer.prx_l))):
            self.state = 3
        elif fnmatch.fnmatch(self.tokenLectura, LexicalAnalyzer.prx_del):
            self.state = 4
        
    def __state4(self):
        self.__datoken("TK_ID", self.__dalexema())
        self.state = 0
        
    def __state9(self):
        self.__datoken("TK_FIN_SENT", ";")
        self.state = 0
        
    def __state14(self):
        self.__datoken("TK_PAR_ABR", "(")
        self.state = 0
        
    def __state15(self):
        self.__datoken("TK_PAR_CER", ")")
        self.state = 0
        
    def __state16(self):
        self.digito = self.__tonum(self.tokenLectura)
        self.valor = self.valor * 10 + self.digito
        self.tokenLectura = self.readchar()
        if LexicalAnalyzer.prx_n.match(self.tokenLectura):
            self.state = 16
        elif LexicalAnalyzer.prx_del1.match(self.tokenLectura):
            self.state = 17
    
    def __state17(self):
        self.__retrocesopuntero()
        self.__datokenint("TK_CTE_NUM", self.valor)
        self.state = 0
        
    def __state25(self):
        self.__datoken("TK_COMMA", ",")
        self.state = 0
    
    def __generatestates(self):
        self.states = {
            0 : self.__state0,
            1 : self.__state1,
            2 : self.__state2,
            3 : self.__state3,
            4 : self.__state4,
            9 : self.__state9,
            14 : self.__state14,
            15 : self.__state15,
            16 : self.__state16,
            17 : self.__state17,
            25 : self.__state25
        }
        
    def lineanalyzer(self, line):
        self.__inilexema()
        self.lineaCodigo = line
        self.state = self.valor = self.digito = 0
        self.puntero = -1
        self.__generatestates()
        try:
            while(self.fin != self.tokenLectura):
                self.states[self.state]()   
        except:
            pass
        finally:
            self.listaTokens.append(("TK_SALIDA", "$EOF$"))
        return self.listaTokens
        
    def __inilexema(self):
        self.tokenActual = ""
        self.tokenLectura = ""
        
    def __retrocesopuntero(self):
        self.puntero -= 1
        
    def __datoken(self, lexema, contenido):
        t = (lexema, contenido)
        self.listaTokens.append(t)
        return t
    
    def __datokenint(self, lexema, valor):
        t = (lexema, valor)
        self.listaTokens.append(t)
        return t
        
    def __diferprid(self, lexema):
        if lexema in self.palabrasReservadas:
            t = ("TK_" + self.__dalexema().upper(), lexema)
        elif lexema in self.palabrasReservadasTipo:
            t = ("TK_TYPE", lexema)
        elif lexema in self.palabrasReservadasProp:
            t = ("TK_PROP", lexema)
        else:
            t = ("TK_ID", lexema)
        self.listaTokens.append(t)
    
    def __dalexema(self):
        return self.tokenActual
    
    def palabrasreservadas(self, *args):
        self.addpr(args)
        
    def showreservadas(self):
        for n in enumerate(self.palabrasReservadas):
            print n, "   ",
        print
        
    def __addpr(self, **kwargs):
        for arg in kwargs['pkey']:
            self.palabrasReservadas.add(arg.upper())
            self.palabrasReservadas.add(arg.lower())
        for arg in kwargs['type']:
            self.palabrasReservadasTipo.add(arg.upper())
            self.palabrasReservadasTipo.add(arg.lower())
        for arg in kwargs['prop']:
            self.palabrasReservadasProp.add(arg.upper())
            self.palabrasReservadasProp.add(arg.lower())
            
    def readchar(self):
        self.puntero += 1
        if len(self.lineaCodigo) > self.puntero:
            gotdata = self.lineaCodigo[self.puntero]
        else:
            gotdata = self.fin
        return gotdata
    
    def showtokens(self):
        print self.listaTokens
            
    def __concatenatechar(self, tokenLectura):
        self.tokenActual += tokenLectura
            
            
    def __tonum(self, cadena):
        i = 0
        try:
            i = int(cadena)
        except TypeError:
            i = -1
        return i

class Arp:
    def __init__(self):
        #self.g = g
        self.tokenActual = [None]
        self.listaTokens = []
        self.position = 0
        self.nLine = 0
        
    def analyze(self, lt):
        self.listaTokens = lt
        self.nLine = 0
        self.position = 0
        while not self.tokenActual[0] == "TK_SALIDA":
            try:
                pass
                self.readnewtoken()
                self.e()     #E
            except:
                return False
        return True
      
    def iscreate(self):
        return self.tokenActual[0] == "TK_CREATE"
    def isif(self):
        return self.tokenActual[0] == "TK_IF"
    def isleftbrackets(self):
        return self.tokenActual[0] == "TK_PAR_ABR"
    def isrightbrackets(self):
        return self.tokenActual[0] == "TK_PAR_CER"
    def iscomma(self):
        return self.tokenActual[0] == "TK_COMMA"
    def isprop(self):
        if(self.tokenActual[0] == "TK_NULL"):
            self.tokenActual[0] = "TK_PROP"
        return self.tokenActual[0] == "TK_PROP"
    def e(self):
        if self.iscreate():
            self.match("TK_CREATE")
            self.match("TK_TABLE")
            if self.isif():
                self.match("TK_IF")
                self.match("TK_NOT")
            self.ntpr()    #NT'
            self.match("TK_PAR_CER")
            self.match("TK_FIN_SENT")
        #lambda
                    
    def ntpr(self):
        self.match("TK_ID") #table name
        self.match("TK_PAR_ABR")
        self.atpr()     #At'
        
    def atpr(self):
        if self.isprop(): # For primary key :D
            self.match("TK_PROP")       # primary
            self.match("TK_PROP")       # key
            self.match("TK_PAR_ABR")    # (
            self.match("TK_ID")         # attribute to be pk
            self.match("TK_PAR_CER")    # )
            if self.iscomma():
                self.match("TK_COMMA")
                self.atpr()
        else:    
            self.match("TK_ID") #attribute name
            self.match("TK_TYPE") #attribute type
            if self.isleftbrackets():
                self.match("TK_PAR_ABR")
                self.match("TK_CTE_NUM")    #int value type
                if self.isrightbrackets():
                    self.match("TK_PAR_CER")
            if self.isprop():
                self.proppr()       #Prop'
            if self.iscomma():
                self.match("TK_COMMA")
                self.atpr()
        
    def proppr(self):
        self.match("TK_PROP")
        if self.isprop():
            self.proppr()
        else:
            pass #lambda
        
    def value(self):
        pass
    
    def match(self, token):
        if token == self.tokenActual[0]:
            if self.position != (len(self.listaTokens) - 1) :
                self.readnewtoken()
                return
            else :
                self.tokenActual = ("TK_SALIDA", "$#$")
                return
        raise Exception("Error D:")

    def readnewtoken(self):
        self.tokenActual = self.listaTokens[self.position]
        self.position += 1
        print "TOKEN: ", self.tokenActual

if __name__ == "__main__": 
    
    la = LexicalAnalyzer(pkey=open("pk.txt").readline()[:-1].split(" "), type=open("type.txt").readline()[:-1].split(" "), prop=open("prop.txt").readline()[:-1].split(" "))
    l = la.lineanalyzer(
    "CREATE TABLE Customer"
    "(id int auto_increment,"
    "First_Name char(50),"
    "City int,"
    "primary key(id),"
    "Birth_Date datetime,"
    "FOREIGN KEY (P_Id) REFERENCES Persons(P_Id)"
    ");")
    
    print l
    arp = Arp()
    print arp.analyze(l)
    
    