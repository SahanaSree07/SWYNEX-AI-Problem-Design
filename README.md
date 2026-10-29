# Spam Email Classifier (Spam vs Not Spam)

TF-IDF + Multinomial Naive Bayes / Logistic Regression (scikit-learn).

## Run
pip install -r requirements.txt
python make_sample_data.py                 # optional: synthetic demo data -> data/emails.csv
python spam_classifier.py train            # trains, compares models, saves best model
python spam_classifier.py predict "You won a free prize, click http://x.biz"
python spam_classifier.py interactive

## Use a real dataset (recommended for submission)
Download the SMS Spam Collection (UCI) or Kaggle "spam.csv" into data/ then:
python spam_classifier.py train --data data/spam.csv

## Outputs
spam_model.joblib, results.csv (accuracy/precision/recall/F1), confusion_matrix.png

## Notes
- Data is deduplicated; 80/20 stratified train/test split.
- Best model is chosen by precision first (avoid marking real emails as spam), then F1.
- English text only; ignores attachments, images, and sender info.
