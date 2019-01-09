import os
import zipfile
import tempfile
from django.http import HttpResponse

class Document:

	TEXT_FILE = 'word/document.xml'

	def __init__(self, docxname):
		self.docxname = docxname
		self.file_path = 'relatorio/templates/relatorio/{}'.format(docxname)

	#from https://stackoverflow.com/questions/25738523/how-to-update-one-file-inside-zip-file-using-python
	def update_and_download(self, data):

		# generate a temp file
		tmpfd, tmpname = tempfile.mkstemp()
		os.close(tmpfd)

		# create a temp copy of the archive without filename            
		with zipfile.ZipFile(self.file_path, 'r') as zin:
			with zipfile.ZipFile(tmpname, 'w') as zout:
				zout.comment = zin.comment # preserve the comment
				for item in zin.infolist():
					if item.filename != self.TEXT_FILE:
						zout.writestr(item, zin.read(item.filename))

		# now add filename with its new data
		with zipfile.ZipFile(tmpname, mode='a', compression=zipfile.ZIP_DEFLATED) as zf:
			zf.writestr(self.TEXT_FILE, data)

		#Return HttpResponse for downloading
		with open(tmpname, 'rb') as fh:
			response = HttpResponse(fh.read(), content_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document")
			response['Content-Disposition'] = 'inline; filename=' + self.docxname
			return response

	def get_text_content(self):
		with zipfile.ZipFile(self.file_path) as zin:
			return zin.read(self.TEXT_FILE).decode('utf-8')
		