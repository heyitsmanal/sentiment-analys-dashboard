# 🎾 Tennis Sentiment Analysis Dashboard

Interactive Streamlit dashboard that collects recent Reddit discussions about tennis players and applies sentiment analysis to the retrieved comments.

## ✨ Features
- Search Reddit discussions by player or keyword
- Filter results by year
- Classify comment sentiment
- Visualize sentiment distributions and trends
- Explore the original comment text behind the charts

## 🧰 Tech Stack
- Python
- Streamlit
- PRAW
- TextBlob / NLTK
- pandas
- matplotlib

## 🖼️ Preview

![Dashboard preview](./screenshots/img.jpeg)

## 🌐 Demo

Live app: https://tennis-player-analys-dashboard.streamlit.app/

## 🔐 Configuration

The app expects Reddit API credentials through environment variables:

```bash
REDDIT_CLIENT_ID=your-client-id
REDDIT_CLIENT_SECRET=your-client-secret
REDDIT_USER_AGENT=tennis-sentiment-analysis
```

Use `.env.example` as the reference. Do not commit real credentials.

For Streamlit Community Cloud, add these values in the app's Secrets settings instead of committing them to the repository.

## 🚀 Run locally

```bash
python -m venv .venv
# macOS/Linux
source .venv/bin/activate
# Windows
# .venv\Scripts\activate

pip install -r requirements.txt
streamlit run streamlit_app.py
```

## ⚠️ Limitations
- Results depend on Reddit search availability and API limits.
- Sentiment models can misread sarcasm, slang, and context.
- The dashboard is intended for exploratory analysis rather than definitive opinion measurement.
