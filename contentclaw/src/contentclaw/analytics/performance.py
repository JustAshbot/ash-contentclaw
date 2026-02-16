import pandas as pd
from typing import Dict, List

class PerformanceTracker:
    def __init__(self):
        self.performance_data = []

    def track_performance(self, content_id: str, platform: str, metrics: Dict[str, float]):
        """
        Track performance metrics for distributed content
        
        :param content_id: Unique content identifier
        :param platform: Distribution platform
        :param metrics: Performance metrics
        """
        entry = {
            'content_id': content_id,
            'platform': platform,
            'timestamp': pd.Timestamp.now(),
            **metrics
        }
        self.performance_data.append(entry)

    def get_top_performers(self, metric: str = 'conversion_rate', top_n: int = 3):
        """
        Identify top-performing content pieces
        
        :param metric: Metric to rank by
        :param top_n: Number of top performers to return
        :return: List of top performers
        """
        df = pd.DataFrame(self.performance_data)
        return df.nlargest(top_n, metric).to_dict('records')

    def generate_platform_report(self):
        """
        Generate performance summary by platform
        
        :return: Performance summary DataFrame
        """
        df = pd.DataFrame(self.performance_data)
        return df.groupby('platform').mean()