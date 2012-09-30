main :: IO ()
main = getContents >>= putStr . show . calculate

calculate :: String -> Int
calculate input = 0
