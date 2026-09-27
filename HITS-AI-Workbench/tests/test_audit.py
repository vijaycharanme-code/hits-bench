import pytest
from audit.database import audit_db

def test_audit_log_creation():
    # Attempt a simple write
    try:
        audit_db.log_request(
            session_id="123",
            request="test",
            decision={},
            agent="test_agent",
            model="test_model",
            tools=[],
            verification=True,
            retries=0,
            final_result="Success"
        )
        assert True
    except Exception:
        assert False
