import numpy as np
from typing import List, Dict

class SimpleTokenizer:
    """
    A word-level tokenizer with special tokens.
    """
    
    def __init__(self):
        self.word_to_id: Dict[str, int] = {}
        self.id_to_word: Dict[int, str] = {}
        self.vocab_size = 0
        
        # Special tokens
        self.pad_token = "<PAD>"
        self.unk_token = "<UNK>"
        self.bos_token = "<BOS>"
        self.eos_token = "<EOS>"
    
    def build_vocab(self, texts: List[str]) -> None:
        """
        Build vocabulary from a list of texts.
        Add special tokens first, then unique words.
        """
        # YOUR CODE HERE
        self.word_to_id.update({"<PAD>" : 0, "<UNK>" : 1, "<BOS>" : 2, "<EOS>" : 3}) 
        self.id_to_word.update({0 : "<PAD>", 1 : "<UNK>", 2 : "<BOS>", 3 : "<EOS>"})
        self.vocab_size = 4

        words = []
        for text in texts:
            words.extend(text.split(" "))
            
        new_texts = sorted(list(set(words)))
        for text in new_texts:
            self.word_to_id[text] = self.vocab_size
            self.id_to_word[self.vocab_size] = text
            self.vocab_size += 1

    def encode(self, text: str) -> List[int]:
        """
        Convert text to list of token IDs.
        Use UNK for unknown words.
        """
        # YOUR CODE HERE
        list_of_token_IDs = []
        tokens = text.split(" ")
        for token in tokens:
            if token not in self.word_to_id:
                token = "<UNK>"
            list_of_token_IDs.append(self.word_to_id[token])
        return list_of_token_IDs
    
    def decode(self, ids: List[int]) -> str:
        """
        Convert list of token IDs back to text.
        """
        # YOUR CODE HERE
        text = ""
        for id in ids:
            text += self.id_to_word[id]
            text += " "
        return text[:-1]
