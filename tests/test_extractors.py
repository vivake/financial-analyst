import pytest
from extractors.pdf_extractor import PDFExtractor

@pytest.fixture
def mock_pdf_data():
    # This could be a mock or a sample of a PDF file
    return b"%PDF-1.4\n...Your mock pdf content here..."

def test_pdf_extractor(mock_pdf_data):
    # Create an instance of the extractor
    extractor = PDFExtractor()
    
    # Mock the file reading function to return mock data
    extractor.read_pdf = lambda x: mock_pdf_data
    
    # Call the extract method
    content = extractor.extract_text("path_to_mock_pdf")
    
    # Check if the content extracted is as expected
    assert "expected text" in content
    assert isinstance(content, str)  # Ensure it's a string
import pytest
from extractors.excel_extractor import ExcelExtractor

@pytest.fixture
def sample_excel_data():
    # Mock sample Excel data, represented as a string
    return [
        ["Date", "Revenue", "Expenses"],
        ["2023-12-01", "1000", "500"],
        ["2023-12-02", "1500", "600"]
    ]

def test_excel_extractor(sample_excel_data):
    extractor = ExcelExtractor()
    
    # Mocking the file read operation to return the sample data
    extractor.read_excel = lambda x: sample_excel_data
    
    # Extracting data from the Excel file
    content = extractor.extract_table("mock_excel_file_path")
    
    # Asserting the result
    assert isinstance(content, list)  # Should return a list of rows
    assert len(content) == 3  # Number of rows including header
    assert content[1][0] == "2023-12-01"  # Check if the first date is correct
    assert content[1][1] == "1000"  # Revenue value is correct