# Amadeus AI - PyTorch 版本

> 一个基于《命运石之门 0》灵感的 AI 对话系统，拥有红莉栖（Kurisu Makise）的人格思维和形象。

**EL PSY CONGROO~** 🚀

## 🌟 核心功能

- 🧠 **红莉栖人格 AI** - 模拟红莉栖的思维方式和对话风格
- 🎭 **Live2D 动态形象** - 游戏中的实时动画表现
- 🎤 **语音合成** - 游戏原声音色的语音合成
- 💬 **多轮对话** - 支持上下文记忆和连贯对话
- 📱 **移动端支持** - 轻量化模型可在手机上运行
- 🌐 **Web 和 API** - 完整的服务接口

## 📋 项目结构

```
amadeus-ai-pytorch/
├── models/                    # PyTorch 模型相关
│   ├── kurisu_model.py       # 红莉栖 AI 模型定义
│   ├── dialogue_generator.py # 对话生成引擎
│   ├── personality.py        # 人格系统和提示词
│   └── pretrained/           # 预训练模型权重目录
│
├── live2d/                    # Live2D 形象和渲染
│   ├── live2d_renderer.py    # Live2D 渲染引擎
│   ├── animation_manager.py  # 动作和表情管理
│   ├── models/               # Live2D 模型文件（从游戏解包）
│   │   ├── kurisu/
│   │   │   ├── model.json
│   │   │   ├── model.moc3
│   │   │   ├── textures/
│   │   │   └── animations/
│   │   └── ...
│   └── voice_sync.py         # 语音同步动画
│
├── tts/                       # 文字转语音
│   ├── voice_synthesizer.py  # 语音合成器
│   ├── audio_processor.py    # 音频处理
│   └── voices/               # 语音音色库（从游戏解包）
│       ├── kurisu/
│       │   ├── voice_model.pth
│       │   └── audio_samples/
│       └── ...
│
├── inference/                 # 推理和服务
│   ├── dialog_engine.py      # 对话引擎
│   ├── context_manager.py    # 对话上下文管理
│   ├── memory_system.py      # 记忆系统（MEM0）
│   └── conversation.py       # 对话流程
│
├── api/                       # API 服务
│   ├── app.py                # FastAPI 主应用
│   ├── routes.py             # API 路由
│   ├── websocket_handler.py  # WebSocket 实时通信
│   └── schemas.py            # 数据模型
│
├── mobile/                    # 移动端适配
│   ├── model_quantization.py # 模型量化（轻量化）
│   ├── mobile_inference.py   # 移动端推理优化
│   └── flutter_integration/  # Flutter 集成示例
│
├── utils/                     # 工具函数
│   ├── logger.py             # 日志系统
│   ├── config.py             # 配置管理
│   └── data_processor.py     # 数据处理
│
├── data/                      # 数据和训练资源
│   ├── personality_data/     # 人格训练数据
│   ├── conversation_data/    # 对话样本
│   └── game_scripts/         # 游戏脚本（可选）
│
├── tests/                     # 单元测试
├── requirements.txt           # Python 依赖
├── .env.example              # 环境变量示例
├── setup.py                  # 项目安装脚本
├── config.yaml               # 配置文件
└── main.py                   # 主程序入口
```

## 🚀 快速开始

### 环境要求

- Python ≥ 3.8
- PyTorch ≥ 2.0
- CUDA 11.8+（可选，用于 GPU 加速）
- Node.js 18+（Web 前端）

### 1. 安装依赖

```bash
# 克隆项目
git clone https://github.com/xinran0502/amadeus-ai-pytorch.git
cd amadeus-ai-pytorch

# 创建虚拟环境
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 安装依赖
pip install -r requirements.txt
```

### 2. 配置环境

```bash
# 复制环境变量文件
cp .env.example .env

# 编辑 .env 文件，填入必要的配置
# 如：OpenAI API Key、数据库连接等
```

### 3. 准备游戏资源

**从《命运石之门 0》游戏中解包以下资源：**

```
# Live2D 模型（红莉栖）
复制到: live2d/models/kurisu/
- model.json
- model.moc3
- textures/
- animations/

# 语音音色数据
复制到: tts/voices/kurisu/
- voice_model.pth （或相关模型文件）
- audio_samples/ （音频样本）
```

> 📝 解包教程：
> - 可使用 `UnityEX`、`AssetStudio` 等工具解包游戏资源
> - 将 Live2D 模型转换为标准格式
> - 提取游戏中的语音文件

