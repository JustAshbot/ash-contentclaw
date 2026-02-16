from generators.tiktok import AffiliateProductResearch
from platforms.distribution import ContentDistributor
from analytics.performance import PerformanceTracker

def main():
    # Initialize components
    product_research = AffiliateProductResearch()
    distributor = ContentDistributor(api_keys={})
    performance_tracker = PerformanceTracker()

    # Get top products
    top_products = product_research.get_top_products()

    for product in top_products:
        # Generate content script
        script = product_research.generate_tiktok_script(product)

        # Distribute content
        distribution_results = distributor.distribute(
            {'text': script},
            platforms=['tiktok', 'instagram']
        )

        # Track performance (simulated)
        for platform, result in distribution_results.items():
            performance_tracker.track_performance(
                content_id=result.get('content_id', 'unknown'),
                platform=platform,
                metrics={
                    'views': 1000,
                    'likes': 50,
                    'conversion_rate': 0.05
                }
            )

    # Generate reports
    platform_report = performance_tracker.generate_platform_report()
    top_performers = performance_tracker.get_top_performers()

    print("Platform Performance Report:")
    print(platform_report)
    print("\nTop Performing Content:")
    print(top_performers)

if __name__ == '__main__':
    main()