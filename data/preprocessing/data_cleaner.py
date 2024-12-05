import pandas as pd
import PyPDF2
from langchain import LangChain

# Class for data cleansing logic (Class: `DataCleansing`)
# Cleansing logic for pdf data (Class: `PdfDataCleansing`) and excel data (Class: `ExcelDataCleansing`)
# Use langchain to access pypdf2 for pdf data extraction
class DataCleansing:
    def __init__(self, data):
        self.data = data

    def clean_data(self):
        # Implement general data cleansing logic here
        pass

class PdfDataCleansing(DataCleansing):
    def __init__(self, pdf_path):
        self.pdf_path = pdf_path
        self.data = self.extract_pdf_data()

    def extract_pdf_data(self):
        with open(self.pdf_path, 'rb') as file:
            reader = PyPDF2.PdfFileReader(file)
            text = ''
            for page_num in range(reader.numPages):
                text += reader.getPage(page_num).extractText()
        return text

    def clean_data(self):
        # Implement PDF specific data cleansing logic here
        pass

class ExcelDataCleansing(DataCleansing):
    def __init__(self, excel_path):
        self.excel_path = excel_path
        self.data = self.extract_excel_data()

    def extract_excel_data(self):
        return pd.read_excel(self.excel_path)

    def clean_data(self):
        # Implement Excel specific data cleansing logic here
        pass