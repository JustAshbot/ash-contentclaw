from core.content_strategy import ContentGenerator, ContentPlatform

def main():
    generator = ContentGenerator()
    
    # Generate a multi-platform campaign
    campaign = generator.generate_campaign(num_scripts=3)
    
    print("🚀 ContentClaw Campaign Generator 🚀")
    print("-" * 50)
    
    for index, script in enumerate(campaign, 1):
        print(f"Script #{index} ({script.platform.name}):")
        print(script.script_text)
        print(f"Engagement Potential: {script.engagement_potential * 100:.2f}%")
        print("-" * 50)

if __name__ == "__main__":
    main()