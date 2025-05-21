class Logger:
    def __init__(self):
        self.log_level = "INFO"

    def set_level(self, level):
        print(f"[Logger] Setting log level to {level}")
        self.log_level = level

    def get_level(self):
        return self.log_level

# Singleton instance
logger = Logger()