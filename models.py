from pydantic import BaseModel, HttpUrl
from typing import Dict, List

# Model untuk input request
class SecurityScanRequest(BaseModel):
    target_url: HttpUrl
    scan_type: str = "basic"

# Model untuk struktur data hasil scan agar lebih terstruktur
class ScanData(BaseModel):
    score: int
    details: Dict[str, str]
    recommendations: List[str]

# Model utama untuk respon
class SecurityResponse(BaseModel):
    status: str
    message: str
    data: ScanData
