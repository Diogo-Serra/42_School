# Call-Me-Maybe

This project is present here: https://github.com/Diogo-Serra/Call_Me_Maybe

---

## Description

Call Me Maybe is a function calling project that translates natural language prompts into structured, machine-executable function calls. Given a set of available function definitions and a set of natural language prompts, the goal is to identify the correct function to call and extract its arguments with the correct types, producing valid JSON output for every single prompt.

The program uses a small local LLM (Qwen/Qwen3-0.6B) through a provided SDK, and relies on constrained decoding - a token-by-token generation technique that restricts the model's next-token choices to only those that keep the output both syntactically valid JSON and compliant with the expected function schema - to guarantee 100% valid, parseable output even from an unreliable, low-parameter model.

