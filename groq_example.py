#!/usr/bin/env python3
"""
Example script showing how to use MathBlackBox with Groq API

Usage Method 1 (Config File - Recommended):
    1. Edit config.json and set:
       {
         "api": {
           "use_groq": true,
           "groq_api_key": "your_groq_api_key_here"
         }
       }
    2. python groq_example.py llama-3.1-8b-instant gsm8k-groq-test

Usage Method 2 (Environment Variables):
    export USE_GROQ=true
    export GROQ_API_KEY=your_groq_api_key_here
    python groq_example.py llama-3.1-8b-instant gsm8k-groq-test
"""

import os
import json

# Check if config.json exists and is properly configured
try:
    with open('config.json', 'r') as f:
        config = json.load(f)
    if config.get('api', {}).get('use_groq') and config.get('api', {}).get('groq_api_key'):
        print("✅ Using Groq API configuration from config.json")
        print(f"Model: {config.get('api', {}).get('groq_model', 'llama-3.1-8b-instant')}")
    else:
        print("⚠️  config.json found but Groq API not properly configured")
        print("Please set 'use_groq': true and 'groq_api_key' in config.json")
        exit(1)
except FileNotFoundError:
    print("📝 config.json not found, checking environment variables...")
    # Fallback to environment variables
    if not os.getenv('GROQ_API_KEY'):
        print("❌ Error: Please either:")
        print("1. Create config.json with Groq API configuration, or")
        print("2. Set GROQ_API_KEY environment variable")
        print("\nExample config.json:")
        print("""{
    "api": {
        "use_groq": true,
        "groq_api_key": "your_groq_api_key_here",
        "groq_model": "llama-3.1-8b-instant"
    }
}""")
        exit(1)
    else:
        print("✅ Using Groq API configuration from environment variables")
        os.environ['USE_GROQ'] = 'true'

# Import the main module
import sys
# Use command line args if provided, otherwise use defaults
if len(sys.argv) >= 2:
    model_name = sys.argv[1]
else:
    model_name = 'llama-3.1-8b-instant'

if len(sys.argv) >= 3:
    data_name = sys.argv[2]
else:
    data_name = 'gsm8k-groq-test'

sys.argv = ['groq_example.py', model_name, data_name]
print(f"🚀 Running with model: {model_name}, dataset: {data_name}")

# Now import and run the main script
import run_with_earlystopping

print("Groq API integration test completed!")
print(f"Model: {run_with_earlystopping.MODEL_NAME}")
print(f"Dataset: {run_with_earlystopping.DATA_NAME}")
print(f"Using Groq: {run_with_earlystopping.USE_GROQ}")
