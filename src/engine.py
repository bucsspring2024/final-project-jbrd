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
                
                

                
                results_df.to_csv('duckduck_tutorial.csv',index=False)
                df = pd.read_csv('duckduck_tutorial.csv')

                result_df = df[['title', 'href']]
                result_df.to_csv('duckduck_tutorial.csv',index=False)
                
                
                return(results_df)
                
                

        def toStr(results_df):
                results=results_df
                print (pd.DataFrame(results))
                