### 4. 启动服务

```bash
# 方式 1：直接运行
python main.py

# 方式 2：使用 FastAPI 服务
uvicorn api.app:app --reload

# 方式 3：使用 Docker
docker-compose up -d
```

### 5. 访问应用

- **Web 界面**：http://localhost:8000
- **API 文档**：http://localhost:8000/docs
- **WebSocket**：ws://localhost:8000/ws

## 💬 使用示例

### Python API

```python
from inference.dialog_engine import DialogEngine
from live2d.live2d_renderer import Live2DRenderer
from tts.voice_synthesizer import VoiceSynthesizer

# 初始化引擎
dialog_engine = DialogEngine()
renderer = Live2DRenderer("kurisu")
synthesizer = VoiceSynthesizer("kurisu")

# 进行对话
user_input = "你好，红莉栖！"
response = dialog_engine.generate_response(user_input)

# 生成语音
audio_data = synthesizer.synthesize(response)

# 获取对应的动作
animation = renderer.get_animation_for_text(response)

# 同步语音和动画
synchronized_output = renderer.sync_voice_with_animation(audio_data, animation)
```

### REST API

```bash
# 发送对话请求
curl -X POST http://localhost:8000/api/chat \
  -H "Content-Type: application/json" \
  -d '{
    "message": "你好，红莉栖！",
    "user_id": "user123"
  }'

# 响应示例
{
  "response": "哼，找我有什么事吗？",
  "audio_url": "/audio/response_12345.wav",
  "animation": "talk_normal",
  "emotion": "normal"
}
```

### WebSocket 实时通信

```javascript
const ws = new WebSocket('ws://localhost:8000/ws');

ws.onopen = () => {
  ws.send(JSON.stringify({
    type: 'message',
    content: '你在研究什么？'
  }));
};

ws.onmessage = (event) => {
  const data = JSON.parse(event.data);
  console.log('红莉栖回复:', data.response);
  console.log('动作:', data.animation);
};
```

## 🎨 AI 人格系统

红莉栖的性格特点：
- 🧪 **科学家气质** - 逻辑严谨，喜欢讨论科学问题
- 😠 **傲娇** - 表面严肃，实际关心他人
- 🎯 **认真** - 对研究和朋友的事情非常认真
- 💭 **好奇心强** - 对新事物充满兴趣
- 🚀 **行动派** - 说做就做，不怕困难

系统会根据对话上下文动态调整响应风格。

## 🗣️ 语音和动画同步

系统会：
1. 生成对话文本
2. 合成相应的语音（使用游戏音色）
3. 分析文本情感和内容
4. 选择对应的 Live2D 动作和表情
5. 实时同步语音和动画播放

## 📱 移动端部署

### 轻量化模型

```python
from mobile.model_quantization import quantize_model

# 量化模型以减小体积
quantized_model = quantize_model("models/pretrained/kurisu_model.pth")

# 移动端推理
result = quantized_model.inference(user_input)
```

### Flutter 应用示例

详见 `mobile/flutter_integration/` 目录

## 🔧 配置说明

### config.yaml

```yaml
# 模型配置
model:
  name: "kurisu_model"
  type: "pytorch"
  device: "cuda"  # 或 "cpu"
  
# Live2D 配置
live2d:
  model_path: "live2d/models/kurisu"
  animation_speed: 1.0
  
# TTS 配置
tts:
  engine: "kurisu_voice"
  sample_rate: 22050
  voice_style: "normal"
  
# API 配置
api:
  host: "0.0.0.0"
  port: 8000
  debug: false
  
# 对话配置
dialog:
  max_context_length: 10
  temperature: 0.7
  top_p: 0.9
```

## 📚 学习资源

- [PyTorch 官方文档](https://pytorch.org/)
- [Live2D Cubism SDK](https://www.live2d.com/)
- [FastAPI 文档](https://fastapi.tiangolo.com/)
- [命运石之门维基](https://steinsgate.fandom.com/)

## 🤝 贡献指南

欢迎提交 Issue 和 Pull Request！

## 📝 许可证

MIT License - 见 LICENSE 文件

## 🙏 致谢

- 灵感来自《命运石之门 0》
- 感谢所有开源项目贡献者
- 感谢红莉栖的官方设定支持

---

**"The universe has a beginning, but no end."**

*— Steins;Gate 0*
