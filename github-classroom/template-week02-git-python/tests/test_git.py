"""
Test Git Commits
================
ตรวจสอบว่านักศึกษา commit อย่างน้อย 3 ครั้ง

คะแนน: 20 คะแนน
"""

import pytest
import subprocess
import os


class TestGitCommits:
    """Test Git commit history"""
    
    def test_minimum_commits(self):
        """ทดสอบว่ามี commits อย่างน้อย 3 ครั้ง (20 คะแนน)"""
        try:
            # นับจำนวน commits
            result = subprocess.run(
                ["git", "rev-list", "--count", "HEAD"],
                capture_output=True,
                text=True,
                cwd=os.path.dirname(os.path.dirname(__file__))
            )
            
            if result.returncode != 0:
                pytest.skip("Not a git repository or git not available")
            
            commit_count = int(result.stdout.strip())
            
            # ต้องมีอย่างน้อย 3 commits (ไม่นับ initial commit จาก template)
            # Template มี 1 commit อยู่แล้ว ดังนั้นต้องมีทั้งหมด >= 4
            assert commit_count >= 4, (
                f"ต้องมี commits อย่างน้อย 3 ครั้ง (จากนักศึกษา)\n"
                f"ปัจจุบันมี {commit_count - 1} commits จากนักศึกษา\n"
                f"(ไม่นับ initial commit จาก template)"
            )
            
        except FileNotFoundError:
            pytest.skip("Git not installed")
    
    def test_commit_messages_not_empty(self):
        """ทดสอบว่า commit messages ไม่ว่างเปล่า"""
        try:
            result = subprocess.run(
                ["git", "log", "--format=%s", "-10"],
                capture_output=True,
                text=True,
                cwd=os.path.dirname(os.path.dirname(__file__))
            )
            
            if result.returncode != 0:
                pytest.skip("Not a git repository")
            
            messages = result.stdout.strip().split('\n')
            
            for msg in messages:
                assert len(msg) > 0, "Commit message should not be empty"
                assert len(msg) >= 5, f"Commit message too short: '{msg}'"
                
        except FileNotFoundError:
            pytest.skip("Git not installed")


# ==========================================
# รันไฟล์นี้โดยตรงเพื่อทดสอบ
# ==========================================
if __name__ == "__main__":
    pytest.main([__file__, "-v"])
