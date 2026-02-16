import random

class ContentGenerator:
    def __init__(self):
        self.product_categories = [
            'Fitness Tech',
            'Beauty Products',
            'Gaming Accessories',
            'Smart Home Devices'
        ]

    def generate_tiktok_script(self, product_category=None):
        """
        Generate a TikTok-style affiliate marketing script
        
        :param product_category: Optional specific category
        :return: Generated script
        """
        if not product_category:
            product_category = random.choice(self.product_categories)

        hooks = [
            f"🔥 GUYS! Check out this {product_category} hack!",
            f"THIS {product_category} changed EVERYTHING...",
            f"I can't believe this {product_category} is only $X..."
        ]

        benefits = [
            "saves you time",
            "makes life easier",
            "looks INSANE",
            "works like magic"
        ]

        cta = [
            "Link in bio! 👇",
            "Tap now before it's gone! 🚨",
            "Use code VIRAL for 10% off! 💥"
        ]

        script = f"""{random.choice(hooks)}

I found a {product_category} that {random.choice(benefits)}. 

Seriously, this thing {random.choice(benefits)}. 

{random.choice(cta)}"""

        return script

    def generate_multiple_scripts(self, num_scripts=3):
        """
        Generate multiple content scripts
        
        :param num_scripts: Number of scripts to generate
        :return: List of generated scripts
        """
        return [self.generate_tiktok_script() for _ in range(num_scripts)]