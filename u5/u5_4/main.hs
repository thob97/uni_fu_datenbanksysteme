  -- imports --
import Control.Monad
import Database.HDBC
import Database.HDBC.PostgreSQL

  -- functions --
main :: IO ()
main = do {dbh <- connectPostgreSQL "host=localhost dbname=dbs user=postgres password=postgres";
             rows <- quickQuery' dbh "SELECT * FROM passagier"[];       -- do a query
             forM_ rows $ \row -> putStrLn $ show row;                  -- print the query; forM_ :: Monad m => [a] -> (a -> m b) -> m ()
            }
