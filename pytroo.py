#!/usr/bin/python
# -*- encoding: utf-8 -*-
if 64 - 64: i11iIiiIii
__author__ = "maldicion069"
__date__ = "$Aug 4, 2014 3:42:08 AM$"
if 65 - 65: O0 / iIii1I11I1II1 % OoooooooOO - i1IIi
if 73 - 73: II111iiii
if 22 - 22: I1IiiI * Oo0Ooo / OoO0O00 . OoOoOO00 . o0oOOo0O0Ooo / I1ii11iIi11i
import re
if 48 - 48: oO0o / OOooOOo / I11i / Ii1I
class IiiIII111iI :
 fin = "$#$"
 prx_l = re . compile ( '[^\W\d_]+' )
 prx_n = re . compile ( '^-?[0-9]+$' )
 prx_del = re . compile ( " |\t" )
 prx_del1 = re . compile ( "( |\t)|\\\"|\\'|\\(|\\*|\\/|\\$|\\;|\\,|\\)" )
 prx_del2 = re . compile ( "( |\t)|\\(|([^\W\d_]+)|(-?[0-9]+$)" )
 if 34 - 34: iii1I1I / O00oOoOoO0o0O . O0oo0OO0 + Oo0ooO0oo0oO . OoO0O00 - I1ii11iIi11i
 def __init__ ( self , ** kwargs ) :
  self . actualToken = ""
  self . readToken = ""
  self . pointer = - 1
  self . tokenList = [ ]
  self . reservedWords = set ( )
  self . reservedWordsType = set ( )
  self . reservedWordsProp = set ( )
  self . state = 0
  self . __generatestates ( )
  self . states = { }
  self . codeLine = ""
  self . __addpr ( ** kwargs )
  if 53 - 53: I11i / Oo0Ooo / II111iiii % Ii1I / OoOoOO00 . Oo0ooO0oo0oO
 def __state0 ( self ) :
  self . __inilexema ( )
  self . digit = 0
  self . value = 0
  self . readToken = self . readchar ( )
  if self . readToken == 't' :
   pass
  if IiiIII111iI . prx_del . match ( self . readToken ) :
   self . state = 0
  elif IiiIII111iI . prx_l . match ( self . readToken ) :
   self . state = 1
  elif self . readToken == ";" :
   self . state = 9
  elif self . readToken == "(" :
   self . state = 14
  elif self . readToken == ")" :
   self . state = 15
  elif IiiIII111iI . prx_n . match ( self . readToken ) :
   self . state = 16
  elif self . readToken == "/" :
   self . state = 21
  elif self . readToken == "," :
   self . state = 25
   if 100 - 100: i1IIi
 def __state1 ( self ) :
  self . __concatenatechar ( self . readToken )
  self . readToken = self . readchar ( )
  if self . readToken == 't' :
   pass
  if IiiIII111iI . prx_n . match ( self . readToken ) :
   self . state = 3
  elif IiiIII111iI . prx_l . match ( self . readToken ) :
   self . state = 1
  elif IiiIII111iI . prx_del1 . match ( self . readToken ) :
   self . state = 2
   if 27 - 27: O00oOoOoO0o0O * OoooooooOO + I11i * Oo0ooO0oo0oO - i11iIiiIii - iii1I1I
 def __state2 ( self ) :
  self . __backwardpointer ( )
  self . __diferprid ( self . __dalexema ( ) )
  self . state = 0
  if 30 - 30: iIii1I11I1II1 * iIii1I11I1II1 . II111iiii - oO0o
 def __state3 ( self ) :
  self . __concatenatechar ( self . readToken )
  self . readToken = self . readchar ( )
  if IiiIII111iI . prx_n . match ( self . readToken ) or IiiIII111iI . prx_l . match ( self . readToken ) :
   self . state = 3
  elif IiiIII111iI . prx_del . match ( self . readToken ) :
   self . state = 4
   if 72 - 72: II111iiii - OoOoOO00
 def __state4 ( self ) :
  self . __giventoken ( "TK_ID" , self . __dalexema ( ) )
  self . state = 0
  if 91 - 91: OoO0O00 . i11iIiiIii / oO0o % I11i / OoO0O00 - i11iIiiIii
 def __state9 ( self ) :
  self . __giventoken ( "TK_FIN_SENT" , ";" )
  self . state = 0
  if 8 - 8: o0oOOo0O0Ooo * I1ii11iIi11i * iIii1I11I1II1 . O00oOoOoO0o0O / O00oOoOoO0o0O % O00oOoOoO0o0O
 def __state14 ( self ) :
  self . __giventoken ( "TK_PAR_ABR" , "(" )
  self . state = 0
  if 22 - 22: Ii1I . O00oOoOoO0o0O
 def __state15 ( self ) :
  self . __giventoken ( "TK_PAR_CER" , ")" )
  self . state = 0
  if 41 - 41: O0oo0OO0 . Oo0ooO0oo0oO * O00oOoOoO0o0O % i11iIiiIii
 def __state16 ( self ) :
  self . digit = self . __tonum ( self . readToken )
  self . value = self . value * 10 + self . digit
  self . readToken = self . readchar ( )
  if IiiIII111iI . prx_n . match ( self . readToken ) :
   self . state = 16
  elif IiiIII111iI . prx_del1 . match ( self . readToken ) :
   self . state = 17
   if 74 - 74: iii1I1I * O00oOoOoO0o0O
 def __state17 ( self ) :
  self . __backwardpointer ( )
  self . __giventokenint ( "TK_CTE_NUM" , self . value )
  self . state = 0
  if 82 - 82: iIii1I11I1II1 % O00oOoOoO0o0O
 def __state25 ( self ) :
  self . __giventoken ( "TK_COMMA" , "," )
  self . state = 0
  if 86 - 86: OoOoOO00 % I1IiiI
 def __generatestates ( self ) :
  self . states = {
 0 : self . __state0 ,
 1 : self . __state1 ,
 2 : self . __state2 ,
 3 : self . __state3 ,
 4 : self . __state4 ,
 9 : self . __state9 ,
 14 : self . __state14 ,
 15 : self . __state15 ,
 16 : self . __state16 ,
 17 : self . __state17 ,
 25 : self . __state25
 }
  if 80 - 80: OoooooooOO . I1IiiI
 def lineanalyzer ( self , line ) :
  self . __inilexema ( )
  self . codeLine = line
  self . state = self . value = self . digit = 0
  self . pointer = - 1
  self . __generatestates ( )
  try :
   while ( self . fin != self . readToken ) :
    self . states [ self . state ] ( )
  except :
   pass
  finally :
   self . tokenList . append ( ( "TK_SALIDA" , "$EOF$" ) )
  return self . tokenList
  if 87 - 87: oO0o / Oo0ooO0oo0oO + O0oo0OO0 - Oo0ooO0oo0oO . Oo0ooO0oo0oO / II111iiii
 def __inilexema ( self ) :
  self . actualToken = ""
  self . readToken = ""
  if 11 - 11: I1IiiI % o0oOOo0O0Ooo - Oo0Ooo
 def __backwardpointer ( self ) :
  self . pointer -= 1
  if 58 - 58: i11iIiiIii % O0oo0OO0
 def __giventoken ( self , lexema , contenido ) :
  O0OoOoo00o = ( lexema , contenido )
  self . tokenList . append ( O0OoOoo00o )
  return O0OoOoo00o
  if 31 - 31: II111iiii + OoO0O00 . O0oo0OO0
 def __giventokenint ( self , lexema , valor ) :
  O0OoOoo00o = ( lexema , valor )
  self . tokenList . append ( O0OoOoo00o )
  return O0OoOoo00o
  if 68 - 68: I1IiiI - i11iIiiIii - OoO0O00 / OOooOOo - OoO0O00 + i1IIi
 def __diferprid ( self , lexema ) :
  if lexema in self . reservedWords :
   O0OoOoo00o = ( "TK_" + self . __dalexema ( ) . upper ( ) , lexema )
  elif lexema in self . reservedWordsType :
   O0OoOoo00o = ( "TK_TYPE" , lexema )
  elif lexema in self . reservedWordsProp :
   O0OoOoo00o = ( "TK_PROP" , lexema )
  else :
   O0OoOoo00o = ( "TK_ID" , lexema )
  self . tokenList . append ( O0OoOoo00o )
  if 48 - 48: OoooooooOO % o0oOOo0O0Ooo . I1IiiI - Ii1I % i1IIi % OoooooooOO
 def __dalexema ( self ) :
  return self . actualToken
  if 3 - 3: iii1I1I + O0
 def reservedWords ( self , * args ) :
  self . addpr ( args )
  if 42 - 42: OOooOOo / i1IIi + i11iIiiIii - Ii1I
 def __addpr ( self , ** kwargs ) :
  for oo0Ooo0 in kwargs [ 'pkey' ] :
   self . reservedWords . add ( oo0Ooo0 . upper ( ) )
   self . reservedWords . add ( oo0Ooo0 . lower ( ) )
  for oo0Ooo0 in kwargs [ 'type' ] :
   self . reservedWordsType . add ( oo0Ooo0 . upper ( ) )
   self . reservedWordsType . add ( oo0Ooo0 . lower ( ) )
  for oo0Ooo0 in kwargs [ 'prop' ] :
   self . reservedWordsProp . add ( oo0Ooo0 . upper ( ) )
   self . reservedWordsProp . add ( oo0Ooo0 . lower ( ) )
   if 46 - 46: Oo0ooO0oo0oO % Oo0ooO0oo0oO - oO0o * o0oOOo0O0Ooo % iii1I1I
 def readchar ( self ) :
  self . pointer += 1
  if len ( self . codeLine ) > self . pointer :
   OOooO0OOoo = self . codeLine [ self . pointer ]
  else :
   OOooO0OOoo = self . fin
  return OOooO0OOoo
  if 29 - 29: o0oOOo0O0Ooo / iIii1I11I1II1
 def __concatenatechar ( self , tokenLectura ) :
  self . actualToken += tokenLectura
  if 24 - 24: O0 % o0oOOo0O0Ooo + i1IIi + O0oo0OO0 + I1ii11iIi11i
 def __tonum ( self , cadena ) :
  OOoO000O0OO = 0
  try :
   OOoO000O0OO = int ( cadena )
  except TypeError :
   OOoO000O0OO = - 1
  return OOoO000O0OO
  if 23 - 23: i11iIiiIii + I1IiiI
