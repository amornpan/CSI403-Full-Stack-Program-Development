"""
Test cases for docker-compose.yml
=================================
ใช้สำหรับ auto-grading Week 03

คะแนน: 40 คะแนน
"""

import pytest
import yaml
import os


# Load docker-compose.yml
COMPOSE_FILE = os.path.join(os.path.dirname(__file__), '..', 'docker-compose.yml')


def load_compose():
    """Load and parse docker-compose.yml"""
    with open(COMPOSE_FILE, 'r') as f:
        return yaml.safe_load(f)


class TestDockerCompose:
    """Test docker-compose.yml configuration"""
    
    def test_file_exists(self):
        """ทดสอบว่าไฟล์ docker-compose.yml มีอยู่"""
        assert os.path.exists(COMPOSE_FILE), "docker-compose.yml not found"
    
    def test_valid_yaml(self):
        """ทดสอบว่า YAML syntax ถูกต้อง"""
        try:
            compose = load_compose()
            assert compose is not None
        except yaml.YAMLError as e:
            pytest.fail(f"Invalid YAML syntax: {e}")
    
    def test_opensearch_service_exists(self):
        """ทดสอบว่ามี opensearch service"""
        compose = load_compose()
        assert 'services' in compose, "No services defined"
        assert 'opensearch' in compose['services'], "opensearch service not found"


class TestEnvironmentVariables:
    """Test OpenSearch environment variables (TODO 1 - 15 คะแนน)"""
    
    def test_discovery_type(self):
        """ทดสอบ discovery.type=single-node (3 คะแนน)"""
        compose = load_compose()
        env = compose['services']['opensearch'].get('environment', [])
        
        # Convert to dict if list
        if isinstance(env, list):
            env_dict = {}
            for item in env:
                if '=' in str(item):
                    key, value = str(item).split('=', 1)
                    env_dict[key] = value
        else:
            env_dict = env
        
        assert 'discovery.type' in env_dict or any('discovery.type=single-node' in str(e) for e in env), \
            "Missing discovery.type=single-node"
    
    def test_memory_lock(self):
        """ทดสอบ bootstrap.memory_lock=true (3 คะแนน)"""
        compose = load_compose()
        env = compose['services']['opensearch'].get('environment', [])
        
        has_memory_lock = any('bootstrap.memory_lock' in str(e) for e in env)
        assert has_memory_lock, "Missing bootstrap.memory_lock=true"
    
    def test_java_opts(self):
        """ทดสอบ OPENSEARCH_JAVA_OPTS (3 คะแนน)"""
        compose = load_compose()
        env = compose['services']['opensearch'].get('environment', [])
        
        has_java_opts = any('OPENSEARCH_JAVA_OPTS' in str(e) for e in env)
        assert has_java_opts, "Missing OPENSEARCH_JAVA_OPTS"
    
    def test_security_disabled(self):
        """ทดสอบ DISABLE_SECURITY_PLUGIN=true (3 คะแนน)"""
        compose = load_compose()
        env = compose['services']['opensearch'].get('environment', [])
        
        has_security = any('DISABLE_SECURITY_PLUGIN' in str(e) for e in env)
        assert has_security, "Missing DISABLE_SECURITY_PLUGIN=true"
    
    def test_demo_config_disabled(self):
        """ทดสอบ DISABLE_INSTALL_DEMO_CONFIG=true (3 คะแนน)"""
        compose = load_compose()
        env = compose['services']['opensearch'].get('environment', [])
        
        has_demo = any('DISABLE_INSTALL_DEMO_CONFIG' in str(e) for e in env)
        assert has_demo, "Missing DISABLE_INSTALL_DEMO_CONFIG=true"


class TestPortsMapping:
    """Test ports mapping (TODO 2 - 10 คะแนน)"""
    
    def test_port_9200(self):
        """ทดสอบ port 9200 mapping (5 คะแนน)"""
        compose = load_compose()
        ports = compose['services']['opensearch'].get('ports', [])
        
        has_9200 = any('9200' in str(p) for p in ports)
        assert has_9200, "Missing port 9200 mapping"
    
    def test_port_9600(self):
        """ทดสอบ port 9600 mapping (5 คะแนน)"""
        compose = load_compose()
        ports = compose['services']['opensearch'].get('ports', [])
        
        has_9600 = any('9600' in str(p) for p in ports)
        assert has_9600, "Missing port 9600 mapping"


class TestHealthcheck:
    """Test healthcheck configuration (TODO 3 - 15 คะแนน)"""
    
    def test_healthcheck_exists(self):
        """ทดสอบว่ามี healthcheck (5 คะแนน)"""
        compose = load_compose()
        healthcheck = compose['services']['opensearch'].get('healthcheck', {})
        
        assert healthcheck, "Missing healthcheck configuration"
    
    def test_healthcheck_test(self):
        """ทดสอบ healthcheck test command (5 คะแนน)"""
        compose = load_compose()
        healthcheck = compose['services']['opensearch'].get('healthcheck', {})
        test = healthcheck.get('test', [])
        
        # ต้องมี curl และ localhost:9200
        test_str = str(test)
        has_curl = 'curl' in test_str.lower()
        has_9200 = '9200' in test_str
        
        assert has_curl and has_9200, "Healthcheck should use curl to check localhost:9200"
    
    def test_healthcheck_interval(self):
        """ทดสอบ healthcheck interval (5 คะแนน)"""
        compose = load_compose()
        healthcheck = compose['services']['opensearch'].get('healthcheck', {})
        
        assert 'interval' in healthcheck, "Missing healthcheck interval"


# ==========================================
# รันไฟล์นี้โดยตรงเพื่อทดสอบ
# ==========================================
if __name__ == "__main__":
    pytest.main([__file__, "-v"])
