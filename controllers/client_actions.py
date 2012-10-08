def hello1():
    """ simple page without template """

    return "Hello World! Movies: " + settings.movies_path

def create1():
    from datetime import datetime
    xpto_spot = get_or_create(db.spot, filename=request.vars.name, \
            description="", time=30, position=2, uploader="admin", \
            timestamp = datetime.now())

    return "I think I've created something: {0}-{1} by {2} @ {3}".format( \
            xpto_spot.id, xpto_spot.filename, xpto_spot.uploader, xpto_spot.timestamp)

def check1():
    xpto_spot = get(db.spot, filename=request.vars.name)
    if (xpto_spot == None):
        return "Sorry. Nothing"
    return "I think I've found something: {0}-{1} by {2} @ {3}".format( \
            xpto_spot.id, xpto_spot.filename, xpto_spot.uploader, xpto_spot.timestamp)

# Adaptar o para utilizar
# com um Ajax uploader
def manager_upload_spot():
    """
    Permite utilizador fazer o upload de um spot e de
    criar a BE correspondente na BD. Sera implementado
    do lado do manager.
    1. Guarda ficheiro nos uploads
    2. Converte o movie para .swf
    3. Invoca o WebService do Cliente para fazer o upload
       do filme
    """
    import gluon.contrib.simplejson as sj
    import os

    received_filename = request.args(0)
    xpto_spot = get(db.spot, filename=received_filename)
    if (xpto_spot != None):
        return sj.dumps({"success": "false"})
    else:
        variables = request.vars
        data = variables.qqfile.value
        f = open(os.path.join(settings.movies_path, received_filename), "wb")
        try:
            # TODO: Verificar se chega no formato esperado
            data = base64.b64decode(data)
            f.write(data)
        finally:
            f.close()