class oOo :
 def __init__ ( self ) :
  self . actualToken = [ None ]
  self . tokenList = [ ]
  self . position = 0
  self . nLine = 0
  self . actualTable = None
  self . ts = oOoOoO ( )
  self . actualAttribute = None
  if 6 - 6: I1IiiI / Oo0Ooo % Ii1I
 def analyze ( self , lt ) :
  self . tokenList = lt
  self . nLine = 0
  self . position = 0
  self . readnewtoken ( )
  while True :
   try :
    pass
    self . e ( )
   except Exception as oo :
    print "             " , oo . args
    return False
   if self . actualToken [ 0 ] == "TK_SALIDA" :
    return True
    if 54 - 54: OOooOOo + OOooOOo % O0oo0OO0 % i11iIiiIii / iIii1I11I1II1 . OOooOOo
 def iscreate ( self ) :
  return self . actualToken [ 0 ] == "TK_CREATE"
 def isif ( self ) :
  return self . actualToken [ 0 ] == "TK_IF"
 def isid ( self ) :
  return self . actualToken [ 0 ] == "TK_ID"
 def isleftbrackets ( self ) :
  return self . actualToken [ 0 ] == "TK_PAR_ABR"
 def isrightbrackets ( self ) :
  return self . actualToken [ 0 ] == "TK_PAR_CER"
 def iscomma ( self ) :
  return self . actualToken [ 0 ] == "TK_COMMA"
 def isprop ( self ) :
  if ( self . actualToken [ 0 ] == "TK_NOT" ) :
   self . actualToken = ( "TK_PROP" , self . actualToken [ 1 ] )
  return self . actualToken [ 0 ] == "TK_PROP"
 def isfinalsentence ( self ) :
  return self . actualToken [ 0 ] == "TK_FIN_SENT"
 def isalter ( self ) :
  return self . actualToken [ 0 ] == "TK_ALTER" ;
 def e ( self ) :
  if self . iscreate ( ) :
   self . match ( "TK_CREATE" )
   self . match ( "TK_TABLE" )
   if self . isif ( ) :
    self . match ( "TK_IF" )
    self . match ( "TK_NOT" )
    self . match ( "TK_EXISTS" )
   self . ntpr ( )
   self . match ( "TK_PAR_CER" )
   if self . isfinalsentence ( ) :
    self . match ( "TK_FIN_SENT" )
   return
  elif self . isalter ( ) :
   self . match ( "TK_ALTER" )
   self . match ( "TK_TABLE" )
   self . match ( "TK_ID" )
   self . match ( "TK_PROP" )
   self . match ( "TK_PROP" )
   self . match ( "TK_PAR_ABR" )
   self . match ( "TK_ID" )
   self . match ( "TK_PAR_CER" )
   self . match ( "TK_PROP" )
   self . match ( "TK_ID" )
   self . match ( "TK_PAR_ABR" )
   self . match ( "TK_ID" )
   self . match ( "TK_PAR_CER" )
   return
  raise
 def ntpr ( self ) :
  self . actualTable = self . actualToken [ 1 ]
  self . match ( "TK_ID" )
  self . match ( "TK_PAR_ABR" )
  if self . isid ( ) :
   self . atpr ( )
   if 57 - 57: Ii1I % OoooooooOO
 def atpr ( self ) :
  if self . isprop ( ) :
   self . match ( "TK_PROP" )
   self . match ( "TK_PROP" )
   self . match ( "TK_PAR_ABR" )
   self . actualAttribute = self . actualToken [ 1 ]
   self . match ( "TK_ID" )
   self . match ( "TK_PAR_CER" )
   if self . isprop ( ) :
    self . match ( "TK_PROP" )
    self . match ( "TK_ID" )
    self . match ( "TK_PAR_ABR" )
    self . ts . add ( self . actualTable , self . actualAttribute , "FK#" + self . actualToken [ 1 ] )
    self . match ( "TK_ID" )
    self . match ( "TK_PAR_CER" )
   else :
    self . ts . add ( self . actualTable , self . actualAttribute , "PK" )
    if 61 - 61: iii1I1I . iIii1I11I1II1 * I1IiiI . Oo0ooO0oo0oO % Oo0Ooo
   if self . iscomma ( ) :
    self . match ( "TK_COMMA" )
    self . atpr ( )
  else :
   self . actualAttribute = self . actualToken [ 1 ]
   self . match ( "TK_ID" )
   self . ts . add ( self . actualTable , self . actualAttribute , self . actualToken [ 1 ] )
   self . match ( "TK_TYPE" )
   if self . isleftbrackets ( ) :
    self . ts . add ( self . actualTable , self . actualAttribute , self . actualToken [ 1 ] )
    self . match ( "TK_PAR_ABR" )
    self . ts . add ( self . actualTable , self . actualAttribute , self . actualToken [ 1 ] )
    self . match ( "TK_CTE_NUM" )
    if self . isrightbrackets ( ) :
     self . ts . add ( self . actualTable , self . actualAttribute , self . actualToken [ 1 ] )
     self . match ( "TK_PAR_CER" )
   if self . isprop ( ) :
    self . proppr ( )
   if self . iscomma ( ) :
    self . match ( "TK_COMMA" )
    self . atpr ( )
    if 72 - 72: OOooOOo
 def proppr ( self ) :
  self . ts . add ( self . actualTable , self . actualAttribute , self . actualToken [ 1 ] )
  self . match ( "TK_PROP" )
  if self . isprop ( ) :
   self . proppr ( )
  else :
   pass
   if 63 - 63: Ii1I
 def value ( self ) :
  pass
  if 86 - 86: Oo0ooO0oo0oO . I1IiiI % Oo0Ooo + o0oOOo0O0Ooo
 def match ( self , token ) :
  if token == self . actualToken [ 0 ] :
   if self . position != ( len ( self . tokenList ) - 1 ) :
    self . readnewtoken ( )
    return
   else :
    self . actualToken = ( "TK_SALIDA" , "$#$" )
    return
  raise Exception ( "Error D:" )
  if 35 - 35: iIii1I11I1II1 % oO0o * I11i % I11i + II111iiii * iii1I1I
 def readnewtoken ( self ) :
  self . actualToken = self . tokenList [ self . position ]
  self . position += 1
  print "TOKEN: " , self . actualToken
  if 54 - 54: I11i + O00oOoOoO0o0O / iii1I1I
