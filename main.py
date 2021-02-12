#script triagem da COVID-19

import triagem
import paho.mqtt.client as mqtt 
from datetime import datetime

# variaveis de envio via MQTT
entrada = "null"
nomeVisitante = "null"
nomeVisitante = perguntaNome()

#interação principal com o visitante 
if usandoMascara():
  PerguntaSitomas()
  if respostaSintomas():
    RecomendaçõesGerais()
    entrada = "entradaAceita"
  else:
    entradaNegada("sintomasAparente")
    entrada = "entradaNegada"
else:
  entradaNegada("mascara")
  entrada = "entradaNegada"

#conexão com sever MQTT
mqttSever ="mqtt.empresa.com" 
client = mqtt.Client("Robios1")
client.connect(mqttServer) 

agora = datetime.now()
#publicando o nome visitante como chave e a data e hora da visita e se ele entrou ou nao no recinto 
client.publish(nomeVisitante, str(agora) + "_" + str(entrada))

