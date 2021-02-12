#modularização da bibliotecas ultilizadas
import recFace
import recObj
import voz 
import recVoz
import Expressoes

#reconhecimeto de voz
def respostaSintomas():
  return recVoz.frase()

#inteção com o visitante para captar o seu nome
def perguntaNome():
  Expresoes.sorriso()
  voz.fala("ola, seja bem vindo, poderia dizer seu nome")
  return recVoz.frase()

#funcao para indentificar seu visitante esta usando mascara
def usandoMascara():
  if "mascara" == recObj.reconhecimento():
    return True
  else:
    Expresoes.img('mascara.jpg')
    voz.fala("por favor ultilize mascara no recinto")  
    return False
  
#interaçao com visitante para perguntando com se apresenta algun sintoma e recebendo resposta dele
def PerguntaSitomas():
  frase ="NULL"
  
  Expresoes.sorriso()
  
  voz.fala("nos ultimos 7 dias voce sentiu alguns desse sintomas")
  Expresoes.img('termetro.jpg')
  voz.fala("febre")
  Expresoes.img('pessoaTossindo.jpg')
  voz.fala("tosse")
  Expresoes.img('pessoaCansada.jpg')
  voz.fala("tosse")
  Expresoes.img('perdaOufatoGosto.jpg')
  voz.fala("ou perda de oufato ou paladar sim ou não")
  Expresoes.pergunta()

  while frase == "sim" or frase == "sim": 
    frase = respostaSintomas()
    if "sim" == frase:
      return False
    if "nao" == frase:
      return True
    else:
      voz.fala("responda com sim ou não")

#interação com visitante sobre precauções com contaminação com covid
def RecomendaçõesGerais():
  Expresoes.sorriso()
  voz.fala("seja bem vindo")
  Expresoes.img('distancialmeto.jpg')
  voz.fala("recomendamos o distanciamento social de 1 metro")
  expresoes.img('álcoolemGel.jpg')
  voz.fala("e antes de entrar no recinto utile os álcool em gel nas mãos")
  Expresoes.sorriso()
  
#função de inteção com visitante para negar a entra do mesmo 
def entradaNegada(causa):
  Expresoes.triste()
  if causa == "sem mascara":
    voz.fala("coloque a mascara para entrar no recinto")
  if causa == "sintomasAparente"
    voz.fala("voce apresentou alguns sitomas, recomendamos que volte outro dia para possiveis riscos de contaminação")
  else:
    voz.fala("entrada negada")
