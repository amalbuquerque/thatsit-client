#########################################################################
## This scaffolding model makes your app work on Google App Engine too
#########################################################################

# use SQLite
db = DAL('sqlite://storage.sqlite')

db.define_table(
    'spot',
    Field('filename', notnull=True, unique=True),
    Field('description'),
    # in seconds
    Field('time', 'integer', notnull=True),
    Field('position', 'integer'),
    Field('file', 'upload'),
    Field('uploader', notnull=True),
    Field('timestamp', 'datetime', notnull=True),
    # how records of this table should be represented
    # when referenced by another table in forms (dropboxes)
    format = '%(filename)s',
    singular = 'Spot',
    plural = 'Spots',
    )

db.spot.filename.requires = [IS_NOT_EMPTY(), IS_NOT_IN_DB(db, 'spot.filename')]
db.spot.uploader.requires = IS_NOT_EMPTY()
db.spot.time.requires = IS_INT_IN_RANGE(1, 300)

def get(table, **fields):
	"""
	Returns record from table with passed field values.
	'table' is a DAL table reference, such as 'db.spot'
	fields are field=value pairs
    Example:
        xpto_spot = get_or_create(db.spot, filename="xptoone.swf", \
                description="", time=30, position=2, uploader="admin", \
                timestamp = datetime.now()
	"""
	return table(**fields)

def get_or_create(table, **fields):
	"""
	Returns record from table with passed field values.
	Creates record if it does not exist.
	'table' is a DAL table reference, such as 'db.spot'
	fields are field=value pairs
    Example:
        xpto_spot = get_or_create(db.spot, filename="xptoone.swf", \
                description="", time=30, position=2, uploader="admin", \
                timestamp = datetime.now()
	"""
	return table(**fields) or table.insert(**fields)

def update_or_create(table, fields, updatefields):
	"""
	Modifies record that matches 'fields' with 'updatefields'.
	If record does not exist then create it.
	
	'table' is a DAL table reference, such as 'db.spot'
	'fields' and 'updatefields' are dictionaries
    Example:
        xpto_spot = update_or_create(db.spot, dict(filename="xptoone.swf"), \
                dict(filename="xpto_new_name.swf"))
	"""
	row = table(**fields)
	if row:
		row.update_record(**updatefields)
	else:
		fields.update(updatefields)
		row = table.insert(**fields)
	return row
