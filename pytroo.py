#!/usr/bin/python
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
    prx_del1 = re.compile("( |\t)|\\\"|\\'|\\(|\\*|\\/|\\$|\\;|\\,|\\)") 
    prx_del2 = re.compile("( |\t)|\\(|([^\W\d_]+)|(-?[0-9]+$)")
    
    def __init__(self, **kwargs):
        self.actualToken = ""
        self.readToken = ""
        self.pointer = -1
        self.tokenList = []
        self.reservedWords = set()
        self.reservedWordsType = set()
        self.reservedWordsProp = set()
        self.state = 0
        self.__generatestates()
        self.states = {}
        self.codeLine = ""
        self.__addpr(**kwargs)
        
    def __state0(self):
        self.__inilexema()
        self.digit = 0
        self.value = 0
        self.readToken = self.readchar()
        if self.readToken == 't':
            pass
        if LexicalAnalyzer.prx_del.match(self.readToken):
            self.state = 0
        elif LexicalAnalyzer.prx_l.match(self.readToken):
            self.state = 1
        elif self.readToken == ";":
            self.state = 9
        elif self.readToken == "(":
            self.state = 14
        elif self.readToken == ")":
            self.state = 15
        elif LexicalAnalyzer.prx_n.match(self.readToken):
            self.state = 16
        elif self.readToken == "/":
            self.state = 21
        elif self.readToken == ",":
            self.state = 25
           
    def __state1(self):
        self.__concatenatechar(self.readToken)
        self.readToken = self.readchar()
        if self.readToken == 't':
            pass
        if LexicalAnalyzer.prx_n.match(self.readToken):
            self.state = 3
        elif LexicalAnalyzer.prx_l.match(self.readToken):
            self.state = 1
        elif LexicalAnalyzer.prx_del1.match(self.readToken):
            self.state = 2
            
    def __state2(self):
        self.__backwardpointer()
        self.__diferprid(self.__dalexema())
        self.state = 0
        
    def __state3(self):
        self.__concatenatechar(self.readToken)
        self.readToken = self.readchar()
        if LexicalAnalyzer.prx_n.match(self.readToken) or LexicalAnalyzer.prx_l.match(self.readToken) :
            self.state = 3
        elif LexicalAnalyzer.prx_del.match(self.readToken):
            self.state = 4
        
    def __state4(self):
        self.__giventoken("TK_ID", self.__dalexema())
        self.state = 0
        
    def __state9(self):
        self.__giventoken("TK_FIN_SENT", ";")
        self.state = 0
        
    def __state14(self):
        self.__giventoken("TK_PAR_ABR", "(")
        self.state = 0
        
    def __state15(self):
        self.__giventoken("TK_PAR_CER", ")")
        self.state = 0
        
    def __state16(self):
        self.digit = self.__tonum(self.readToken)
        self.value = self.value * 10 + self.digit
        self.readToken = self.readchar()
        if LexicalAnalyzer.prx_n.match(self.readToken):
            self.state = 16
        elif LexicalAnalyzer.prx_del1.match(self.readToken):
            self.state = 17
    
    def __state17(self):
        self.__backwardpointer()
        self.__giventokenint("TK_CTE_NUM", self.value)
        self.state = 0
        
    def __state25(self):
        self.__giventoken("TK_COMMA", ",")
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
        self.codeLine = line
        self.state = self.value = self.digit = 0
        self.pointer = -1
        self.__generatestates()
        try:
            while(self.fin != self.readToken):
                self.states[self.state]()   
        except:
            pass
        finally:
            self.tokenList.append(("TK_SALIDA", "$EOF$"))
        return self.tokenList
        
    def __inilexema(self):
        self.actualToken = ""
        self.readToken = ""
        
    def __backwardpointer(self):
        self.pointer -= 1
        
    def __giventoken(self, lexema, contenido):
        t = (lexema, contenido)
        self.tokenList.append(t)
        return t
    
    def __giventokenint(self, lexema, valor):
        t = (lexema, valor)
        self.tokenList.append(t)
        return t
        
    def __diferprid(self, lexema):
        if lexema in self.reservedWords:
            t = ("TK_" + self.__dalexema().upper(), lexema)
        elif lexema in self.reservedWordsType:
            t = ("TK_TYPE", lexema)
        elif lexema in self.reservedWordsProp:
            t = ("TK_PROP", lexema)
        else:
            t = ("TK_ID", lexema)
        self.tokenList.append(t)
    
    def __dalexema(self):
        return self.actualToken
    
    def reservedWords(self, *args):
        self.addpr(args)
        
    def __addpr(self, **kwargs):
        for arg in kwargs['pkey']:
            self.reservedWords.add(arg.upper())
            self.reservedWords.add(arg.lower())
        for arg in kwargs['type']:
            self.reservedWordsType.add(arg.upper())
            self.reservedWordsType.add(arg.lower())
        for arg in kwargs['prop']:
            self.reservedWordsProp.add(arg.upper())
            self.reservedWordsProp.add(arg.lower())
            
    def readchar(self):
        self.pointer += 1
        if len(self.codeLine) > self.pointer:
            gotdata = self.codeLine[self.pointer]
        else:
            gotdata = self.fin
        return gotdata
            
    def __concatenatechar(self, tokenLectura):
        self.actualToken += tokenLectura
            
    def __tonum(self, cadena):
        i = 0
        try:
            i = int(cadena)
        except TypeError:
            i = -1
        return i

