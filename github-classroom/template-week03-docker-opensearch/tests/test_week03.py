"""
Test cases for Week 03: Docker + OpenSearch
===========================================
ใช้สำหรับ auto-grading

คะแนน: 70 คะแนน (ไม่รวม screenshots และ README)
"""

import pytest
import yaml
import subprocess
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))


class TestDockerCompose:
    """Test docker-compose.yml (40 คะแนน)"""
    
    @pytest.fixture
    def compose_config(self):
        """Load docker-compose.yml"""
        compose_path = os.path.join(
            os.path.dirname(__file__), '..', 'docker-compose.yml'
        )
        with open(compose_path, 'r') as f:
            return yaml.safe_load(f)
    
    def test_opensearch_service_exists(self, compose_config):
        """ทดสอบว่ามี opensearch service (10 คะแนน)"""
        assert 'services' in compose_config
        assert 'opensearch' in compose_config['services']
    
    def test_environment_variables(self, compose_config):
        """ทดสอบ environment variables (10 คะแนน)"""
        opensearch = compose_config['services']['opensearch']
        env = opensearch.get('environment', [])
        
        # แปลงเป็น dict ถ้าเป็น list
        if isinstance(env, list):
            env_dict = {}
            for item in env:
                if '=' in str(item):
                    key, value = str(item).split('=', 1)
                    env_dict[key] = value
            env = env_dict
        
        required_vars = [
            'discovery.type',
            'bootstrap.memory_lock',
            'DISABLE_SECURITY_PLUGIN'
        ]
        
        for var in required_vars:
            assert var in env or any(var in str(e) for e in opensearch.get('environment', [])), \
                f"Missing environment variable: {var}"
    
    def test_ports_mapping(self, compose_config):
        """ทดสอบ ports mapping (10 คะแนน)"""
        opensearch = compose_config['services']['opensearch']
        ports = opensearch.get('ports', [])
        
        # ตรวจสอบว่ามี port 9200
        port_strings = [str(p) for p in ports]
        has_9200 = any('9200' in p for p in port_strings)
        
        assert has_9200, "Missing port 9200 mapping"
    
    def test_healthcheck_exists(self, compose_config):
        """ทดสอบ healthcheck (10 คะแนน)"""
        opensearch = compose_config['services']['opensearch']
        
        assert 'healthcheck' in opensearch, "Missing healthcheck configuration"
        
        healthcheck = opensearch['healthcheck']
        assert 'test' in healthcheck, "Missing healthcheck test"
        assert 'interval' in healthcheck, "Missing healthcheck interval"


class TestSetupScript:
    """Test setup_opensearch.py (30 คะแนน)"""
    
    def test_check_connection_function_exists(self):
        """ทดสอบว่ามี function check_connection (10 คะแนน)"""
        from setup_opensearch import check_connection
        assert callable(check_connection)
    
    def test_create_index_function_exists(self):
        """ทดสอบว่ามี function create_index (10 คะแนน)"""
        from setup_opensearch import create_index
        assert callable(create_index)
    
    def test_setup_hybrid_pipeline_function_exists(self):
        """ทดสอบว่ามี function setup_hybrid_pipeline (10 คะแนน)"""
        from setup_opensearch import setup_hybrid_pipeline
        assert callable(setup_hybrid_pipeline)


class TestDockerComposeYAMLSyntax:
    """Test YAML syntax"""
    
    def test_valid_yaml(self):
        """ทดสอบว่า docker-compose.yml เป็น valid YAML"""
        compose_path = os.path.join(
            os.path.dirname(__file__), '..', 'docker-compose.yml'
        )
        
        try:
            with open(compose_path, 'r') as f:
                config = yaml.safe_load(f)
            assert config is not None
        except yaml.YAMLError as e:
            pytest.fail(f"Invalid YAML syntax: {e}")


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
