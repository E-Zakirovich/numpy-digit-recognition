import numpy as np
import struct 
from config import test_images ,test_labels, train_images,train_labels

class LoadDataset:
	def load_images(self, path: str) -> np.ndarray:
		pass
		
	def load_labels(self, path: str) -> np.ndarray:
		pass
		
	def train_data(self) -> tuple[np.ndarray, np.ndarray]:
		pass
		
	def test_data(self) -> tuple[np.ndarray, np.ndarray]:
		pass