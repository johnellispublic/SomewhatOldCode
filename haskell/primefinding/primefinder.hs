import System.Environment

lesqrt :: Integer -> Integer -> Bool
lesqrt a b = (b*b <= a)

isprime :: Integer -> Bool
isprime n = not ( any (==0) (map (mod n) (possiblefactors n)))

possiblefactors :: Integer -> [Integer]
possiblefactors n = takeWhile (lesqrt n) primes

nextprime :: Integer -> Integer
nextprime n
  | isprime (n+1) = (n+1)
  | otherwise = nextprime (n+1)

primes = 2 : [nextprime n | n <- primes]

findprimesupto :: Integer -> [Integer]

findprimesupto n = takeWhile (<=n) primes

main = do
  maxnstr <- getArgs
  let n = [read (i) :: Integer | i <- maxnstr]
  let a = map findprimesupto n
  putStr (unlines [ unwords [ show j | j <- i] ++ "\n" | i <- a])
