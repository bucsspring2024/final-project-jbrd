import pandas as pd
from duckduckgo_search import DDGS
class searchEngine:
        def search(string):
                search_query=string
                results= DDGS().text( 
                        keywords=search_query,
                        region='wt-wt',
                        safesearch='off',
                        timelimit='7d',
                        max_results=5
                        )
        
                results_df=pd.DataFrame(results)
                
                

                
                results_df.to_csv('file.csv',index=False)
                df = pd.read_csv('file.csv')

                result_df = df[['title', 'href']]
                result_df.to_csv('file.csv',index=False)
                
                
                
                
                

        
