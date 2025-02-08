import spacy
from collections import Counter
from string import punctuation
from typing import List, Tuple, Set

class KeywordExtractor:
    def __init__(self):
        # Load English language model
        self.nlp = spacy.load("en_core_web_sm")
        
        # Common English stop words to filter out
        self.custom_stop_words = {
            'example', 'various', 'etc', 'different', 'various', 'want',
            'good', 'better', 'best', 'make', 'need', 'look', 'many'
        }
        
    def preprocess_text(self, text: str) -> str:
        """Clean and preprocess the input text."""
        # Remove extra whitespace and convert to lowercase
        text = ' '.join(text.split())
        return text.lower().strip()
    
    def extract_keywords(self, text: str, num_keywords: int = 10) -> List[Tuple[str, float]]:
        """Extract keywords from text using spaCy's word importance scoring."""
        # Preprocess text
        text = self.preprocess_text(text)
        
        # Process text with spaCy
        doc = self.nlp(text)
        
        # Extract candidate keywords
        keywords = []
        for token in doc:
            if (
                not token.is_stop and
                not token.is_punct and
                not token.like_num and
                token.text.strip() not in self.custom_stop_words and
                len(token.text.strip()) > 2  # Filter out very short words
            ):
                # Calculate word importance score
                importance_score = (
                    token.prob *  # Word probability
                    (1 + token.dep_ != 'punct') *  # Boost for non-punctuation
                    (1 + token.pos_ in {'NOUN', 'PROPN', 'ADJ'})  # Boost for important POS
                )
                keywords.append((token.text, importance_score))
        
        # Sort by importance score and return top keywords
        keywords.sort(key=lambda x: x[1], reverse=True)
        return keywords[:num_keywords]
    
    def extract_phrases(self, text: str, num_phrases: int = 5) -> List[str]:
        """Extract key phrases using noun chunks and named entities."""
        text = self.preprocess_text(text)
        doc = self.nlp(text)
        
        phrases = set()
        
        # Extract noun chunks
        for chunk in doc.noun_chunks:
            if len(chunk.text.split()) >= 2:  # Only phrases with 2+ words
                phrases.add(chunk.text)
        
        # Extract named entities
        for ent in doc.ents:
            phrases.add(ent.text)
        
        # Sort by length and return top phrases
        return sorted(list(phrases), key=len)[:num_phrases]
    
    def generate_tags(self, text: str, num_tags: int = 5) -> Set[str]:
        """Generate blog tags from text combining keywords and phrases."""
        # Get both keywords and phrases
        keywords = self.extract_keywords(text, num_tags * 2)
        phrases = self.extract_phrases(text, num_tags)
        
        # Combine and clean tags
        tags = set()
        
        # Add single-word keywords
        for keyword, _ in keywords:
            if len(tags) < num_tags:
                tags.add(keyword.replace(' ', '-'))
        
        # Add multi-word phrases as tags
        for phrase in phrases:
            if len(tags) < num_tags:
                tags.add(phrase.replace(' ', '-'))
        
        return tags

def main():
    # Example usage
    text = """
    Artificial Intelligence and Machine Learning are transforming the technology landscape.
    Deep learning models have achieved remarkable results in natural language processing
    and computer vision tasks. Companies are increasingly adopting AI solutions to
    automate processes and gain insights from their data. The future of AI looks
    promising with continuous advancements in neural networks and reinforcement learning.
    """
    
    extractor = KeywordExtractor()
    
    print("Keywords:")
    for keyword, score in extractor.extract_keywords(text, 5):
        print(f"- {keyword}: {score:.4f}")
    
    print("\nKey Phrases:")
    for phrase in extractor.extract_phrases(text, 3):
        print(f"- {phrase}")
    
    print("\nBlog Tags:")
    tags = extractor.generate_tags(text, 5)
    print(", ".join(tags))

if __name__ == "__main__":
    main()
