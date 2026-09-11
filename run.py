#!/usr/bin/env python3
"""Amadeus AI - 简化启动脚本（仅需依赖）"""

import sys
import os

# 添加项目路径
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

print("="*60)
print("🎮 Amadeus AI - 启动脚本")
print("="*60)

# 检查依赖
print("\n检查依赖...")
dependencies = [
    ('fastapi', 'FastAPI'),
    ('uvicorn', 'Uvicorn'),
    ('pydantic', 'Pydantic'),
    ('dotenv', 'python-dotenv'),
    ('loguru', 'Loguru'),
]

missing = []
for module, name in dependencies:
    try:
        __import__(module)
        print(f"✓ {name}")
    except ImportError:
        print(f"✗ {name} 未安装")
        missing.append(name)

if missing:
    print(f"\n缺少依赖: {', '.join(missing)}")
    print("请运行: pip install -r requirements_core.txt")
    sys.exit(1)

print("\n✓ 所有依赖已安装\n")

# 导入配置和日志
from utils.logger import logger
from utils.config import config

print("="*60)
print("启动 Amadeus AI 服务器")
print("="*60)

api_url = f"http://{config.API_HOST}:{config.API_PORT}"

print(f"\n📍 服务器地址: {api_url}")
print(f"📖 API 文档: {api_url}/docs")
print(f"🏥 健康检查: {api_url}/health")
print(f"💻 Web UI: {api_url}/")
print(f"\n⏳ 服务器正在启动... 按 Ctrl+C 停止\n")

try:
    from api.app import app
    import uvicorn
    
    # 启动服务器
    uvicorn.run(
        app,
        host=config.API_HOST,
        port=config.API_PORT,
        debug=config.API_DEBUG,
        workers=1,
        log_level="info"
    )

except KeyboardInterrupt:
    print("\n\n✓ 服务器已停止 (Ctrl+C)")
    sys.exit(0)
except Exception as e:
    logger.error(f"服务器错误: {str(e)}")
    import traceback
    traceback.print_exc()
    sys.exit(1)
