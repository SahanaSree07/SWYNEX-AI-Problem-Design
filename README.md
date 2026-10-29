# SWYNEX AI Problem Design: Spam Email Classifier

A narrow AI use case: classify a message as **Spam** or **Not Spam**.

## 1. AI Use Case
The system reads the text of a message and predicts one of two labels: Spam or Not Spam. It does one task only (binary text classification).

## 2. Target User
College students and everyday email/SMS users who receive unwanted promotional, scam, or phishing messages and want them flagged automatically.

## 3. Data Source
**SMS Spam Collection** (UCI Machine Learning Repository / Kaggle), a public dataset of labeled messages.
- 5,171 unique messages after removing duplicates: 653 spam and 4,518 not spam.
- 80/20 stratified train/test split (1,035 test messages).
- `download_data.py` downloads it to `data/spam.csv`. `make_sample_data.py` creates a small synthetic set for offline testing only.

## 4. AI Method
- **Preprocessing:** lowercase, replace URLs and numbers with tokens, remove punctuation and stop words.
- **Features:** TF-IDF (unigrams and bigrams).
- **Models compared:** Multinomial Naive Bayes and Logistic Regression.
- **Model selection:** highest precision first (a real message wrongly marked as spam is the costlier error), then F1.

## 5. Constraints
- The dataset is small and made of SMS messages, not full emails.
- English text only; binary classification only (no phishing vs. promotion categories).
- Attachments, images, links, and sender information are not analyzed.
- The data is imbalanced (about 13% spam), so accuracy alone can mislead.
- Spam wording changes over time, so the model would need retraining.

## 6. Evaluation Approach
Evaluated on the held-out 20% test set using accuracy, precision, recall, F1-score, and a confusion matrix (`confusion_matrix.png`, `results.csv`).

## 7. Results

| Model | Accuracy | Precision | Recall | F1 |
|---|---|---|---|---|
| Multinomial Naive Bayes (selected) | 97.68% | 99.08% | 82.44% | 90.00% |
| Logistic Regression | 96.62% | 81.17% | 95.42% | 87.72% |

Naive Bayes confusion matrix: 903 true negatives, 1 false positive, 23 false negatives, 108 true positives.

**Why Naive Bayes:** it wrongly flagged only 1 legitimate message as spam, while Logistic Regression flagged 29. It catches fewer spam messages (82% recall), which is an accepted trade-off.

**Observed limitation:** the message "URGENT! Your account is suspended, send your bank details to verify" scored only 26.84% spam and was missed. The SMS training data contains few phishing-style messages. A larger email dataset with phishing examples would improve this.

## 8. How to Run
```
pip install -r requirements.txt
python download_data.py
python spam_classifier.py train --data data/spam.csv
python spam_classifier.py predict "Congratulations! You won a free prize, click http://claim.biz"
python spam_classifier.py interactive
```

## 9. Expected Outcome
The system automatically flags most unwanted messages with high precision, saving users time and reducing the risk of clicking scam links.
