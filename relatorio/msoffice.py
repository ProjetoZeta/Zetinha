import os
import zipfile
import tempfile
from django.http import HttpResponse
from relatorio.render import Render

'''

	Estas classes manipulam arquivos docx e xlsx como arquivos zip. Ao fazerem alterações específicas em arquivos que
	fazem parte do pacote comprimido, as alterações correspondentes são observadas nos documentos docx e xlsx.
		

	O conteúdo dos arquivos docx são alterados através do arquivo 'word/document.xml'
	O conteúdo dos arquivos xlsx são alterados através dos arquivos:
		* xl/sharedStrings.xml => que mantem os textos simples
		* xl/drawings/*.vml => que mantém os estados dos checkboxes contidos nas planilhas (marcações especiais são feitas diretamente neste arquivo)
		
'''

class Document:

	'''
		1 - Criar cópia de zip sem a lista de alvos
		2 - Inserir lista de alvos atualizados
		3 - Download de arquivo temporário atulizado
	'''
	def __init__(self, msfilename, dict_context, target_list):
		self.msfilename = msfilename
		self.file_path = 'relatorio/templates/relatorio/msoffice/{}'.format(msfilename)
		self.target_list = target_list
		self.dict_context = dict_context
		self.tmpfile_path = self.get_temp_copy_msfile_path()

	#from https://stackoverflow.com/questions/25738523/how-to-update-one-file-inside-zip-file-using-python
	def get_temp_copy_msfile_path(self):

		tmpfd, tmpname = tempfile.mkstemp()
		os.close(tmpfd)

		# create a temp copy of the archive without filename            
		with zipfile.ZipFile(self.file_path, 'r') as zin:
			with zipfile.ZipFile(tmpname, 'w') as zout:
				zout.comment = zin.comment # preserve the comment
				for item in zin.infolist():
					if item.filename not in self.target_list:
						zout.writestr(item, zin.read(item.filename))

		return tmpname

	def get_inner_template_zip_content(self, inner_file_path):
		with zipfile.ZipFile(self.file_path) as zin:
			return zin.read(inner_file_path).decode('utf-8')

	def render_targets(self):

		# now add filename with its new data
		with zipfile.ZipFile(self.tmpfile_path, mode='a', compression=zipfile.ZIP_DEFLATED) as zf:
			for target in self.target_list:
				processed_text = Render.text(self.get_inner_template_zip_content(target), self.dict_context)
				zf.writestr(target, processed_text)

	def update_and_download(self):

		self.render_targets()

		#Return HttpResponse for downloading
		with open(self.tmpfile_path, 'rb') as fh:
			response = HttpResponse(fh.read(), content_type=self.content_type)
			response['Content-Disposition'] = 'inline; filename=' + self.msfilename
			return response

class Word(Document):

	def __init__(self, msfilename, dict_context, target_list=['word/document.xml']):
		self.content_type = "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
		super(Word, self).__init__(msfilename, dict_context, target_list)


class Excel(Document):

	def __init__(self, msfilename, dict_context, target_list=['xl/sharedStrings.xml', 'xl/drawings/vmlDrawing1.vml']):
		self.content_type = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
		super(Excel, self).__init__(msfilename, dict_context, target_list)