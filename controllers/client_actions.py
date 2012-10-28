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

def log_test():
    logger.debug("DEBUG WELL")
    logger.warning("WARNING WELL")

def get_benfica_rss():
    import gluon.contrib.feedparser as feedparser
    d = feedparser.parse(
        "http://feeds.record.xl.pt/?idcanal=11")
    return dict(title=d.channel.title,
                link = d.channel.link,
                description = d.channel.description,
                created_on = request.now,
                entries = [
                  dict(title = entry.title,
                  link = entry.link,
                  description = entry.description,
                  created_on = request.now) for entry in d.entries])

def upload_example():
    response.files.append(URL(r=request, c='static/js', f='fileuploader.js'))
    response.files.append(URL(r=request, c='static/css', f='fileuploader.css'))
    response.files.append(URL(r=request, c='static/js/thatsit/global', f='use_fileuploader.js'))
    return dict(message = "abcd")

def upload():
    """
    Permite utilizador fazer o upload de um spot e de
    criar a BE correspondente na BD. Sera implementado
    do lado do manager.
    1. Guarda ficheiro nos uploads
    2. Converte o movie para .swf
    3. Invoca o WebService do Cliente para fazer o upload
       do filme
    """
    try:
        for r in request.vars:
            if r=="qqfile":
                filename = request.vars.qqfile
                # process the file here
                gen_filename = db.spot.file.store(request.body, filename)
                logger.debug("Wrote {} bytes to {}"\
                        .format(len(request.body), filename))
                logger.warning("*Warning*Wrote {} bytes to {}"\
                        .format(len(request.body), filename))
                # db.document.insert(file=db.spot.file.store(request.body,filename))
                return response.json({'success': 'true',\
                        'upl_file' : filename,\
                        'new_file' : gen_filename})
    except:
        return response.json({'success': 'false'})