class Arp:
    def __init__(self):
        self.actualToken = [None]
        self.tokenList = []
        self.position = 0
        self.nLine = 0
        self.actualTable = None
        self.ts = Tables()
        self.actualAttribute = None
        
    def analyze(self, lt):
        self.tokenList = lt
        self.nLine = 0
        self.position = 0
        self.readnewtoken()
        while True:
            try:
                pass
                self.e()     #E
            except Exception as e:
                print "             ", e.args
                return False
            if self.actualToken[0] == "TK_SALIDA":
                return True
      
    def iscreate(self):
        return self.actualToken[0] == "TK_CREATE"
    def isif(self):
        return self.actualToken[0] == "TK_IF"
    def isid(self):
        return self.actualToken[0] == "TK_ID"
    def isleftbrackets(self):
        return self.actualToken[0] == "TK_PAR_ABR"
    def isrightbrackets(self):
        return self.actualToken[0] == "TK_PAR_CER"
    def iscomma(self):
        return self.actualToken[0] == "TK_COMMA"
    def isprop(self):
        if(self.actualToken[0] == "TK_NOT"):
            self.actualToken = ("TK_PROP", self.actualToken[1])
        return self.actualToken[0] == "TK_PROP"
    def isfinalsentence(self):
        return self.actualToken[0] == "TK_FIN_SENT"
    def isalter(self):
        return self.actualToken[0] == "TK_ALTER";
    def e(self):
        if self.iscreate():
            self.match("TK_CREATE")
            self.match("TK_TABLE")
            if self.isif():
                self.match("TK_IF")
                self.match("TK_NOT")
                self.match("TK_EXISTS")
            self.ntpr()    #NT'
            self.match("TK_PAR_CER")
            if self.isfinalsentence():
                self.match("TK_FIN_SENT")
            return
        elif self.isalter():
            self.match("TK_ALTER")
            self.match("TK_TABLE")
            self.match("TK_ID")
            self.match("TK_PROP")
            self.match("TK_PROP")
            self.match("TK_PAR_ABR")
            self.match("TK_ID")
            self.match("TK_PAR_CER")
            self.match("TK_PROP")
            self.match("TK_ID")
            self.match("TK_PAR_ABR")
            self.match("TK_ID")
            self.match("TK_PAR_CER")
            return
        raise            
    def ntpr(self):
        self.actualTable = self.actualToken[1]
        self.match("TK_ID") #table name
        self.match("TK_PAR_ABR")
        if self.isid():
            self.atpr()     #At'
        
    def atpr(self):
        if self.isprop(): # For primary key :D
            self.match("TK_PROP")       # primary
            self.match("TK_PROP")       # key
            self.match("TK_PAR_ABR")    # (
            self.actualAttribute = self.actualToken[1]
            self.match("TK_ID")         # attribute to be pk
            self.match("TK_PAR_CER")    # )
            if self.isprop():           # references
                self.match("TK_PROP")
                self.match("TK_ID")         #table reference
                self.match("TK_PAR_ABR")    # (
                self.ts.add(self.actualTable, self.actualAttribute, "FK#" + self.actualToken[1])
                self.match("TK_ID")         # attribute to be fk
                self.match("TK_PAR_CER")    # )
            else:
                self.ts.add(self.actualTable, self.actualAttribute, "PK")
            
            if self.iscomma():
                self.match("TK_COMMA")
                self.atpr()
        else:    
            self.actualAttribute = self.actualToken[1]
            self.match("TK_ID") #attribute name
            self.ts.add(self.actualTable, self.actualAttribute, self.actualToken[1])
            self.match("TK_TYPE") #attribute type
            if self.isleftbrackets():
                self.ts.add(self.actualTable, self.actualAttribute, self.actualToken[1])
                self.match("TK_PAR_ABR")
                self.ts.add(self.actualTable, self.actualAttribute, self.actualToken[1])
                self.match("TK_CTE_NUM")    #int value type
                if self.isrightbrackets():
                    self.ts.add(self.actualTable, self.actualAttribute, self.actualToken[1])
                    self.match("TK_PAR_CER")
            if self.isprop():
                self.proppr()       #Prop'
            if self.iscomma():
                self.match("TK_COMMA")
                self.atpr()
        
    def proppr(self):
        self.ts.add(self.actualTable, self.actualAttribute, self.actualToken[1])
        self.match("TK_PROP")
        if self.isprop():
            self.proppr()
        else:
            pass #lambda
        
    def value(self):
        pass
    
    def match(self, token):
        if token == self.actualToken[0]:
            if self.position != (len(self.tokenList) - 1) :
                self.readnewtoken()
                return
            else :
                self.actualToken = ("TK_SALIDA", "$#$")
                return
        raise Exception("Error D:")

    def readnewtoken(self):
        self.actualToken = self.tokenList[self.position]
        self.position += 1
	print "TOKEN: ", self.actualToken

