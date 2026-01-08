"""
Test cases for Docker Compose
=============================
ใช้สำหรับ auto-grading Week 08

คะแนน: 90 คะแนน (+ 10 screenshots)
"""

import pytest
import os
import yaml


# Paths
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
API_DOCKERFILE = os.path.join(BASE_DIR, 'api', 'Dockerfile')
FRONTEND_DOCKERFILE = os.path.join(BASE_DIR, 'frontend', 'Dockerfile')
COMPOSE_FILE = os.path.join(BASE_DIR, 'docker-compose.yml')


def load_compose():
    """Load docker-compose.yml"""
    with open(COMPOSE_FILE, 'r') as f:
        return yaml.safe_load(f)


class TestAPIDockerfile:
    """Test api/Dockerfile (25 คะแนน)"""
    
    def test_file_exists(self):
        """ทดสอบว่า Dockerfile มีอยู่"""
        assert os.path.exists(API_DOCKERFILE), "api/Dockerfile not found"
    
    def test_has_from(self):
        """ทดสอบว่ามี FROM instruction (TODO 1)"""
        with open(API_DOCKERFILE, 'r') as f:
            content = f.read()
        
        assert 'FROM python' in content or 'FROM python:' in content.replace(' ', ''), \
            "Should have FROM python instruction"
    
    def test_has_copy_requirements(self):
        """ทดสอบว่ามี COPY requirements (TODO 2)"""
        with open(API_DOCKERFILE, 'r') as f:
            content = f.read()
        
        assert 'COPY' in content and 'requirements' in content, \
            "Should COPY requirements.txt"
    
    def test_has_pip_install(self):
        """ทดสอบว่ามี pip install (TODO 2)"""
        with open(API_DOCKERFILE, 'r') as f:
            content = f.read()
        
        assert 'pip install' in content, "Should have pip install"
    
    def test_has_copy_source(self):
        """ทดสอบว่ามี COPY source (TODO 3)"""
        with open(API_DOCKERFILE, 'r') as f:
            content = f.read()
        
        # Should have at least 2 COPY statements
        copy_count = content.count('COPY')
        assert copy_count >= 2, "Should have COPY for requirements and source"
    
    def test_has_cmd_uvicorn(self):
        """ทดสอบว่ามี CMD uvicorn (TODO 4)"""
        with open(API_DOCKERFILE, 'r') as f:
            content = f.read()
        
        assert 'CMD' in content and 'uvicorn' in content, \
            "Should have CMD with uvicorn"
    
    def test_not_todo(self):
        """ทดสอบว่าไม่มี TODO เหลือ"""
        with open(API_DOCKERFILE, 'r') as f:
            content = f.read()
        
        # ตรวจเฉพาะ FROM และ CMD lines
        lines = content.split('\n')
        for line in lines:
            if line.strip().startswith('FROM') or line.strip().startswith('CMD'):
                assert 'TODO' not in line, f"TODO not replaced: {line}"


class TestFrontendDockerfile:
    """Test frontend/Dockerfile (25 คะแนน)"""
    
    def test_file_exists(self):
        """ทดสอบว่า Dockerfile มีอยู่"""
        assert os.path.exists(FRONTEND_DOCKERFILE), "frontend/Dockerfile not found"
    
    def test_has_from(self):
        """ทดสอบว่ามี FROM instruction (TODO 1)"""
        with open(FRONTEND_DOCKERFILE, 'r') as f:
            content = f.read()
        
        assert 'FROM python' in content or 'FROM python:' in content.replace(' ', ''), \
            "Should have FROM python instruction"
    
    def test_has_copy_requirements(self):
        """ทดสอบว่ามี COPY requirements (TODO 2)"""
        with open(FRONTEND_DOCKERFILE, 'r') as f:
            content = f.read()
        
        assert 'COPY' in content and 'requirements' in content, \
            "Should COPY requirements.txt"
    
    def test_has_pip_install(self):
        """ทดสอบว่ามี pip install (TODO 2)"""
        with open(FRONTEND_DOCKERFILE, 'r') as f:
            content = f.read()
        
        assert 'pip install' in content, "Should have pip install"
    
    def test_has_cmd_streamlit(self):
        """ทดสอบว่ามี CMD streamlit (TODO 4)"""
        with open(FRONTEND_DOCKERFILE, 'r') as f:
            content = f.read()
        
        assert 'CMD' in content and 'streamlit' in content, \
            "Should have CMD with streamlit"
    
    def test_not_todo(self):
        """ทดสอบว่าไม่มี TODO เหลือ"""
        with open(FRONTEND_DOCKERFILE, 'r') as f:
            content = f.read()
        
        lines = content.split('\n')
        for line in lines:
            if line.strip().startswith('FROM') or line.strip().startswith('CMD'):
                assert 'TODO' not in line, f"TODO not replaced: {line}"


