# -*- encoding: utf-8 -*-

__author__="maldicion069"
__date__ ="$Aug 4, 2014 3:42:08 AM$"

#from analyzer.lexical import LexicalAnalyzer

import re

class LexicalAnalyzer:
    
    fin = "$#$" #" " => \b
    #arregladas  
    prx_l = re.compile('[^\W\d_]+')
    prx_n = re.compile('^-?[0-9]+$')
    prx_del = re.compile(" |\t")
    prx_del1 = re.compile("( |\t)|\\(|\\*|\\/|\\$|\\;|\\)") 
    prx_del2 = re.compile("( |\t)|\\(|([^\W\d_]+)|(-?[0-9]+$)")
    #arregladas
    
    prx_e = re.compile("\\+|\\-")   #Añadidos nuevos delimitadores. Poner en memoria (>)
    
    
    def __init__(self, *argv):
        self.tokenActual = ""
        self.tokenLectura = ""
        self.puntero = -1
        self.listaTokens = []
        self.palabrasReservadas = set()
        self.state = 0#self.valor = self.digito = 0
        self.__generatestates()
        self.states = {}
        self.lineaCodigo = ""
        self.__addpr(*argv)
        
    def __state0(self):
        self.__inilexema()
        self.digito = 0
        self.valor = 0
        self.tokenLectura = self.readchar()
        print "Tengo: ", self.tokenLectura
        if LexicalAnalyzer.prx_del.match(self.tokenLectura):
            self.state = 0
        elif LexicalAnalyzer.prx_l.match(self.tokenLectura):
            self.state = 1
        elif self.tokenLectura == "$":
            self.state = 9
        elif self.tokenLectura == "(":
            self.state = 14
        elif self.tokenLectura == ")":
            self.state = 15
        elif LexicalAnalyzer.prx_n.match(self.tokenLectura):
            self.state = 16
        elif self.tokenLectura == "/":
            self.state = 21
           
    def __state1(self):
        self.__concatenatechar(self.tokenLectura)
        self.tokenLectura = self.readchar()
        print "Tengo: ", self.tokenActual
        if LexicalAnalyzer.prx_n.match(self.tokenLectura):
            self.state = 3
        elif LexicalAnalyzer.prx_l.match(self.tokenLectura):
            self.state = 1
        elif LexicalAnalyzer.prx_del1.match(self.tokenLectura):
            self.state = 2
            
    def __state2(self):
        self.__retrocesopuntero()
        self.__diferprid(self.__dalexema())
        print self.listaTokens
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
        self.__datoken("TK_FIN_SENT", "$")
        self.state = 0
        
    def __state14(self):
        self.__datoken("TK_PAR_ABR", "(")
        self.state = 0
        
    def __state15(self):
        self.__datoken("TK_PAR_CER", ")")
        self.state = 0
        
    def __state16(self):
        self.digito = self.__tonum(self.tokenLectura)
        print "Dígito: ", self.digito
        self.valor = self.valor * 10 + self.digito
        print "Valor: ", self.valor
        self.tokenLectura = self.readchar()
        if LexicalAnalyzer.prx_n.match(self.tokenLectura):
            self.state = 16
        elif LexicalAnalyzer.prx_del1.match(self.tokenLectura):
            self.state = 17
    
    def __state17(self):
        self.__retrocesopuntero()
        self.__datokenint("TK_CTE_NUM", self.valor)
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
            17 : self.__state17
        }
        
    def lineanalyzer(self, line):
        self.__inilexema()
        self.lineaCodigo = line
        self.state = 0#self.valor = self.digito = 0
        self.puntero = -1
        self.__generatestates()
        print self.states
        #self.states[self.state]()
        try:
            while(self.fin != self.tokenLectura):
                print self.state
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
        else:
            t = ("TK_ID", lexema)
        self.listaTokens.append(t)
        #self.listaTokens.append("TK_" + self.__dalexema().upper(), lexema) if lexema in self.palabrasReservadas else ("TK_ID", lexema)
        
    
    def __dalexema(self):
        return self.tokenActual
    
    def palabrasreservadas(self, *args):
        self.addpr(args)
        
    def showreservadas(self):
        for n in enumerate(self.palabrasReservadas):
            print n, "   ",
        print
        
    def __addpr(self, *args):
        for arg in args[0]:
            print arg
            self.palabrasReservadas.add(arg)
            
    def readchar(self):
        
        
        self.puntero += 1
        print "SIZE: ", len(self.lineaCodigo), "  ", self.puntero
        if len(self.lineaCodigo) > self.puntero:
            gotdata = self.lineaCodigo[self.puntero]
        else:
            gotdata = self.fin
        return gotdata
        '''
        #return self.lineaCodigo[self.puntero]
        print "SIZE: ", len(self.lineaCodigo)
        try:
            return str(self.lineaCodigo[self.puntero])#str(self.lineaCodigo.index(self.puntero)) + ""
        except IndexError:
            return self.fin
        '''
    def showtokens(self):
        print self.listaTokens
            
    def __concatenatechar(self, tokenLectura):
        self.tokenActual += tokenLectura
        print self.tokenActual
            
            
    def __tonum(self, cadena):
        i = 0
        print "Cadena: ", cadena
        try:
            i = int(cadena)
        except TypeError:
            i = -1
        return i


if __name__ == "__main__": 
    r = re.compile(" |\t")#"(\b|\t)|\\(|\\*|\\/|\\$|\\;|\\)")
    if r.match("A"):
        print "true"
    else:
        print "no"
    l = "CREATE TABLE IF NOT EXIST not null auto_increment int long varchar datetime min max primary key".split(" ")
    print l
    la = LexicalAnalyzer(l)
    l = la.lineanalyzer("CREATE TABLE IF NOT EXIST user ("
        "id int not null auto_increment"
    ")$")#"CREATE TABLE IF NOT EXIST$")
    i = 0
    for i in range(0, len(l)):
        print l[i]
    
    