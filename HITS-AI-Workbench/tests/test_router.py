import pytest
from laya.router import LayaRouter
from laya.security import check_security
from laya.classifier import classify_task

def test_security_check():
    res = check_security("please rm -rf /")
    assert not res["safe"]

    res = check_security("summarize this doc")
    assert res["safe"]

def test_classify_task():
    res = classify_task("verify this document")
    assert res["task_type"] == "document_verification"
    assert res["agent"] == "document_agent"

    res = classify_task("calculate technical specs")
    assert res["agent"] == "engineer_agent"

def test_router():
    router = LayaRouter()
    decision = router.process_request("calculate the load capacity")
    assert decision["safe"]
    assert decision["agent"] == "engineer_agent"
    assert "calculator" in decision["tools"]
