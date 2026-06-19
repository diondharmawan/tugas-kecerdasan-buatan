import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
import nbformat as nbf
import json

# Create 'hasil' directory
os.makedirs('hasil', exist_ok=True)

print("1. Loading dataset...")
df = pd.read_csv('instruksi/playstore_reviews.csv')
df = df.dropna(subset=['content', 'score'])

print("2. Preprocessing...")
def get_sentiment(score):
    if score <= 2:
        return 'Negatif'
    elif score == 3:
        return 'Netral'
    else:
        return 'Positif'

df['sentiment'] = df['score'].apply(get_sentiment)
df = df[df['sentiment'] != 'Netral'] # Simplify to Positif/Negatif

# Sentiment Distribution Plot
plt.figure(figsize=(6,4))
sns.countplot(data=df, x='sentiment', palette='viridis')
plt.title('Distribusi Sentimen Ulasan WhatsApp')
plt.xlabel('Sentimen')
plt.ylabel('Jumlah')
plt.savefig('hasil/sentiment_distribution.png')
plt.close()

print("3. Training Model...")
X = df['content']
y = df['sentiment']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

vectorizer = TfidfVectorizer(max_features=5000)
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

svm = SVC(kernel='linear', random_state=42)
svm.fit(X_train_vec, y_train)

y_pred = svm.predict(X_test_vec)

print("4. Evaluation...")
acc = accuracy_score(y_test, y_pred)
prec = precision_score(y_test, y_pred, pos_label='Positif')
rec = recall_score(y_test, y_pred, pos_label='Positif')
f1 = f1_score(y_test, y_pred, pos_label='Positif')

results = f"""
Evaluasi Model SVM:
Akurasi   : {acc:.4f}
Precision : {prec:.4f}
Recall    : {rec:.4f}
F1-Score  : {f1:.4f}
"""
print(results)
with open('hasil/eval_results.txt', 'w') as f:
    f.write(results)

# Confusion Matrix
cm = confusion_matrix(y_test, y_pred, labels=['Negatif', 'Positif'])
plt.figure(figsize=(6,4))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=['Negatif', 'Positif'], yticklabels=['Negatif', 'Positif'])
plt.title('Confusion Matrix SVM')
plt.xlabel('Prediksi')
plt.ylabel('Aktual')
plt.savefig('hasil/confusion_matrix.png')
plt.close()

print("5. Generating Jupyter Notebook...")
nb = nbf.v4.new_notebook()

md_header = """# Tugas Kecerdasan Buatan (Artificial Intelligence)
**Topik:** Natural Language Processing (NLP) - Analisis Sentimen Ulasan Google Play Store
**Algoritma:** Support Vector Machine (SVM)

**Identitas Mahasiswa:**
- **Nama:** Fransiscus Asisi Kananda Herdion Dharmawan
- **NIM:** 24.83.1107
- **Jurusan:** Teknik Komputer
- **Universitas:** Universitas Amikom Yogyakarta
"""

code_import = """import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score"""

md_data = "## 1. Data Loading & Preprocessing"
code_data = """# Load dataset
try:
    df = pd.read_csv('playstore_reviews.csv')
except FileNotFoundError:
    df = pd.read_csv('instruksi/playstore_reviews.csv')
df = df.dropna(subset=['content', 'score'])
df['content'] = df['content'].astype(str)

# Kategorisasi skor ke dalam sentimen
def get_sentiment(score):
    if score <= 2:
        return 'Negatif'
    elif score == 3:
        return 'Netral'
    else:
        return 'Positif'

df['sentiment'] = df['score'].apply(get_sentiment)

# Kita abaikan sentimen 'Netral' untuk fokus ke binary classification
df = df[df['sentiment'] != 'Netral']

# Tampilkan beberapa data awal
display(df[['content', 'score', 'sentiment']].head())

# Plot distribusi
plt.figure(figsize=(6,4))
sns.countplot(data=df, x='sentiment', hue='sentiment', palette='viridis', legend=False)
plt.title('Distribusi Sentimen Ulasan')
plt.show()"""

md_model = "## 2. Pembangunan Model (TF-IDF & SVM)"
code_model = """# Split Data
X = df['content']
y = df['sentiment']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# TF-IDF Vectorization
vectorizer = TfidfVectorizer(max_features=5000)
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# Inisialisasi dan Training Model Support Vector Machine
svm_model = SVC(kernel='linear', random_state=42)
svm_model.fit(X_train_vec, y_train)

print("Proses training model selesai.")"""

md_eval = "## 3. Evaluasi & Hasil Uji"
code_eval = """# Prediksi pada data testing
y_pred = svm_model.predict(X_test_vec)

# Menampilkan metrik
print("Akurasi:", accuracy_score(y_test, y_pred))
print("\\nClassification Report:\\n", classification_report(y_test, y_pred))

# Visualisasi Confusion Matrix
cm = confusion_matrix(y_test, y_pred, labels=['Negatif', 'Positif'])
plt.figure(figsize=(6,4))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=['Negatif', 'Positif'], yticklabels=['Negatif', 'Positif'])
plt.title('Confusion Matrix SVM')
plt.xlabel('Prediksi')
plt.ylabel('Aktual')
plt.show()"""

nb['cells'] = [
    nbf.v4.new_markdown_cell(md_header),
    nbf.v4.new_code_cell(code_import),
    nbf.v4.new_markdown_cell(md_data),
    nbf.v4.new_code_cell(code_data),
    nbf.v4.new_markdown_cell(md_model),
    nbf.v4.new_code_cell(code_model),
    nbf.v4.new_markdown_cell(md_eval),
    nbf.v4.new_code_cell(code_eval)
]

with open('hasil/Tugas_AI_NLP_Dion.ipynb', 'w', encoding='utf-8') as f:
    nbf.write(nb, f)
    
print("All tasks completed successfully!")
