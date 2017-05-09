# reverse print a two dimention list py27
# by sfzhang 2016/05/23
""". . O O O O O . .
   . O O O O O O O .
   . O O O O O O O .
   . . O O O O O . .
   . . . O O O . . .
   . . . . O . . . .
"""
grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]


def reverse_pr(ls):
    for column in range(len(ls[0])):
        for row in ls:
            print(row[column],)
        print()

if __name__ == "__main__":
    reverse_pr(grid)
