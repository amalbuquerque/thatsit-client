from gluon.tools import Service
service = Service()

def call():
    # remove forget() if you plan
    # to use session cookies with services
    session.forget()
    return service()

@service.soap('ThatsitUpload', returns={'result':str},
        args={'filename':str, 'description':str, 
            'time':int, 'position':int,
            'uploader':str,
            'content':str})
def upload(filename, description, time, position,\
        uploader, content):
    import base64
    import os
    import cStringIO
    from datetime import datetime
    to_return = "Received: {0},{1},{2},{3},{4};".\
            format(filename, description, time,\
            position, uploader)
    to_return = to_return + "Raw "
    to_return = to_return + str(len(content)) + " bytes"
    logger.debug("Before: " + to_return)

    converted = base64.\
            standard_b64decode(content)
            
    # escrever na pasta onde ficarao
    # os filmes para serem mostrados
    # Nota: Escrevemos primeiro na pasta onde
    # ficarao porque depois precisamos da stream
    # para que o insert na BD do field upload
    # funcione
    path_to_write = os.path.join(\
            settings.movies_path, filename)
    try:
        with open(path_to_write, "wb") as file:
            file.write(converted)
        to_return = to_return + str(len(converted))\
                + " bytes converted on " + path_to_write
    except:
        return to_return + "[ERROR]"

    # guarda na pasta onde ficam os ficheiros
    # recebidos
    with open(path_to_write, "rb") as temp_to_use:
        spot_uploaded = update_or_create(db.spot,\
                dict(filename=filename),\
                dict(description=description, time=time,\
                    position=position,uploader=uploader,\
                    timestamp=datetime.now(),\
                    movie=temp_to_use))

    logger.debug("Saved upload: {}".\
            format(get(db.spot,filename=filename).movie))

    return to_return

@service.soap('ThatsitList', returns={'result':db.spot},
        args={'filename':str})
def upload(filename):
    import base64
    import os
    import cStringIO
    from datetime import datetime
    #to_return = "Received: {0},{1},{2},{3},{4};".\
    #        format(filename, description, time,\
    #        position, uploader)
    #to_return = to_return + "Raw "
    to_return = get(db.spot,filename=filename)
    return to_return
