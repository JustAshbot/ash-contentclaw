import pandas as pd
from typing import List, Dict

class PerformanceTracker:
    def __init__(self):
        self.performance_data = []

    def track_content_performance(self, content_id: str, platform: str, metrics: Dict):
        """
        Track performance metrics for a piece of content
        
        :param content_id: Unique identifier for content
        :param platform: Platform where content was distributed
        :param metrics: Performance metrics dictionary
        """
        performance_entry = {
            'content_id': content_id,
            'platform': platform,
            **metrics
        }
        self.performance_data.append(performance_entry)

    def generate_performance_report(self) -> pd.DataFrame:
        """
        Generate a performance report across all tracked content
        
        :return: Pandas DataFrame with performance metrics
        """
        df = pd.DataFrame(self.performance_data)
        
        # Aggregate performance by platform
        platform_performance = df.groupby('platform').agg({
            'views': 'mean',
            'likes': 'mean',
            'shares': 'mean',
            'conversion_rate': 'mean'
        })

        return platform_performance

    def identify_top_performers(self, metric: str = 'conversion_rate', top_n: int = 5) -> List[Dict]:
        """
        Identify top-performing content pieces
        
        :param metric: Metric to rank by
        :param top_n: Number of top performers to return
        :return: List of top-performing content
        """
        df = pd.DataFrame(self.performance_data)
        return df.nlargest(top_n, metric).to_dict('records')