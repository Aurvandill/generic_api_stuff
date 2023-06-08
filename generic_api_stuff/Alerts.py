from enum import Enum
from pydantic import BaseModel

# Pyhton 3.9 does not have a StrEnum :(
class SEVERITY(str,Enum):
    PRIMARY = "primary"
    SECONDARY = "secondary"
    SUCCESS = "success"
    DANGER = "danger"
    WARNING = "warning"
    INFO = "info"
    LIGHT = "light"
    DARK = "dark"

#@dataclass
class Alert(BaseModel):
    message:str
    severity:SEVERITY = SEVERITY.INFO