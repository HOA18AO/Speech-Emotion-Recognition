# Speech Emotion Recognition
# DS313.O21 - UIT

This is a course's project in UIT.

This repository contains the source code and datasets used for Speech Emotion Recognition (SER) using various machine learning models. Follow the instructions below to set up and run the project.

## Dataset Preparation

If there is no folder named `TESS` or `RAVDESS`, please download the 'TESS' and 'RAVDESS' datasets and place them in the `datasets` folder within the `source code` directory. The download links for these datasets are attached in the report file.

I have update a new directory `data/` storing those two datasets (which I used for the project)

## Source Code Structure

- All code files or folders in the source code directory that start with `_` are valuable.
- The file named `_functions.py` contains all the functions written by the author that are considered helpful.
- Code files ending with `.ipynb` are processing files and model running files. Be careful when running them to avoid messing up the dataset.

## Running the Project

1. **Merge Datasets:**
   - Run the `_remake.ipynb` code file to merge the two big datasets into one.

2. **Generate MFCC Features:**
   - Run the `_preprocessing.ipynb` code file to generate MFCC features datasets.

3. **View Results:**
   - Run any model file (ending with `.ipynb`) to view the results.

4. **Optional Demo:**
   - Run the `demo.ipynb` file to see the model recognize speech emotion.

## Why Not BERT?

I did not use BERT (Bidirectional Encoder Representations from Transformers) for this task because BERT is primarily designed for natural language processing (NLP) tasks involving text data, such as sentiment analysis, question answering, and text classification. BERT processes and understands the context of words in sentences using transformers, which are not inherently designed to handle audio signal processing or features like MFCCs (Mel-frequency cepstral coefficients).

For Speech Emotion Recognition (SER), features are typically extracted from audio signals, and models like SVMs, Random Forests, or LSTMs are more suitable because they are designed to handle numerical data derived from audio features. BERT, on the other hand, excels in understanding and contextualizing text data but is not optimized for direct audio signal processing tasks.

## Contact

Feel free to contact the author:
- **Phone:** 0369285329
- **Email:** [tranhoaibao9@gmail.com](mailto:tranhoaibao9@gmail.com)