class oOoOoO :
 def __init__ ( self ) :
  self . map = { }
  if 9 - 9: OoOoOO00 / Oo0Ooo - O00oOoOoO0o0O . i1IIi / I1IiiI % O00oOoOoO0o0O
 def add ( self , table , label , value ) :
  if not self . map . has_key ( table ) :
   self . map [ table ] = o0 ( table )
  self . map [ table ] . add ( label , value )
  if 9 - 9: Ii1I + oO0o % Ii1I + i1IIi . OOooOOo
 def keyss ( self ) :
  III1i1i = ""
  for iiI1 in self . map . items ( ) :
   III1i1i += iiI1 [ 1 ] . printwithformat ( ) + "\n"
   if 19 - 19: I11i + Oo0ooO0oo0oO
  return III1i1i
  if 53 - 53: OoooooooOO . i1IIi
  if 18 - 18: o0oOOo0O0Ooo
class o0 ( object ) :
 def __init__ ( self , name ) :
  self . map = { }
  self . name = name
  if 28 - 28: OOooOOo - O00oOoOoO0o0O . O00oOoOoO0o0O + OoOoOO00 - OoooooooOO + O0
 def add ( self , label , value ) :
  if self . map . has_key ( label ) :
   O0OoOoo00o = self . map [ label ]
  else :
   O0OoOoo00o = [ ]
  O0OoOoo00o . append ( value )
  self . map [ label ] = O0OoOoo00o
  if 95 - 95: OoO0O00 % oO0o . O0
  if 15 - 15: Oo0ooO0oo0oO / Ii1I . Ii1I - i1IIi
  if 53 - 53: O00oOoOoO0o0O + I1IiiI * oO0o
  if 61 - 61: i1IIi * OOooOOo / OoooooooOO . i11iIiiIii . OoOoOO00
 def tuple_without ( self , original_tuple , element_to_remove ) :
  o00O = [ ]
  for OOO0OOO00oo in list ( original_tuple ) :
   if not OOO0OOO00oo == element_to_remove :
    o00O . append ( OOO0OOO00oo )
  return tuple ( o00O )
  if 31 - 31: II111iiii - OOooOOo . O0oo0OO0 % OoOoOO00 - O0
 def tuple_without_index ( self , original_tuple , index ) :
  o00O = [ ]
  for OOO0OOO00oo in range ( 0 , len ( original_tuple ) ) :
   if not OOO0OOO00oo == index :
    o00O . append ( original_tuple [ OOO0OOO00oo ] )
  return tuple ( o00O )
  if 4 - 4: II111iiii / Oo0ooO0oo0oO . iii1I1I
 def index_tuple_value_compare ( self , tuple , value , index ) :
  if len ( tuple ) < index :
   return False
  else :
   return tuple [ index ] == value
   if 58 - 58: OOooOOo * i11iIiiIii / OoOoOO00 % O0oo0OO0 - I1ii11iIi11i / oO0o
 def first_tuple_value_compare ( self , tuple , value ) :
  if len ( tuple ) == 0 :
   return False
  else :
   return tuple [ 0 ] == value
   if 50 - 50: I1IiiI
 def first_tuple_value_in_compare ( self , tuple , value ) :
  if len ( tuple ) == 0 :
   return False
  else :
   return value in tuple [ 0 ]
   if 34 - 34: I1IiiI * II111iiii % iii1I1I * OoOoOO00 - I1IiiI
   if 33 - 33: o0oOOo0O0Ooo + OOooOOo * OoO0O00 - Oo0Ooo / oO0o % Ii1I
 def printwithformat ( self ) :
  III1i1i = "entity --class ~.model." + self . name + " --testAutomatically "
  III1i1i += "--activeRecord false"
  II1i1IiiIIi11 = ""
  iI1Ii11iII1 = False
  for Oo0O0O0ooO0O , IIIIii in self . map . iteritems ( ) :
   if "PK" in IIIIii :
    continue
   II1i1IiiIIi11 += "field "
   O0o0 = ""
   if "varchar" in IIIIii :
    II1i1IiiIIi11 += "string "
    O0o0 = "varchar"
   if "char" in IIIIii :
    II1i1IiiIIi11 += "string "
    O0o0 = "char"
   elif "int" in IIIIii :
    II1i1IiiIIi11 += "number"
    O0o0 = "int"
   elif "date" in IIIIii :
    II1i1IiiIIi11 += "date"
    if 71 - 71: OOooOOo + Oo0ooO0oo0oO % i11iIiiIii + I1ii11iIi11i - O00oOoOoO0o0O
   elif "double" in IIIIii :
    II1i1IiiIIi11 += "number"
    if 88 - 88: OoOoOO00 - OoO0O00 % OOooOOo
   IIIIii = self . tuple_without ( IIIIii , O0o0 )
   II1i1IiiIIi11 += "--fieldName " + str ( Oo0O0O0ooO0O ) + " "
   if self . first_tuple_value_compare ( IIIIii , "not" ) :
    II1i1IiiIIi11 += "--notNull "
    IIIIii = self . tuple_without ( IIIIii , "not" )
    IIIIii = self . tuple_without ( IIIIii , "null" )
   if self . first_tuple_value_compare ( IIIIii , "unique" ) :
    II1i1IiiIIi11 += "--unique "
    IIIIii = self . tuple_without ( IIIIii , "unique" )
   if self . first_tuple_value_compare ( IIIIii , "date" ) :
    II1i1IiiIIi11 += "--type java.util.Date"
    IIIIii = self . tuple_without ( IIIIii , "date" )
   if self . first_tuple_value_compare ( IIIIii , "(" ) :
    IIIIii = self . tuple_without ( IIIIii , "(" )
    II1i1IiiIIi11 += "--sizeMax " + str ( IIIIii [ 0 ] ) + " "
    IIIIii = self . tuple_without_index ( IIIIii , 0 )
    IIIIii = self . tuple_without ( IIIIii , ")" )
   if self . first_tuple_value_compare ( IIIIii , "double" ) :
    IIIIii = self . tuple_without ( IIIIii , "double" )
    II1i1IiiIIi11 += "--type java.math.BigDecimal"
   if self . first_tuple_value_in_compare ( IIIIii , "FK#" ) :
    if iI1Ii11iII1 :
     raise
    iI1I111Ii111i = IIIIii [ 0 ] [ 3 : ]
    II1i1IiiIIi11 += "--type ~.domain." + iI1I111Ii111i
    III1i1i += "--identifierType ~.domain." + iI1I111Ii111i
    I11IiI1I11i1i = True
    IIIIii = self . tuple_without_index ( IIIIii , 0 )
   if len ( IIIIii ) > 0 :
    pass
    if 38 - 38: o0oOOo0O0Ooo
   II1i1IiiIIi11 += "\n"
  III1i1i += "\n" + II1i1IiiIIi11
  return III1i1i
  if 57 - 57: O0 / oO0o * O0oo0OO0 / OoOoOO00 . II111iiii
