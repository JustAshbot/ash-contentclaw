import openai
from typing import List, Dict

class TikTokContentGenerator:
    def __init__(self, api_key: str):
        openai.api_key = api_key
        self.models = {
            'script': 'openrouter/anthropic/claude-3.5-haiku',
            'research': 'openrouter/google/gemini-2.0-flash-thinking-exp:free'
        }

    def generate_affiliate_script(self, product: Dict, platform: str = 'tiktok') -> str:
        """
        Generate a short-form content script for affiliate marketing
        
        :param product: Product details dictionary
        :param platform: Target social media platform
        :return: Generated content script
        """
        prompt = f"""Generate a compelling {platform} script for an affiliate marketing video.

        Product Details:
        - Name: {product.get('name', 'Product')}
        - Price: {product.get('price', 'N/A')}
        - Key Features: {product.get('features', 'None specified')}

        Script Requirements:
        - 30-60 seconds long
        - Engaging hook
        - Clear value proposition
        - Call-to-action with affiliate link
        """

        response = openai.ChatCompletion.create(
            model=self.models['script'],
            messages=[
                {"role": "system", "content": "You are an expert short-form content creator specializing in affiliate marketing."},
                {"role": "user", "content": prompt}
            ]
        )

        return response.choices[0].message.content

    def find_trending_products(self, category: str) -> List[Dict]:
        """
        Research trending affiliate products in a given category
        
        :param category: Product category to research
        :return: List of trending products
        """
        # Placeholder for actual API integration
        research_prompt = f"Find top 5 trending affiliate products in {category} with high conversion potential"

        response = openai.ChatCompletion.create(
            model=self.models['research'],
            messages=[
                {"role": "system", "content": "You are an expert affiliate marketing researcher."},
                {"role": "user", "content": research_prompt}
            ]
        )

        # Parse and return product list
        return [
            {
                'name': product.strip(),
                'category': category,
                'potential_commission': 'High'
            } for product in response.choices[0].message.content.split('\n') if product.strip()
        ]