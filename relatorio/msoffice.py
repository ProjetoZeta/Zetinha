import os
import zipfile
import tempfile
from django.http import HttpResponse

'''

	Estas classes manipulam arquivos docx e xlsx como arquivos zip. Ao fazerem alterações específicas em arquivos que
	fazem parte do pacote comprimido, as alterações correspondentes são observadas nos documentos docx e xlsx.
		

	O conteúdo dos arquivos docx são alterados através do arquivo 'word/document.xml'
	O conteúdo dos arquivos xlsx são alterados através dos arquivos:
		* xl/sharedStrings.xml => que mantem os textos simples
		* xl/drawings/*.vml => que mantém os estados dos checkboxes contidos nas planilhas (marcações especiais são feitas diretamente neste arquivo)

'''

class Document:

	def __init__(self, msfilename, content_path):
		self.msfilename = msfilename
		self.file_path = 'relatorio/templates/relatorio/msoffice/{}'.format(msfilename)
		self.content_path = content_path

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
					if item.filename != self.content_path:
						zout.writestr(item, zin.read(item.filename))

		# now add filename with its new data
		with zipfile.ZipFile(tmpname, mode='a', compression=zipfile.ZIP_DEFLATED) as zf:
			zf.writestr(self.content_path, data)

		#Return HttpResponse for downloading
		with open(tmpname, 'rb') as fh:
			response = HttpResponse(fh.read(), content_type=self.content_type)
			response['Content-Disposition'] = 'inline; filename=' + self.msfilename
			return response

	def get_text_content(self):
		with zipfile.ZipFile(self.file_path) as zin:
			return zin.read(self.content_path).decode('utf-8')


class Word(Document):

	def __init__(self, msfilename, content_path='word/document.xml'):
		self.content_type = "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
		super(Word, self).__init__(msfilename, content_path)


class Excel(Document):

	def __init__(self, msfilename, content_path='xl/sharedStrings.xml'):
		self.content_type = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
		super(Excel, self).__init__(msfilename, content_path)