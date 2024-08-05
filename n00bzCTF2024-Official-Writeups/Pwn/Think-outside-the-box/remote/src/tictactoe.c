#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

void init() {
    setbuf(stdin, NULL);
    setbuf(stdout, NULL);
    setbuf(stderr, NULL);
}

void main() {
	init();
	int size = 3;
	int botfirstrow;
	int botfirstcolumn;
	int botsecondrow;
	int botsecondcolumn;
	int botthirdrow;
	int botthirdcolumn;
	int botfourthrow;
	int botfourthcolumn;
	char board[3][3] = {
	        { '_', '_', '_' },
	        { '_', 'X', '_' },
	        { '_', '_', '_' }
	    };
    puts("Welcome to Tic-Tac-Toe! In order to get the flag, just win! The bot goes first!");
    printBoard(board,size);
    move(board,size,1,&botfirstrow,&botfirstcolumn,0,1);
    printBoard(board,size);
    move(board,size,2,&botsecondrow,&botsecondcolumn,botfirstrow,botfirstcolumn);
    printBoard(board,size);
    move(board,size,3,&botthirdrow,&botthirdcolumn,botsecondrow,botsecondcolumn);
   	printBoard(board,size);
    move(board,size,4,&botfourthrow,&botfourthcolumn,botthirdrow,botthirdcolumn);



 }
int canWin(char board[3][3], int size, char player) {
    for (int i = 0; i < size; i++) {
        int countPlayer = 0;
        int emptyCell = -1;
        for (int j = 0; j < size; j++) {
            if (board[i][j] == player) {
                countPlayer++;
            } else if (board[i][j] == '_') {
                emptyCell = j;
            }
        }
        if (countPlayer == size - 1 && emptyCell != -1) {
            board[i][emptyCell] = player;
            return 1;
        }
    }
    for (int j = 0; j < size; j++) {
        int countPlayer = 0;
        int emptyCell = -1;
        for (int i = 0; i < size; i++) {
            if (board[i][j] == player) {
                countPlayer++;
            } else if (board[i][j] == '_') {
                emptyCell = i;
            }
        }
        if (countPlayer == size - 1 && emptyCell != -1) {
            board[emptyCell][j] = player;
            return 1;
        }
    }
    int countPlayer = 0;
    int emptyCell = -1;
    for (int i = 0; i < size; i++) {
        if (board[i][i] == player) {
            countPlayer++;
        } else if (board[i][i] == '_') {
            emptyCell = i;
        }
    }
    if (countPlayer == size - 1 && emptyCell != -1) {
        board[emptyCell][emptyCell] = player;
        return 1;
    }
    countPlayer = 0;
    emptyCell = -1;
    for (int i = 0; i < size; i++) {
        if (board[i][size - i - 1] == player) {
            countPlayer++;
        } else if (board[i][size - i - 1] == '_') {
            emptyCell = i;
        }
    }
    if (countPlayer == size - 1 && emptyCell != -1) {
        board[emptyCell][size - emptyCell - 1] = player;
        return 1;
    }

    return 0;
}
int checkWin(char board[3][3], int size) {
    int c = 1;
    int row = 1;
    for (int r = 0; r < size; r++) {
    	if ((board[r][c]==board[r][c-1])&&(board[r][c]==board[r][c+1])&&(board[r][c]=='O')) {
    		puts("Returning!");
    		return 1;
    	}
    }
    for (int col = 0; col < size; col++) {
    	if ((board[row][col]==board[row-1][col])&& (board[row][col] == board[row+1][col]) && (board[row][col]=='O')) {
    		return 1;
    	}
    }
    return 0;
    
}
void move(char board[3][3],int size,int movenum,int *a,int *b,int previousrow,int previouscolumn) {
	int botfirstrow;
	int botfirstcolumn;
	int botsecondrow;
	int botsecondcolumn;
	int botthirdrow;
	int botthirdcolumn;
	int botfourthrow;
	int botfourthcolumn;
	int row;
	int column;
	FILE *flagptr;
	printf("Move: ");
	scanf("%d,%d", &row, &column);
	if (row < size && column < size && board[row][column] != 'X' && board[row][column]!='O') {
		bool x;
		board[row][column] = 'O';
		x = checkWin(board,size);
		if (x) {
			printBoard(board,size);
			printf("You won! Flag: ");
			flagptr = fopen("/srv/flag.txt", "r");
			char flag[60];
			fgets(flag, 60, flagptr);
			printf("%s\n", flag);
			exit(0);
		}
		printBoard(board,size);
		if (movenum == 1) {
			puts("Bot turn!");
			firstmove(board,row,column,&botfirstrow,&botfirstcolumn);
			*a = botfirstrow;
			*b = botfirstcolumn;	
		}
		if (movenum == 2) {
			puts("Bot turn!");
			secondmove(board,row,column,&botsecondrow,&botsecondcolumn,previousrow,previouscolumn,size);
			*a = botsecondrow;
			*b = botsecondcolumn;
		}
		if (movenum == 3) {
			puts("Bot turn!");
			thirdmove(board,row,column,&botthirdrow,&botthirdcolumn,previousrow,previouscolumn,size);
		}
		if (movenum == 4) {
			puts("Bot turn!");
			fourthmove(board,row,column,&botfourthrow,&botfourthcolumn,previousrow,previouscolumn,size);
		}


}
	else {
		puts("Invalid move!");
		exit(0);
	}
}

