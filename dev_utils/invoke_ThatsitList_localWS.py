from gluon.contrib.pysimplesoap.client import SoapClient
import os
import base64

client = SoapClient(wsdl="http://localhost:8000/thatsitclient/client_soap/call/soap?WSDL")

invoke_res = client.ThatsitList(filename="largest.swf")
print("Answer {0}".format(invoke_res))
