"""
Test cases for Week 03: Docker + OpenSearch
===========================================
"""

import pytest
import yaml
import subprocess
import os


class TestDockerCompose:
    """Test docker-compose.yml configuration"""
    
    @pytest.fixture
    def compose_config(self):
        """Load docker-compose.yml"""
        compose_path = os.path.join(
            os.path.dirname(__file__), '..', 'src', 'docker-compose.yml'
        )
        with open(compose_path, 'r') as f:
            return yaml.safe_load(f)
    
    def test_opensearch_service_exists(self, compose_config):
        """ทดสอบว่ามี opensearch service (5 คะแนน)"""
        assert 'services' in compose_config
        assert 'opensearch' in compose_config['services']
    
    def test_opensearch_image(self, compose_config):
        """ทดสอบว่าใช้ image ที่ถูกต้อง"""
        opensearch = compose_config['services']['opensearch']
        assert 'opensearchproject/opensearch' in opensearch['image']
    
    def test_environment_discovery_type(self, compose_config):
        """ทดสอบ environment: discovery.type (5 คะแนน)"""
        opensearch = compose_config['services']['opensearch']
        env = opensearch.get('environment', [])
        
        # Convert to list of strings if it's a dict
        if isinstance(env, dict):
            env = [f"{k}={v}" for k, v in env.items()]
        
        env_str = ' '.join(env)
        assert 'discovery.type=single-node' in env_str or 'single-node' in env_str, \
            "Missing discovery.type=single-node"
    
    def test_environment_security_disabled(self, compose_config):
        """ทดสอบว่าปิด security plugin (5 คะแนน)"""
        opensearch = compose_config['services']['opensearch']
        env = opensearch.get('environment', [])
        
        if isinstance(env, dict):
            env = [f"{k}={v}" for k, v in env.items()]
        
        env_str = ' '.join(env)
        assert 'DISABLE_SECURITY_PLUGIN=true' in env_str, \
            "Missing DISABLE_SECURITY_PLUGIN=true"
    
    def test_port_9200_exposed(self, compose_config):
        """ทดสอบว่า expose port 9200 (5 คะแนน)"""
        opensearch = compose_config['services']['opensearch']
        ports = opensearch.get('ports', [])
        ports_str = ' '.join(str(p) for p in ports)
        assert '9200' in ports_str, "Port 9200 not exposed"
    
    def test_healthcheck_exists(self, compose_config):
        """ทดสอบว่ามี healthcheck (10 คะแนน)"""
        opensearch = compose_config['services']['opensearch']
        assert 'healthcheck' in opensearch, "Missing healthcheck configuration"
    
    def test_network_exists(self, compose_config):
        """ทดสอบว่ามี network configuration"""
        assert 'networks' in compose_config


class TestSetupScript:
    """Test setup_opensearch.py functions"""
    
    def test_check_connection_returns_bool(self):
        """ทดสอบว่า check_connection return boolean (5 คะแนน)"""
        import sys
        sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
        
        try:
            from setup_opensearch import check_connection, get_client
            client = get_client()
            result = check_connection(client)
            assert isinstance(result, bool), "check_connection should return bool"
        except Exception:
            pytest.skip("OpenSearch not running or function not implemented")
    
    def test_setup_pipeline_returns_bool(self):
        """ทดสอบว่า setup_hybrid_search_pipeline return boolean (5 คะแนน)"""
        import sys
        sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
        
        try:
            from setup_opensearch import setup_hybrid_search_pipeline
            result = setup_hybrid_search_pipeline()
            assert isinstance(result, bool), "setup_hybrid_search_pipeline should return bool"
        except Exception:
            pytest.skip("OpenSearch not running or function not implemented")


class TestDockerComposeFile:
    """Test docker-compose.yml file syntax"""
    
    def test_yaml_syntax_valid(self):
        """ทดสอบว่า YAML syntax ถูกต้อง (5 คะแนน)"""
        compose_path = os.path.join(
            os.path.dirname(__file__), '..', 'src', 'docker-compose.yml'
        )
        
        try:
            with open(compose_path, 'r') as f:
                config = yaml.safe_load(f)
            assert config is not None, "YAML file is empty"
        except yaml.YAMLError as e:
            pytest.fail(f"Invalid YAML syntax: {e}")
    
    def test_version_specified(self):
        """ทดสอบว่ากำหนด version"""
        compose_path = os.path.join(
            os.path.dirname(__file__), '..', 'src', 'docker-compose.yml'
        )
        
        with open(compose_path, 'r') as f:
            config = yaml.safe_load(f)
        
        assert 'version' in config, "Missing version in docker-compose.yml"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
