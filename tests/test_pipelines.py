import pytest
from pipelines.extraction_pipeline import ExtractionPipeline
from pipelines.nlp_pipeline import NLPPipeline
from pipelines.embedding_pipeline import EmbeddingPipeline

@pytest.fixture
def sample_pdf_data():
    return b"%PDF-1.4\n...mock pdf data..."

def test_full_pipeline(sample_pdf_data):
    # Set up the pipelines
    extraction_pipeline = ExtractionPipeline()
    nlp_pipeline = NLPPipeline()
    embedding_pipeline = EmbeddingPipeline()
    
    # Simulate PDF extraction
    extracted_data = extraction_pipeline.extract(sample_pdf_data)
    
    # Simulate NLP processing
    processed_data = nlp_pipeline.process(extracted_data)
    
    # Simulate embedding generation
    embeddings = embedding_pipeline.embed(processed_data)
    
    # Assertions for each step
    assert isinstance(extracted_data, str)
    assert len(processed_data) > 0  # Check if data was processed
    assert isinstance(embeddings, list)  # Check if embeddings are returned as list
