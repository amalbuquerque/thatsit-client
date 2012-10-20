from gluon.contrib.pysimplesoap.client import SoapClient
import os
import base64

client = SoapClient(wsdl="http://localhost:8000/thatsitclient/client_soap/call/soap?WSDL")

# content "heyho lets go (based 64)"
content_64 = "aGV5aG8gbGV0cyBnbw=="

path_to_send = os.path.join("C:\\dados\\projectos\\thatsit\\movies_test_upload", "largest.swf")
# path_to_send = os.path.join("C:\\dados\\projectos\\thatsit\\movies_test_upload", "text.txt")
with open(path_to_send, "rb") as file_to_send:
    raw_content = file_to_send.read()
    print("Raw {0} bytes".format(len(raw_content)))
    content_64 = base64.standard_b64encode(raw_content)
    content_64_to_send = unicode(content_64)

print("Will send {0} bytes".format(len(content_64_to_send)))
invoke_res = client.ThatsitUpload(filename="largest.swf", description="desc",\
        time=30, position=1, uploader="lejboua", content=content_64_to_send)

print("Answer {0}".format(invoke_res))
