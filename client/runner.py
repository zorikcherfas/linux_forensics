from client.collectors.collector import Collector
import logging

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    logging.info("A Debug Logging Message")

    collector = Collector()
    collector.register_volatile_data()
    collector.register_files_data()
    collector.run_collectors()