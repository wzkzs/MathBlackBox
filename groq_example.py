#!/usr/bin/env python3
"""
Example script showing how to use MathBlackBox with Groq API

Usage:
    export USE_GROQ=true
    export GROQ_API_KEY=your_groq_api_key_here
    python groq_example.py llama-3.1-8b-instant gsm8k-groq-test
"""

import os

# Set environment variables for Groq API
os.environ['USE_GROQ'] = 'true'
# os.environ['GROQ_API_KEY'] = 'your_groq_api_key_here'  # Set this in your shell

if not os.getenv('GROQ_API_KEY'):
    print("Error: Please set GROQ_API_KEY environment variable")
    print("Example: export GROQ_API_KEY=your_groq_api_key_here")
    exit(1)

# Import the main module
import sys
sys.argv = ['groq_example.py', 'llama-3.1-8b-instant', 'gsm8k-groq-test']

# Now import and run the main script
import run_with_earlystopping

print("Groq API integration test completed!")
print(f"Model: {run_with_earlystopping.MODEL_NAME}")
print(f"Dataset: {run_with_earlystopping.DATA_NAME}")
print(f"Using Groq: {run_with_earlystopping.USE_GROQ}")
