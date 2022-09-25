data Tree = Operand Integer | Operator Char (Tree) (Tree) | EmptyTree

singleton :: Integer -> Integer -> Char -> Tree


insert :: Integer -> Integer -> Char -> Tree -> Tree
insert op1 op2 comm EmptyTree = Operator comm Operand op1
