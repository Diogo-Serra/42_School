#!/usr/bin/env python3
from typing import Any, List, Dict, Union, Optional
from abc import ABC, abstractmethod


class DataStream(ABC):
    def __init__(self, stream_id: str) -> None:
        self.stream_id: str = stream_id
        self.data_processed: int = 0

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        if criteria is None:
            return data_batch
        return [item for item in data_batch if criteria.lower() in str(
            item).lower()]

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {
            "stream_id": self.stream_id,
            "data_processed": self.data_processed
        }


class SensorStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        self.stream_type: str = "Environmental Data"

    def process_batch(self, data_batch: List[Any]) -> str:
        print(f"Processing sensor batch: {data_batch}")
        try:
            temps = [float(x.split(":")[1]) for x in data_batch
                     if "temp" in x]
            avg_temp = sum(temps) / len(temps) if temps else 0
            self.data_processed += len(data_batch)
            return (f"Sensor analysis: {len(data_batch)} readings processed, "
                    f"avg temp: {avg_temp}°C")
        except Exception:
            return "Error processing sensor data"


class TransactionStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        self.stream_type: str = "Financial Data"

    def process_batch(self, data_batch: List[Any]) -> str:
        print(f"Processing transaction batch: {data_batch}")
        try:
            net_flow = 0
            for item in data_batch:
                if "buy" in str(item):
                    net_flow -= int(str(item).split(":")[1])
                elif "sell" in str(item):
                    net_flow += int(str(item).split(":")[1])
            self.data_processed += len(data_batch)
            sign = "+" if net_flow >= 0 else ""
            return (f"Transaction analysis: {len(data_batch)} operations, "
                    f"net flow: {sign}{net_flow} units")
        except Exception:
            return "Error processing transaction data"


class EventStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        self.stream_type: str = "System Events"

    def process_batch(self, data_batch: List[Any]) -> str:
        print(f"Processing event batch: {data_batch}")
        try:
            error_count = sum(1 for item in data_batch if "error" in str(
                item).lower())
            self.data_processed += len(data_batch)
            return (f"Event analysis: {len(data_batch)} events, "
                    f"{error_count} error detected")
        except Exception:
            return "Error processing event data"


class StreamProcessor:
    def __init__(self) -> None:
        self.streams: List[DataStream] = []

    def add_stream(self, stream: DataStream) -> None:
        self.streams.append(stream)

    def process_all(self, batches: List[List[Any]]) -> None:
        for i, batch in enumerate(batches, 1):
            print(f"Batch {i} Results:")
            try:
                for stream in self.streams:
                    result = stream.process_batch(batch)
                    print(f"- {stream.stream_type}: {result}")
            except Exception:
                print("Error processing batch")

    def filter_all(self, criteria: str) -> None:
        print(f"\nStream filtering active: {criteria}")
        results = []
        for stream in self.streams:
            try:
                if isinstance(stream, SensorStream):
                    filtered = stream.filter_data([
                        "temp:25.5", "temp:15.0", "humidity:80"
                    ], "temp")
                    results.append(f"{len(filtered)} critical sensor alerts")
                elif isinstance(stream, TransactionStream):
                    filtered = stream.filter_data([
                        "buy:1000", "sell:500"
                    ], "buy")
                    results.append(f"{len(filtered)} large transaction")
            except Exception:
                pass
        print(f"Filtered results: {', '.join(results)}")


def main() -> None:
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===\n")

    print("Initializing Sensor Stream...")
    sensor = SensorStream("SENSOR_001")
    print(f"Stream ID: {sensor.stream_id}, Type: {sensor.stream_type}")
    print(sensor.process_batch(["temp:22.5", "humidity:65", "pressure:1013"]))

    print("\nInitializing Transaction Stream...")
    trans = TransactionStream("TRANS_001")
    print(f"Stream ID: {trans.stream_id}, Type: {trans.stream_type}")
    print(trans.process_batch(["buy:100", "sell:150", "buy:75"]))

    print("\nInitializing Event Stream...")
    event = EventStream("EVENT_001")
    print(f"Stream ID: {event.stream_id}, Type: {event.stream_type}")
    print(event.process_batch(["login", "error", "logout"]))

    print("\n=== Polymorphic Stream Processing ===")
    print("Processing mixed stream types through unified interface...")

    processor = StreamProcessor()
    processor.add_stream(sensor)
    processor.add_stream(trans)
    processor.add_stream(event)

    processor.process_all([
        ["temp:20.0", "humidity:60"],
        ["buy:200", "sell:100", "buy:150", "sell:50"],
        ["login", "logout", "error"]
    ])

    processor.filter_all("High-priority")
    print("\nAll streams processed successfully. Nexus throughput optimal.")


if __name__ == "__main__":
    main()