void printBoard(char board[3][3],int size) {
	int a = 3;
    for (int i = 0; i < a; i++) {
        for (int j = 0; j < a; j++) {
            printf(" %c ", board[i][j]);
            if (j < a - 1) printf("|");
        }
        printf("\n");
        if (i < a - 1) printf("---|---|---\n");
    }
}

void firstmove(char board[3][3],int row,int column,int *botfirstrow,int *botfirstcolumn) {
	if (row == 0 && column == 0 || row == 0 && column == 2) {
		if (board[0][1] = '_') {
			board[0][1] = 'X';
			*botfirstrow = 0;
			*botfirstcolumn = 1;
		}
	}
	if (row == 2 && column == 0 || row == 2 && column == 2) {
		if (board[2][1] == '_') {
			board[2][1] = 'X';
			*botfirstrow = 2;
			*botfirstcolumn = 1;
		}
	}
	if (row == 0 && column == 1 || row == 1 && column == 2 || row == 2 && column == 1) {
		if (board[0][2] == '_') {
			board[0][2]='X';
			*botfirstrow = 0;
			*botfirstcolumn = 2;
		}
	}
	if (row == 1 && column == 0 || row == 2 && column == 0 ) {
		if (board[2][0]=='_') {
			board[2][0]='X';
			*botfirstrow = 2;
			*botfirstcolumn = 0;
		}
	}

}

void secondmove(char board[3][3],int row,int column,int *botrow,int *botcolumn,int previousrow, int previouscolumn, int size) {
	bool x;
	x = canWin(board,size,'X');
	if (x) {
		printBoard(board,size);
		puts("Bot wins!");
		exit(0);
	}
	if (row == 2 && column == 1) {
		if (board[2][0] = '_') {
			board[2][0] = 'X';
			*botrow = 2;
			*botcolumn = 0;
		}
	}
	if ((row == 0 && column == 1)) {
		if (board[0][0] = '_') {
			board[0][0] = 'X';
			*botrow = 0;
			*botcolumn = 0;
			return;
		}
	}
	if (row == 2 && column == 0 && previousrow == 0 && previouscolumn == 2) {
		if (board[2][0] == 'O' && board[2][1] == 'O') {
			board[2][2] = 'X';
			*botrow = 2;
			*botcolumn=2;
			return;
		}
		if (board[0][0] == '_' && board[0][1] == '_') {
			board[0][0] = 'X';
			*botrow = 0;
			*botcolumn = 0;
			return;
		}
		else if (board[0][0] == '_' && board[0][1]== 'O') {
			board[2][2] = 'X';
			*botrow = 2;
			*botcolumn = 2;
		}
	}
	if (row == 2 && column == 0 || row == 0 && column == 2) {
		if (board[2][2] == '_') {
			board[2][2] = 'X';
			*botrow = 2;
			*botcolumn = 2;
		}
	}
}

void thirdmove(char board[3][3],int row,int column,int *botrow,int *botcolumn,int previousrow, int previouscolumn, int size) {
	bool x;
	x = canWin(board,size,'X');
	if (x) {
		printBoard(board,size);
		puts("Bot wins!");
		exit(0);
	}	
	if (row == 0 && column == 2 || row == 1 && column == 0 || row == 2 && column == 0) {
		if (board[1][2]=='_') {
			board[1][2]='X';
			*botrow = 1;
			*botcolumn = 2;
		}

	}

	if (row == 1 && column == 2) {
		if (board[2][2] == '_' && board[1][2]=='O' && board[0][2]=='O') {
			board[2][2]='X';
			*botrow = 2;
			*botcolumn = 2;
		}
		else if (board[0][2] == '_' && board[1][2]=='O' && board[2][2]=='O') {
			board[0][2]='X';
			*botrow = 0;
			*botcolumn = 2;
		}
	}
	if (row == 2 && column == 2) {
		if (board[0][2]=='_') {
			board[0][2] = 'X';
			*botrow = 0;
			*botcolumn = 2;
		}
		else if(board[0][2]=='O' && board[2][2]=='O')
			board[1][2]='X';
			*botrow = 1;
			*botcolumn = 2;
	}
}

void fourthmove(char board[3][3],int row,int column,int *botrow,int *botcolumn,int previousrow, int previouscolumn, int size) {
	bool x;
	x = canWin(board,size,'X');
	if (x) {
		printBoard(board,size);
		puts("Bot wins!");
		exit(0);
	}	
	for (int i = 0; i < size; i++) {
		for (int j = 0; j < size; j++) {
		if (board[i][j]=='_') {
			board[i][j]='X';
			printBoard(board,size);
			puts("Draw!");
			exit(0);
		}
	}
}
}
