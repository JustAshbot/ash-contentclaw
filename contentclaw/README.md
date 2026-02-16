# ContentClaw 🦾

## AI-Powered Content Generation Toolkit

### Features
- 🎥 TikTok Shop Affiliate Content Generation
- 🌐 Multi-Platform Distribution
- 📊 Performance Tracking

### Quick Start

```bash
pip install contentclaw
```

### Usage

```python
from contentclaw.generators.tiktok import TikTokContentGenerator
from contentclaw.platforms.distribution import ContentDistributor

# Generate affiliate content
generator = TikTokContentGenerator(api_key='your_key')
content = generator.generate_affiliate_script(product)

# Distribute across platforms
distributor = ContentDistributor()
distributor.distribute(content, platforms=['tiktok', 'instagram'])
```

### Development

```bash
git clone https://github.com/JustAshbot/ash-contentclaw.git
cd contentclaw
pip install -e .
```