class TestDockerCompose:
    """Test docker-compose.yml (40 คะแนน)"""
    
    def test_file_exists(self):
        """ทดสอบว่า docker-compose.yml มีอยู่"""
        assert os.path.exists(COMPOSE_FILE), "docker-compose.yml not found"
    
    def test_valid_yaml(self):
        """ทดสอบว่า YAML valid"""
        try:
            compose = load_compose()
            assert compose is not None
        except yaml.YAMLError as e:
            pytest.fail(f"Invalid YAML: {e}")
    
    def test_has_services(self):
        """ทดสอบว่ามี services"""
        compose = load_compose()
        assert 'services' in compose, "Should have services"


class TestAPIService:
    """Test API service (TODO 1)"""
    
    def test_api_service_exists(self):
        """ทดสอบว่ามี api service"""
        compose = load_compose()
        assert 'api' in compose.get('services', {}), "Should have api service"
    
    def test_api_has_build(self):
        """ทดสอบว่า api มี build"""
        compose = load_compose()
        api = compose['services'].get('api', {})
        
        assert 'build' in api or 'image' in api, "API should have build or image"
        if 'build' in api:
            assert 'api' in str(api['build']), "Should build from ./api"
    
    def test_api_has_ports(self):
        """ทดสอบว่า api มี ports"""
        compose = load_compose()
        api = compose['services'].get('api', {})
        
        ports = api.get('ports', [])
        has_9000 = any('9000' in str(p) for p in ports)
        assert has_9000, "API should expose port 9000"


class TestFrontendService:
    """Test Frontend service (TODO 2)"""
    
    def test_frontend_service_exists(self):
        """ทดสอบว่ามี frontend service"""
        compose = load_compose()
        assert 'frontend' in compose.get('services', {}), "Should have frontend service"
    
    def test_frontend_has_build(self):
        """ทดสอบว่า frontend มี build"""
        compose = load_compose()
        frontend = compose['services'].get('frontend', {})
        
        assert 'build' in frontend or 'image' in frontend, "Frontend should have build or image"
    
    def test_frontend_has_ports(self):
        """ทดสอบว่า frontend มี ports"""
        compose = load_compose()
        frontend = compose['services'].get('frontend', {})
        
        ports = frontend.get('ports', [])
        has_8501 = any('8501' in str(p) for p in ports)
        assert has_8501, "Frontend should expose port 8501"


class TestOpenSearchService:
    """Test OpenSearch service (TODO 3)"""
    
    def test_opensearch_service_exists(self):
        """ทดสอบว่ามี opensearch service"""
        compose = load_compose()
        assert 'opensearch' in compose.get('services', {}), "Should have opensearch service"
    
    def test_opensearch_has_image(self):
        """ทดสอบว่า opensearch มี image"""
        compose = load_compose()
        opensearch = compose['services'].get('opensearch', {})
        
        image = opensearch.get('image', '')
        assert 'opensearch' in image.lower(), "Should use opensearch image"
    
    def test_opensearch_has_ports(self):
        """ทดสอบว่า opensearch มี ports"""
        compose = load_compose()
        opensearch = compose['services'].get('opensearch', {})
        
        ports = opensearch.get('ports', [])
        has_9200 = any('9200' in str(p) for p in ports)
        assert has_9200, "OpenSearch should expose port 9200"


class TestNetworksAndVolumes:
    """Test Networks and Volumes (TODO 4)"""
    
    def test_has_networks(self):
        """ทดสอบว่ามี networks"""
        compose = load_compose()
        assert 'networks' in compose, "Should have networks section"
    
    def test_has_volumes(self):
        """ทดสอบว่ามี volumes"""
        compose = load_compose()
        assert 'volumes' in compose, "Should have volumes section"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
