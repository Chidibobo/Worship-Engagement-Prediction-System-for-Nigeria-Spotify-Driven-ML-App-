from src.data_ingestion.spotify_fetch_artist import fetch_artist  
from src.data_ingestion.spotify_fetch_playlist import fetch_top_artist_playlists 
from src.data_ingestion.tidy_json import tidy_artist_data, tidy_tracks_data, tidy_metrics
from src.data_ingestion.ingession import save_artist, save_artist_tracks,save_artist_metrics
from src.config.logger import get_logger
import pandas as pd


logger = get_logger(__name__)



def ingession(artist_id:str, market:str, source:str):
    try:
        logger.info(f"STARTING INGESSION PIPELINE....")

        logger.info(f"Fetch Artist Data")
        artist_data = fetch_artist(artist_id)

        logger.info(f"Fetch Tracks Data")
        track_data = fetch_top_artist_playlists(artist_id, market)

        if artist_data:
            logger.info(f"Tidy artist Data")
            record = tidy_artist_data(artist_data,source)
            if record:
                logger.info(f"Save Tidied Artist Data")
                save_artist(record)

            logger.info(f"Tidy Artist Metrics")
            metrics_record = tidy_metrics(artist_data)
            if metrics_record:
                logger.info(f"Save Tidied Artist Metrics")
                save_artist_metrics(metrics_record)
        
        else:
            logger.warning("No artist data recieved, skipping artist ingession")

        
        if track_data and 'tracks' in track_data:
            logger.info(f"Tidy Tracks Data")
            track_record = tidy_tracks_data(track_data['tracks'], artist_id)

            if track_record:
                logger.info(f"Save Tidied Tracks Data")
                for track in track_record:
                    save_artist_tracks(track)
        
        else:
            logger.warning("No track data recieved, skipping tracks ingession")

        logger.info(f"INGESSION SUCCESSFUL")
        return True

    except Exception as e:
        logger.error(f"Error During Ingession: {str(e)}")
        return False
                



if __name__ == "__main__":
    
    from src.storage.init_db import init_db
    
    #Initialize database 
    init_db()
    gospel_df = pd.read_csv("data/Gospel_artist_ids.csv")
    for i in gospel_df['id']:
        # Run ingestion
        success = ingession(
            artist_id=i,  
            market="NG",
            source="spotify"
        )
    
    if success:
        logger.info(f"Pipeline completed successfully")
    else:
        logger.error(f"Pipeline failed")