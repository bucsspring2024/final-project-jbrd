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
                        max_results=1
                        )
        
                results_df=pd.DataFrame(results)
                results_df.to_csv('duckduck_tutorial.csv',index=False)

        def toStr(results):
                pass
