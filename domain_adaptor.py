from typing import Dict, Any

class DomainAdaptor:
    def __init__(self, domain_type: str):
        self.domain_type = domain_type

    def adapt(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Adapt data to the specific domain's format."""
        if self.domain_type == "nlp":
            return self._adapt_to_nlp(data)
        elif self.domain_type == "cv":
            return self._adapt_to_cv(data)
        else:
            raise ValueError(f"Unsupported domain type: {self.domain_type}")

    def _adapt_to_nlp(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Adapt data for NLP processing."""
        return {"text": str(data), "language": "en"}

    def _adapt_to_cv(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Adapt data for Computer Vision processing."""
        return {"image_path": data, "mode": "grayscale"}