import pandas as pd
def text_category(p) -> str:
    if p < 0:
        return 'negative'
    elif p == 0:
        return 'neutral'
    else:
        return 'positive'
    
class DataPreparation:
    def __init__(self,df:pd.DataFrame)->pd.DataFrame:
        self.df = df
    def create_score(self,df:pd.DataFrame)->pd.DataFrame:
        df['score'] = df['polarity'].apply(text_category)
        return df
    def create_scoremap(self, df: pd.DataFrame) -> pd.DataFrame:
        #remove the neutral rows
        df = df[df['polarity']!=0] 
        df.reset_index()
        df['scoremap'] = df['score'].apply(
            lambda x: 0 if x == 'negative' else 1)
        return df
    