class Tables:
    def __init__(self):
        self.map = {}
    
    def add(self, table, label, value):
        if not self.map.has_key(table):
            self.map[table] = Table(table)
        self.map[table].add(label, value)
    
    def keyss(self):
        ss = ""
        for n in self.map.items():
            ss += n[1].printwithformat() + "\n"
            #print n[0], "  " , n[1].map
        return ss
        

class Table(object):
    def __init__(self, name):
        self.map = {}
	self.name = name
        
    def add(self, label, value):
        if self.map.has_key(label):
            t = self.map[label]
        else:
            t = []
        t.append(value)
        self.map[label] = t
        



    def tuple_without(self, original_tuple, element_to_remove):
        new_tuple = []
        for s in list(original_tuple):
            if not s == element_to_remove:
                new_tuple.append(s)
        return tuple(new_tuple)

    def tuple_without_index(self, original_tuple, index):
        new_tuple = []
        for s in range(0, len(original_tuple)):
            if not s == index:
                new_tuple.append(original_tuple[s])
        return tuple(new_tuple)
 
    def index_tuple_value_compare(self, tuple, value, index):
	if len(tuple) < index:
	    return False
        else:
            return tuple[index] == value

    def first_tuple_value_compare(self, tuple, value):
	if len(tuple) == 0:
	    return False
        else:
            return tuple[0] == value

    def first_tuple_value_in_compare(self, tuple, value):
	if len(tuple) == 0:
	    return False
        else:
            return value in tuple[0]


    def printwithformat(self):
	ss = "entity --class ~.model." + self.name + " --testAutomatically "
	ss += "--activeRecord false"
	tablestr = ""
        haveFk = False
	for k,v in self.map.iteritems():
	    if "PK" in v:
		continue
            tablestr += "field "
	    del_ = ""
            if "varchar" in v:
                tablestr += "string "
		del_ = "varchar"
            if "char" in v:
                tablestr += "string "
		del_ = "char"
            elif "int" in v:
                tablestr += "number"
		del_ = "int"
            elif "date" in v:
                tablestr += "date"
                #del_ = "date"
	    elif "double" in v:
		tablestr += "number"
		#del_ = "double"
            v = self.tuple_without(v, del_)
            tablestr += "--fieldName " + str(k) + " "
            if self.first_tuple_value_compare(v, "not"):
	        tablestr += "--notNull "
	        v = self.tuple_without(v, "not")
		v = self.tuple_without(v, "null")
            if self.first_tuple_value_compare(v, "unique"):
		tablestr += "--unique "
		v = self.tuple_without(v, "unique")
	    if self.first_tuple_value_compare(v, "date"):
                tablestr += "--type java.util.Date"
		v = self.tuple_without(v, "date")
	    if self.first_tuple_value_compare(v, "("):
		v = self.tuple_without(v, "(")
		tablestr += "--sizeMax "+  str(v[0]) + " "
		v = self.tuple_without_index(v, 0)
		v = self.tuple_without(v, ")")
	    if self.first_tuple_value_compare(v, "double"):
		v = self.tuple_without(v, "double")
		tablestr += "--type java.math.BigDecimal"
	    if self.first_tuple_value_in_compare(v, "FK#"):
		if haveFk:
                    raise
		sst = v[0][3:]
		tablestr += "--type ~.domain." + sst
		ss += "--identifierType ~.domain." + sst
		haveFK = True
		v = self.tuple_without_index(v, 0)
            if len(v) > 0:
		pass
	        #tablestr += v
            tablestr += "\n"
        ss += "\n" + tablestr
	return ss

def readfile(route):
    f = open(route, "r")
    sql = ""
    for line in f:
        sql += line.replace("\n", "")
    return sql

if __name__ == "__main__": 
    try:
        sql = readfile("code.sql")
        la = LexicalAnalyzer(pkey=open("pk.txt").readline()[:-1].split(" "), type=open("type.txt").readline()[:-1].split(" "), prop=open("prop.txt").readline()[:-1].split(" "))
        l = la.lineanalyzer(sql)
        if len(l) <= 1: #only end of file or empty
	    raise
        arp = Arp()
        if not arp.analyze(l):
            raise
        code = arp.ts.keyss()
        route = " "
        while route.count(".") != 2 or " " in route:
        	route = raw_input("Define ruta: ")
        f = open("roo.roo", "w")
        f.write("// Create a new project\n")
        f.write("project --topLevelPackage " + route + "\n")
        f.write("// Setup JPA persistence using EclipseLink and H2\n")
        f.write("jpa setup --provider ECLIPSELINK --database H2_IN_MEMORY\n")
        f.write("// Create domain entities\n")
        f.write(arp.ts.keyss())
        f.write("web mvc setup\n")
        f.write("web mvc all --package ~.web\n")
        f.close()
    except:
        print "ERROR :("
