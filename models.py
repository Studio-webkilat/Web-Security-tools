from pydantic import BaseModel, HttpUrl

class SecurityScanRequest(BaseModel):
    target_url: HttpUrl
    scan_type: str = "basic"

class SecurityResponse(BaseModel):
    status: str
    message: str
    data: dict
