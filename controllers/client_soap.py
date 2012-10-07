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
def upload1(filename, description, time, position,\
        uploader, content):
    import base64
    import os
    to_return = "Received: {0},{1},{2},{3},{4};".\
            format(filename, description, time,\
            position, uploader)
    to_return = to_return + "Raw "
    to_return = to_return + str(len(content)) + " bytes"

    converted = base64.\
            standard_b64decode(content)
            
    # to_return = to_return + converted
    path_to_write = os.path.join(\
            settings.movies_path, filename)
    try:
        with open(path_to_write, "wb") as file:
            file.write(converted)
        to_return = to_return + str(len(converted))\
                + " bytes converted on " + path_to_write
    except:
        to_return = to_return + "[ERROR]"
    return to_return
