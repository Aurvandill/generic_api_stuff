from generic_api_stuff.Alerts import SEVERITY
import json

def test_severity_serialisation():
    assert json.dumps(SEVERITY.DANGER) == '"danger"'
    assert json.dumps(SEVERITY.SECONDARY) == '"secondary"'
    assert json.dumps(SEVERITY.PRIMARY) == '"primary"'
    assert json.dumps(SEVERITY.SUCCESS) == '"success"'
    assert json.dumps(SEVERITY.DANGER) == '"danger"'
    assert json.dumps(SEVERITY.WARNING) == '"warning"'
    assert json.dumps(SEVERITY.INFO) == '"info"'
    assert json.dumps(SEVERITY.LIGHT) == '"light"'
    assert json.dumps(SEVERITY.DARK) == '"dark"'

def test_severity_from_str():
    assert SEVERITY.DANGER == SEVERITY("danger")
    assert SEVERITY.SECONDARY == SEVERITY("secondary")
    assert SEVERITY.PRIMARY == SEVERITY("primary")
    assert SEVERITY.SUCCESS == SEVERITY("success")
    assert SEVERITY.DANGER == SEVERITY("danger")
    assert SEVERITY.WARNING == SEVERITY("warning")
    assert SEVERITY.INFO == SEVERITY("info")
    assert SEVERITY.LIGHT == SEVERITY("light")
    assert SEVERITY.DARK == SEVERITY("dark")

def test_severity_value():
    assert SEVERITY.DANGER == "danger"
    assert SEVERITY.SECONDARY == "secondary"
    assert SEVERITY.PRIMARY == "primary"
    assert SEVERITY.SUCCESS == "success"
    assert SEVERITY.DANGER == "danger"
    assert SEVERITY.WARNING == "warning"
    assert SEVERITY.INFO == "info"
    assert SEVERITY.LIGHT == "light"
    assert SEVERITY.DARK == "dark"