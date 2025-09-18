"""
Configuration management for microservices
Handles environment variables and service discovery
"""
import os
from typing import Optional

class ServiceConfig:
    """Service configuration management"""
    
    # Django Backend Service
    DJANGO_HOST = os.getenv("DJANGO_SERVICE_HOST", "localhost")
    DJANGO_PORT = os.getenv("DJANGO_SERVICE_PORT", "8002")
    DJANGO_URL = f"http://{DJANGO_HOST}:{DJANGO_PORT}"
    
    # FastAPI Integration Service
    FASTAPI_HOST = os.getenv("FASTAPI_SERVICE_HOST", "localhost") 
    FASTAPI_PORT = os.getenv("FASTAPI_SERVICE_PORT", "8000")
    FASTAPI_URL = f"http://{FASTAPI_HOST}:{FASTAPI_PORT}"
    
    # React Frontend Service
    REACT_HOST = os.getenv("REACT_SERVICE_HOST", "localhost")
    REACT_PORT = os.getenv("REACT_SERVICE_PORT", "3000") 
    REACT_URL = f"http://{REACT_HOST}:{REACT_PORT}"
    
    # CORS Origins (dynamic)
    @classmethod
    def get_cors_origins(cls) -> list[str]:
        """Get CORS origins dynamically"""
        default_origins = [
            cls.REACT_URL,
            f"http://127.0.0.1:{cls.REACT_PORT}"
        ]
        
        # Add custom origins from environment
        custom_origins = os.getenv("CORS_ORIGINS", "").split(",")
        return default_origins + [origin.strip() for origin in custom_origins if origin.strip()]
    
    # Service Discovery (for future use)
    SERVICE_REGISTRY_URL = os.getenv("SERVICE_REGISTRY_URL", "http://localhost:8500")
    
    @classmethod
    def get_service_url(cls, service_name: str) -> Optional[str]:
        """
        Get service URL by name - supports service discovery in future
        Currently returns hard-coded URLs, but can be extended for:
        - Consul service discovery
        - Kubernetes service discovery  
        - Docker service discovery
        """
        service_map = {
            "django": cls.DJANGO_URL,
            "fastapi": cls.FASTAPI_URL,
            "react": cls.REACT_URL,
        }
        return service_map.get(service_name.lower())
    
    @classmethod
    def discover_service(cls, service_name: str) -> Optional[str]:
        """
        Discover service URL dynamically (future implementation)
        Could integrate with:
        - Consul: consul.py library
        - etcd: etcd3 library  
        - Kubernetes: kubernetes library
        """
        # For now, return static URLs
        return cls.get_service_url(service_name)
        
        # Future implementation example:
        # import consul
        # c = consul.Consul()
        # service = c.health.service(service_name, passing=True)[1]
        # if service:
        #     return f"http://{service[0]['Service']['Address']}:{service[0]['Service']['Port']}"
        # return None