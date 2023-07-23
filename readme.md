# Huggingface model LoRA finetuning for text summarisation

### Instructions

1. Clone this repository on a capable server or instance.

2. create a ".env" file and add your OPENAI_API_KEY

3. If "data/doc_summary_pair.json" is unavailable, run the "doc_summery_generator.ipynb" notebook.

4. Run the "finetuning_xxx.ipynb" notebooks to finetune  the LLMs

5. Run the "benchmark.ipynb" notebook to compare the finetuned flan-T5-small model to the alpaca and vicuna models