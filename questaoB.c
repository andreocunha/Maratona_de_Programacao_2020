#include <stdio.h>

void colocaNavio(int (*tabuleiro)[10], int X, int Y, int len, int orient) {
    for(int i = 0; i < len; i++) {
        if(orient == 1) {
            tabuleiro[X + i - 1][Y - 1] = 1;
        } else {
            tabuleiro[X - 1][Y + i - 1] = 1;
        }
    }
}

int verificaSeTemNavio(int (*tabuleiro)[10], int X, int Y, int len, int orient) {
    int tem = 0;
    
    for(int i = 0; i < len; i++) {
        if(orient == 1) {
            if(tabuleiro[X + i - 1][Y - 1] == 1){
                tem = 1;
                break;
            }
        } else {
            if(tabuleiro[X - 1][Y + i - 1] == 1){
                tem = 1;
                break;
            }
        }
    }

    return tem;
}

int main() {
    int tabuleiro[10][10];
    int i, j;

    int numNavios;

    int D, L, R, C;

    for(i = 0; i < 10; i++) {
        for(j = 0; j < 10; j++) {
            tabuleiro[i][j] = 0;
        }
    }

    scanf("%d", &numNavios);
    int valido = 1;

    for(i = 0; i < numNavios; i++) {
        scanf("%d %d %d %d",&D, &L, &R, &C);
        if(C > 10 || C < 1 || R > 10 || R < 1) {
            valido = 0;
            break;
        }
        if(D == 0) {
            if(C + L - 1 > 10){
                valido = 0;
                break;
            }
        } else if(D == 1) {
            if(R + L - 1 > 10){
                valido = 0;
                break;
            }   
        }

        if(verificaSeTemNavio(tabuleiro, R, C, L, D)) {
            valido = 0;
            break;
        }

        colocaNavio(tabuleiro, R, C, L, D);
        //for(int k = 0; k < 10; k++) {
        //    for(j = 0; j < 10; j++) {
        //        printf("%d ", tabuleiro[k][j]);
        //    }
        //    printf("\n");
        //}
    }

    if(valido)
        printf("Y\n");
    else
        printf("N\n");
    

    return 0;
}