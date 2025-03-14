# FERGPT Thesis

## Overview
This repository contains the research, code, and documentation for my thesis project, *FERGPT Thesis*. The project focuses on [briefly describe the main focus of your thesis].

## Repository Structure
```
├── docs/                 # Documentation and thesis-related papers
├── processed_data/       # Processed datasets for analysis
│   ├── TestingData/     # Data used for testing models
│   │   ├── HumanTest.py
│   │   ├── cleaned_test_gif_metadata.csv
│   │   ├── gif_metadata_blip.csv
│   │   ├── gif_metadata_categorized.csv
│   │   ├── gif_metadata_sentiment.csv
│   │   ├── gif_sentiment_labels.csv
│   │   ├── gif_sentiment_mapped.csv
│   │   ├── manual_labels.csv
│   │   ├── temp_frame.jpg
│   │   ├── test_gif_metadata.csv
│   │   ├── testingDataSetCreation.ipynb
├── p_crema/              # Preprocessed CREMA dataset
│   ├── .ipynb_checkpoints/
│   ├── 200.gif
│   ├── 200w.gif
│   ├── GIF_Annotations.csv
│   ├── all_files_in_gif_folder.txt
│   ├── debug_log.txt
│   ├── john-amos-james-evans-sr.gif
│   ├── manFromLittlePlasticThings.gif
│   ├── missing_files.txt
│   ├── modelTrainingCrema copy.ipynb
│   ├── modelTrainingCrema.ipynb
│   ├── output.txt
│   ├── processCrema.ipynb
│   ├── rant-black.gif
├── notebooks/            # Jupyter notebooks for data analysis and experimentation
│   ├── FERGPT.ipynb      # Main thesis notebook
│   ├── fineTuning.ipynb  # Model fine-tuning experiments
│   ├── modelEvaluation.ipynb  # Model evaluation process
│   ├── modelTesting.ipynb  # Model testing scripts
├── datasets/             # Datasets used for training and evaluation
├── results/              # Outputs, graphs, and findings from experiments
├── scripts/              # Utility scripts for preprocessing and evaluation
├── gif_model_predictions.csv # Predictions from the trained model
├── requirements.txt      # Dependencies and libraries
├── .gitignore            # Ignored files for version control
├── README.md             # Project overview and setup instructions
```

## Setup Instructions
### Prerequisites
- Python 3.x
- Git
- Recommended: A virtual environment (e.g., `venv` or `conda`)

### Installation
1. Clone the repository:
   ```bash
   git clone [https://github.com/your-username/FerLLMs-Emotional-Transition-Detection-in-GIFs](https://github.com/jecroispatwit/FerLLMs-Emotional-Transition-Detection-in-GIFs).git
   cd FerLLMs-Emotional-Transition-Detection-in-GIFs
   ```
2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
- To run experiments, navigate to the `src/` directory and execute the relevant scripts.
- Jupyter notebooks with analysis can be found in the `notebooks/` folder.
- Documentation and thesis-related materials are in the `docs/` folder.

## Contributing
If you'd like to contribute, feel free to fork the repository and submit a pull request. Please follow best practices and ensure that your code is well-documented.

## License
[Wentworth Institute Of Technology]

## Contact
For questions or discussions, feel free to open an issue or reach out to me at [jecroisp@wit.edu].

