#!/usr/bin/env python3
from typing import Any
from abc import ABC, abstractmethod


class DataProcessor(ABC):
    def __init__(self) -> None:
        pass

    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        return result


class NumericProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()

    def validate(self, data: Any) -> bool:
        try:
            return all(isinstance(x, (int, float)) for x in data)
        except Exception:
            return False

    def process(self, data: Any) -> str:
        print(f"Processing data: {data}")
        if not self.validate(data):
            try:
                data = [float(x) for x in data]
            except Exception:
                return "Invalid numeric data"
        print("Validation: Numeric data verified")
        total = sum(data)
        avg = total / len(data)
        msg = f"Processed {len(data)} numeric values, sum={total}, avg={avg}"
        return self.format_output(f"Output: {msg}")


class TextProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()

    def validate(self, data: Any) -> bool:
        return isinstance(data, str)

    def process(self, data: Any) -> str:
        print(f"Processing data: \"{data}\"")
        if not self.validate(data):
            return "Invalid text data"
        print("Validation: Text data verified")
        char_count = len(data)
        word_count = len(data.split())
        result = f"Processed text: {char_count} characters, {word_count} words"
        return self.format_output(f"Output: {result}")


class LogProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()

    def validate(self, data: Any) -> bool:
        levels = ["ERROR", "WARNING", "INFO"]
        return isinstance(data, str) and any(
            level in data.upper() for level in levels)

    def process(self, data: Any) -> str:
        print(f"Processing data: \"{data}\"")
        if not self.validate(data):
            return "Invalid log entry"
        print("Validation: Log entry verified")
        level = "ALERT" if "ERROR" in data.upper() else "INFO"
        result = f"[{level}] {data}"
        return self.format_output(f"Output: {result}")


"""
def main():
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===")

    print("Initializing Numeric Processor...")
    numeric = NumericProcessor()
    print(numeric.process([1, 2, 3, 4, 5]))

    print("\nInitializing Text Processor...")
    text = TextProcessor()
    print(text.process("Hello Nexus World"))

    print("\nInitializing Log Processor...")
    log = LogProcessor()
    print(log.process("ERROR: Connection timeout"))

    print("\n=== Polymorphic Processing Demo ===")


main()
"""
