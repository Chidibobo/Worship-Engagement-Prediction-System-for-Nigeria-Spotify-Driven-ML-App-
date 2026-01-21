# Worship Engagement Prediction System for Nigerian Gospel Artists

A machine learning-powered system that predicts worship engagement metrics for Nigerian gospel artists using Spotify data. This project aims to help artists, labels, and industry stakeholders understand and predict audience engagement patterns in the Nigerian gospel music market.

## 🎯 Project Overview

This system collects and analyzes Spotify data from Nigerian gospel artists to build predictive models for engagement metrics such as:
- Artist popularity trends
- Follower growth patterns
- Track performance indicators
- Weekly engagement metrics

## 📊 Current Progress

### ✅ Completed Features

#### **Data Infrastructure**
- **Spotify API Integration**: Complete authentication and data fetching system
  - OAuth2 client credentials flow
  - Artist profile data retrieval
  - Top playlist tracks fetching (Nigeria market)
  
- **Data Ingestion Pipeline**: Automated data collection system
  - Batch processing for multiple artists
  - Data transformation and cleaning utilities
  - Error handling and logging

- **Database Schema**: SQLite database with three main tables:
  - `artists`: Artist profiles (ID, name, genres, source)
  - `tracks`: Track metadata (ID, artist, name, duration, release date)
  - `artist_weekly_metrics`: Time-series metrics (followers, popularity, week tracking)

#### **Core Functionality**
- ✅ Spotify API authentication (`src/data_ingestion/auth.py`)
- ✅ Artist data fetching (`src/data_ingestion/spotify_fetch_artist.py`)
- ✅ Playlist/track data fetching (`src/data_ingestion/spotify_fetch_playlist.py`)
- ✅ Data transformation utilities (`src/data_ingestion/tidy_json.py`)
- ✅ Database operations (`src/storage/`)
- ✅ Comprehensive logging system (`src/config/logger.py`)
- ✅ Batch ingestion script (`src/run_ingession.py`)

#### **Data Collection**
- ✅ Gospel artist ID list (`data/Gospel_artist_ids.csv`) with 60+ Nigerian gospel artists
- ✅ Automated ingestion pipeline for batch processing
- ✅ Error handling and retry logic

#### **Development & Analysis Tools**
- ✅ Explainability notebook for data exploration (`src/explainability/explainability_notebook.ipynb`)
- ✅ Test notebooks for development and testing

### 🚧 In Progress

- **Streamlit Web Application**: UI skeleton created (`src/app/streamlit_app.py`) - *needs implementation*
- **Data Analysis**: Initial exploratory work in notebooks

## 🔮 What's Coming Next

### **Phase 1: Machine Learning Models** 🎯
- [ ] **Feature Engineering**
  - Time-series feature extraction from weekly metrics
  - Track-level aggregated features
  - Artist metadata feature engineering
  
- [ ] **Model Development**
  - Engagement prediction models (regression)
  - Popularity trend forecasting (time-series)
  - Follower growth prediction
  - Track performance classification

- [ ] **Model Training & Evaluation**
  - Train/test split strategies
  - Cross-validation setup
  - Model performance metrics (RMSE, MAE, R²)
  - Model comparison and selection

### **Phase 2: Model Explainability** 📊
- [ ] SHAP value integration for model interpretability
- [ ] Feature importance analysis
- [ ] Interactive visualizations in explainability notebook
- [ ] Model decision explanations

### **Phase 3: Web Application** 🌐
- [ ] Streamlit dashboard implementation
- [ ] Artist search and selection interface
- [ ] Real-time predictions display
- [ ] Interactive charts and visualizations
- [ ] Historical trend analysis views
- [ ] Model explainability visualizations

### **Phase 4: Advanced Features** 🚀
- [ ] Automated model retraining pipeline
- [ ] Scheduled data ingestion (weekly/monthly updates)
- [ ] API endpoints for predictions (optional FastAPI)
- [ ] Multi-market support (beyond Nigeria)
- [ ] Comparative analysis tools (artist vs artist)

