# Keyword Extractor

A Python-based keyword extraction tool that uses Natural Language Processing (NLP) to extract meaningful keywords, phrases, and generate blog tags from text content. Built with spaCy, this tool provides intelligent keyword extraction with importance scoring and automated tag generation capabilities.

## Features

- **Intelligent Keyword Extraction**: Extracts keywords using spaCy's linguistic features and custom importance scoring
- **Key Phrase Identification**: Identifies meaningful multi-word expressions and named entities
- **Blog Tag Generation**: Automatically generates URL-friendly tags for blog posts
- **Customizable**: Easy to extend with custom stop words and scoring algorithms
- **Clean API**: Simple and intuitive interface for text analysis

## Installation

1. Clone the repository:
```bash
git clone https://github.com/makalin/keyword-extractor.git
cd keyword-extractor
```

2. Install required packages:
```bash
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

## Usage

### Basic Usage

```python
from keyword_extractor import KeywordExtractor

# Initialize the extractor
extractor = KeywordExtractor()

# Sample text
text = """
Artificial Intelligence and Machine Learning are transforming the technology landscape.
Deep learning models have achieved remarkable results in natural language processing
and computer vision tasks. Companies are increasingly adopting AI solutions to
automate processes and gain insights from their data.
"""

# Extract keywords with importance scores
keywords = extractor.extract_keywords(text, num_keywords=5)
print("Keywords:", keywords)

# Extract key phrases
phrases = extractor.extract_phrases(text, num_phrases=3)
print("Phrases:", phrases)

# Generate blog tags
tags = extractor.generate_tags(text, num_tags=5)
print("Tags:", tags)
```

### Example Output

```python
Keywords:
- artificial: 0.8532
- intelligence: 0.7845
- learning: 0.7456
- machine: 0.7234
- deep: 0.6789

Key Phrases:
- artificial intelligence
- machine learning
- deep learning models

Blog Tags:
artificial-intelligence, machine-learning, deep-learning, technology, data-insights
```

## Advanced Usage

### Customizing Stop Words

```python
extractor = KeywordExtractor()
extractor.custom_stop_words.update({'custom', 'stop', 'words'})
```

### Adjusting Output Size

```python
# Get more keywords
keywords = extractor.extract_keywords(text, num_keywords=15)

# Get more phrases
phrases = extractor.extract_phrases(text, num_phrases=10)

# Generate more tags
tags = extractor.generate_tags(text, num_tags=8)
```

## API Reference

### KeywordExtractor Class

#### `__init__()`
Initializes the KeywordExtractor with the English language model and default settings.

#### `extract_keywords(text: str, num_keywords: int = 10) -> List[Tuple[str, float]]`
Extracts keywords from text with importance scores.
- `text`: Input text to analyze
- `num_keywords`: Number of keywords to return
- Returns: List of tuples containing (keyword, importance_score)

#### `extract_phrases(text: str, num_phrases: int = 5) -> List[str]`
Extracts key phrases from text.
- `text`: Input text to analyze
- `num_phrases`: Number of phrases to return
- Returns: List of key phrases

#### `generate_tags(text: str, num_tags: int = 5) -> Set[str]`
Generates blog tags from text.
- `text`: Input text to analyze
- `num_tags`: Number of tags to generate
- Returns: Set of URL-friendly tags

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Built with [spaCy](https://spacy.io/)
- Inspired by RAKE algorithm and TextRank
- Thanks to all contributors!
