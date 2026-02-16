from dataclasses import dataclass, field
from typing import List, Dict, Optional
from enum import Enum, auto
import random

class ContentPlatform(Enum):
    TIKTOK = auto()
    INSTAGRAM = auto()
    YOUTUBE_SHORTS = auto()

class ProductCategory(Enum):
    FITNESS_TECH = "Fitness Technology"
    BEAUTY_PRODUCTS = "Beauty & Skincare"
    GAMING_ACCESSORIES = "Gaming Gear"
    SMART_HOME = "Smart Home Devices"
    TRAVEL_TECH = "Travel Technology"

@dataclass
class AffiliateProduct:
    name: str
    category: ProductCategory
    price_range: tuple[float, float]
    commission_rate: float
    key_features: List[str] = field(default_factory=list)

@dataclass
class ContentScript:
    platform: ContentPlatform
    product: AffiliateProduct
    script_text: str
    engagement_potential: float = 0.0

class ContentGenerator:
    def __init__(self, api_key: Optional[str] = None):
        self.products = self._initialize_product_catalog()
        self.api_key = api_key

    def _initialize_product_catalog(self) -> List[AffiliateProduct]:
        return [
            AffiliateProduct(
                name="Smart Fitness Watch",
                category=ProductCategory.FITNESS_TECH,
                price_range=(99.99, 249.99),
                commission_rate=0.15,
                key_features=[
                    "24/7 health tracking",
                    "AI workout recommendations",
                    "Water-resistant design"
                ]
            ),
            # Additional products would be added here
        ]

    def generate_script(
        self, 
        platform: ContentPlatform = ContentPlatform.TIKTOK,
        product: Optional[AffiliateProduct] = None
    ) -> ContentScript:
        """
        Generate a content script for affiliate marketing
        
        :param platform: Target social media platform
        :param product: Optional specific product
        :return: Generated content script
        """
        if not product:
            product = random.choice(self.products)

        hooks = [
            f"🔥 GAME CHANGER ALERT: {product.category.value}",
            f"I can't believe this {product.category.value} exists...",
            f"Watch how this {product.category.value} TRANSFORMED my life!"
        ]

        benefits = [
            f"saves you {random.randint(30, 70)}% time",
            "looks INSANE",
            "works like absolute magic",
            f"only costs ${random.uniform(*product.price_range):.2f}"
        ]

        cta = [
            "Link in bio NOW! 👇",
            "Tap before it's gone! 🚨",
            f"Use code VIRAL{random.randint(10,99)} for {product.commission_rate * 100}% off! 💥"
        ]

        script_template = f"""{random.choice(hooks)}

Features that'll blow your mind:
{' | '.join(product.key_features)}

This {product.category.value} {random.choice(benefits)}. 

{random.choice(cta)}"""

        return ContentScript(
            platform=platform,
            product=product,
            script_text=script_template,
            engagement_potential=random.uniform(0.1, 0.9)
        )

    def generate_campaign(
        self, 
        num_scripts: int = 3, 
        platforms: List[ContentPlatform] = None
    ) -> List[ContentScript]:
        """
        Generate a multi-platform content campaign
        
        :param num_scripts: Number of scripts to generate
        :param platforms: Optional list of platforms
        :return: List of generated content scripts
        """
        if platforms is None:
            platforms = [ContentPlatform.TIKTOK, ContentPlatform.INSTAGRAM]

        campaign = []
        for _ in range(num_scripts):
            platform = random.choice(platforms)
            script = self.generate_script(platform)
            campaign.append(script)

        return campaign