from generic_api_stuff.Alerts import SEVERITY, Alert
import pytest
import json

def test_alert_creation():
    assert Alert(message="test") == Alert(severity=SEVERITY.INFO,message="test")
    assert Alert(message="test123") != Alert(severity=SEVERITY.DANGER,message="test123")

    with pytest.raises(ValueError):
        Alert(message=123)
        Alert(message="test",severity="DANGER")

def test_alert_serialisation():
    alert1 = Alert(message="test123").dict()
    alert2 = Alert(message="test123", severity=SEVERITY.DANGER).dict()
    assert alert1 == {'message': 'test123', 'severity': SEVERITY.INFO}
    assert alert2 == {'message': 'test123', 'severity': SEVERITY.DANGER}
    assert json.dumps(alert1) == """{"message": "test123", "severity": "info"}"""
    assert json.dumps(alert2) == """{"message": "test123", "severity": "danger"}"""