def i11iIIIIIi1 ( route ) :
 iiII1i1 = open ( route , "r" )
 o00oOO0o = ""
 for OOO00O in iiII1i1 :
  o00oOO0o += OOO00O . replace ( "\n" , "" )
 return o00oOO0o
 if 84 - 84: oO0o * OoO0O00 / I11i - O0
if __name__ == "__main__" :
 try :
  o00oOO0o = i11iIIIIIi1 ( "code.sql" )
  IiI1 = IiiIII111iI ( pkey = open ( "pk.txt" ) . readline ( ) [ : - 1 ] . split ( " " ) , type = open ( "type.txt" ) . readline ( ) [ : - 1 ] . split ( " " ) , prop = open ( "prop.txt" ) . readline ( ) [ : - 1 ] . split ( " " ) )
  Oo0O00Oo0o0 = IiI1 . lineanalyzer ( o00oOO0o )
  if len ( Oo0O00Oo0o0 ) <= 1 :
   raise
  O00O0oOO00O00 = oOo ( )
  if not O00O0oOO00O00 . analyze ( Oo0O00Oo0o0 ) :
   raise
  i1 = O00O0oOO00O00 . ts . keyss ( )
  Oo00 = " "
  while Oo00 . count ( "." ) != 2 or " " in Oo00 :
   Oo00 = raw_input ( "Define ruta: " )
  iiII1i1 = open ( "roo.roo" , "w" )
  iiII1i1 . write ( "// Create a new project\n" )
  iiII1i1 . write ( "project --topLevelPackage " + Oo00 + "\n" )
  iiII1i1 . write ( "// Setup JPA persistence using EclipseLink and H2\n" )
  iiII1i1 . write ( "jpa setup --provider ECLIPSELINK --database H2_IN_MEMORY\n" )
  iiII1i1 . write ( "// Create domain entities\n" )
  iiII1i1 . write ( O00O0oOO00O00 . ts . keyss ( ) )
  iiII1i1 . write ( "web mvc setup\n" )
  iiII1i1 . write ( "web mvc all --package ~.web\n" )
  iiII1i1 . close ( )
 except :
  print "ERROR :("
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
