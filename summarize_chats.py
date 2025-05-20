import os
import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer

nltk.download('punkt')
nltk.download('stopwords')

def process_chat(file_path):
    user_messages = []
    ai_messages = []

    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            if line.startswith("User:"):
                message = line[len("User:"):].strip()
                user_messages.append(message)
            elif line.startswith("AI:"):
                message = line[len("AI:"):].strip()
                ai_messages.append(message)
    
    count_user = len(user_messages)
    count_ai = len(ai_messages)
    total_exchanges = min(count_user, count_ai)

    all_messages = user_messages + ai_messages
    combined_text = " ".join(all_messages)

    stop_words = stopwords.words('english')
    vectorizer = TfidfVectorizer(stop_words=stop_words)
    tfidf_matrix = vectorizer.fit_transform([combined_text])

    feature_names = vectorizer.get_feature_names_out()
    scores = tfidf_matrix.toarray()[0]
    word_score_pairs = list(zip(feature_names, scores))
    top_keywords = sorted(word_score_pairs, key=lambda x: x[1], reverse=True)[:5]
    keywords = [word for word, score in top_keywords]

    first_top_word = keywords[0] if keywords else "unknown topic"
    second_top_word = keywords[1] if len(keywords) > 1 else ""

    if second_top_word:
        nature = f"The user asked mainly about {first_top_word} and its {second_top_word}."
    else:
        nature = f"The user asked mainly about {first_top_word}."

    summary = f"""
Summary for: {os.path.basename(file_path)}
- Total exchanges: {total_exchanges}
- {nature}
- Top Keywords: {', '.join(keywords)}
"""
    return summary.strip()

def summarize_all_chats(folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith('.txt'):
            file_path = os.path.join(folder_path, filename)
            summary = process_chat(file_path)
            print(summary)
            print('-' * 60)

if __name__ == "__main__":
    folder_path = "chat_logs"  
    summarize_all_chats(folder_path)