### **Phase 5: Deployment & Operations** 🏗️
- [ ] Docker containerization
- [ ] Cloud deployment configuration
- [ ] CI/CD pipeline setup
- [ ] Monitoring and alerting
- [ ] Database migration scripts

## 🛠️ Installation

### Prerequisites
- Python 3.8+
- Spotify API credentials (Client ID and Client Secret)

### Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/Worship-Engagement-Prediction-System-for-Nigeria-Spotify-Driven-ML-App-.git
   cd Worship-Engagement-Prediction-System-for-Nigeria-Spotify-Driven-ML-App-
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure environment variables**
   Create a `.env` file in the project root:
   ```env
   CLIENT_ID=your_spotify_client_id
   CLIENT_SECRET=your_spotify_client_secret
   TOKEN_URL=https://accounts.spotify.com/api/token
   BASE_URL=https://api.spotify.com/v1
   ```

4. **Initialize the database**
   ```bash
   python -m src.storage.init_db
   ```

5. **Run data ingestion** (optional - to populate database)
   ```bash
   python src/run_ingession.py
   ```

## 📁 Project Structure

```
.
├── data/
│   ├── Gospel_artist_ids.csv      # List of Nigerian gospel artists
│   └── spotify_data.db            # SQLite database (gitignored)
├── logs/                          # Application logs (gitignored)
├── src/
│   ├── app/
│   │   └── streamlit_app.py       # Streamlit web app (to be implemented)
│   ├── config/
│   │   ├── logger.py              # Logging configuration
│   │   └── setup.py               # Environment configuration
│   ├── data_ingestion/
│   │   ├── auth.py                # Spotify API authentication
│   │   ├── ingession.py           # Database save operations
│   │   ├── spotify_fetch_artist.py # Artist data fetching
│   │   ├── spotify_fetch_playlist.py # Track data fetching
│   │   └── tidy_json.py           # Data transformation utilities
│   ├── explainability/
│   │   └── explainability_notebook.ipynb # Model explainability analysis
│   ├── storage/
│   │   ├── db.py                  # Database connection utilities
│   │   └── init_db.py             # Database schema initialization
│   ├── run_ingession.py           # Main ingestion pipeline script
│   └── test_notebooks/            # Development and testing notebooks
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
```

## 🚀 Usage

### Data Ingestion

Run the ingestion pipeline to collect data for all artists:

```bash
python src/run_ingession.py
```

This will:
1. Initialize the database if it doesn't exist
2. Read artist IDs from `data/Gospel_artist_ids.csv`
3. Fetch artist profiles, tracks, and metrics from Spotify
4. Store all data in the SQLite database

### Database Access

Access the database programmatically:

```python
from src.storage.db import get_connection
import pandas as pd

conn = get_connection()
df = pd.read_sql_query("SELECT * FROM artists", conn)
```

### Run Streamlit App (when implemented)

```bash
streamlit run src/app/streamlit_app.py
```

## 📈 Database Schema

### `artists`
- `artist_id` (PRIMARY KEY): Spotify artist ID
- `name`: Artist name
- `genres`: Comma-separated genres
- `source`: Data source (e.g., "spotify")

### `tracks`
- `track_id` (PRIMARY KEY): Spotify track ID
- `artist_id`: Foreign key to artists table
- `name`: Track name
- `duration_ms`: Track duration in milliseconds
- `explicit`: Explicit content flag (0/1)
- `release_date`: Track release date

### `artist_weekly_metrics`
- `id` (PRIMARY KEY): Auto-increment ID
- `artist_id`: Foreign key to artists table
- `week_start`: Week start date
- `followers`: Number of followers
- `popularity`: Popularity score (0-100)
- `collected_at`: Timestamp when data was collected
- UNIQUE constraint on (`artist_id`, `week_start`)

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Author

**Ekeke Chidiebere**

## 🙏 Acknowledgments

- Spotify Web API for music data
- Nigerian Gospel Artists community
- Open source ML and data science community

---

**Status**: 🟡 Active Development  
**Last Updated**: January 2026
