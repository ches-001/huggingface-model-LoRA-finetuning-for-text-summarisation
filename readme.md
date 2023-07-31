# Huggingface model LoRA finetuning for text summarisation

### Instructions

1. Clone this repository on a capable server or instance.

2. create a ".env" file and add your OPENAI_API_KEY

3. If "data/doc_summary_pair.json" is unavailable, run the "doc_summery_generator.ipynb" notebook.

4. Run the "finetuning_xxx.ipynb" notebooks to finetune  the LLMs

5. Run the "lora_xxx_comparison.ipynb" notebooks to compare the LoRA finetuned LLMs to their base forms models and others. 
**Alteratively**, you can download the necessary folders required to run the comparison notebooks from [Here](https://drive.google.com/file/d/1qMwLSuHDNqise0IDAUAaqMctRiUapg0Q/view?usp=drive_link). There are 6 folders in this zipped file, and all 6 are expected to be on the same directory level as the comparison notebooks.