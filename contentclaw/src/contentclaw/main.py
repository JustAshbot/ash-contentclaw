from generators.tiktok import TikTokContentGenerator
from platforms.distribution import ContentDistributor
from analytics.performance import PerformanceTracker

def main():
    # Initialize components
    content_generator = TikTokContentGenerator(api_key='your_openai_key')
    distributor = ContentDistributor()
    performance_tracker = PerformanceTracker()

    # Research trending products
    trending_products = content_generator.find_trending_products('fitness')

    # Generate content for each product
    for product in trending_products:
        # Generate content script
        content_script = content_generator.generate_affiliate_script(product)

        # Distribute content
        distribution_results = distributor.distribute(
            {
                'title': f"Affiliate: {product['name']}",
                'content': content_script
            },
            platforms=['tiktok', 'instagram']
        )

        # Track performance (simulated)
        for platform, result in distribution_results.items():
            performance_tracker.track_content_performance(
                content_id=product['name'],
                platform=platform,
                metrics={
                    'views': 1000,
                    'likes': 50,
                    'shares': 10,
                    'conversion_rate': 0.05
                }
            )

    # Generate performance report
    performance_report = performance_tracker.generate_performance_report()
    print("Performance Report:")
    print(performance_report)

    # Identify top performers
    top_performers = performance_tracker.identify_top_performers()
    print("\nTop Performers:")
    print(top_performers)

if __name__ == '__main__':
    main()