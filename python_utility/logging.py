from logging import basicConfig, INFO


class Logging:
    @staticmethod
    def enable():
        basicConfig(
            level=INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
