import pytest
from verification.document import verify_document

def test_document_verification():
    res = verify_document("dummy.pdf", expected_fields=[])
    assert res["status"] == "PASS"

    res = verify_document("dummy.pdf", expected_fields=["sig1", "sig2", "date"])
    assert res["status"] == "REVIEW"
