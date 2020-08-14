from client.collectors.collector import Collector, CollectorVolatileData
import logging

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    logging.info("A Debug Logging Message")

    collector = Collector()
    collector.register_volatile_data()
    collector.run_collectors()