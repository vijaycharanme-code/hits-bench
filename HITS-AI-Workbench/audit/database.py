import sqlite3
import json
from pathlib import Path
from core.config import DB_DIR
from core.logging import logger
from datetime import datetime

class AuditDB:
    def __init__(self):
        self.db_path = DB_DIR / "audit.db"
        self._init_db()

    def _init_db(self):
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS audit_logs (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        timestamp TEXT NOT NULL,
                        session_id TEXT,
                        request TEXT,
                        laya_decision TEXT,
                        agent TEXT,
                        model TEXT,
                        tools TEXT,
                        verification_passed BOOLEAN,
                        retry_count INTEGER,
                        final_result TEXT,
                        errors TEXT
                    )
                ''')
                conn.commit()
        except Exception as e:
            logger.error(f"Failed to initialize AuditDB: {e}")

    def log_request(self, session_id: str, request: str, decision: dict,
                    agent: str, model: str, tools: list, verification: bool,
                    retries: int, final_result: str, errors: str = None):
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    INSERT INTO audit_logs
                    (timestamp, session_id, request, laya_decision, agent, model, tools, verification_passed, retry_count, final_result, errors)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                ''', (
                    datetime.now().isoformat(),
                    session_id,
                    request,
                    json.dumps(decision),
                    agent,
                    model,
                    json.dumps(tools),
                    verification,
                    retries,
                    final_result,
                    errors
                ))
                conn.commit()
        except Exception as e:
            logger.error(f"Failed to write to AuditDB: {e}")

audit_db = AuditDB()
