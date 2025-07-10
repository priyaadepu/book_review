# app/core/cache.py
import redis
from app.core.config import settings

redis_client = redis.Redis.from_url(settings.redis_url, decode_responses=True)
