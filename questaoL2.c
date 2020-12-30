#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int 
ehAnagrama( char* p1, char* p2)
{
    int cont[256], cont2[256], i, flag = 0; /*cont e cont2 servem para ver o numero de vezes que cada letra aparece*/

    for (i = 0; i < 256; i++)	 /*zera o vetor que conta as letras da primeira palavra*/
        cont[i] = 0;
    for (i = 0; i < 256; i++)	 /*zera o vetor que conta as letras da segunda palavra*/
        cont2[i] = 0;
    for (i = 0; p1[i] != '\0'; i++) {	   /*percorre a primeira palavra*/
        cont[p1[i]]++;					   /*conta quantas vezes cada letra da palavra aparece*/
    }
    for (i = 0; p2[i] != '\0'; i++) {		 /*percorre a segunda palavra*/
        cont2[p2[i]]++;						/* conta quantas vezes cada letra da palavra aparece*/
    }
    for (i = 0; i < 256; i++) {				  /*percorre o vetor que conta letras*/
        if (cont[i] != cont2[i])	 /* se o numero de vezes que uma letra ocorre na palavra 1 eh diferente da palavra 2 flag recebe1*/
            flag = 1;				/* significa que não são anagramas*/
    }
    if (flag == 0)
        return 1;
    else
        return 0; 
}

int main() {
    int L, C;
    scanf("%d %d", &L, &C);

    char matriz[L][C];

    for(int i = 0; i < L; i++) {
        for(int j = 0; j < C; j++) {
            scanf("%c", &matriz[i][j]);
        }
    }

    int qtdPalavras;

    scanf("%d", &qtdPalavras);
    char palavras[qtdPalavras][41];

    for(int i = 0; i < qtdPalavras; i++) {
        scanf("%s", palavras[i]);
    }

    char palTempH[40], palTempV[40], palTempD[40];
    int tamPal;

    for(int i = 0; i < qtdPalavras; i++) {
        tamPal = strlen(palavras[i]);
        for(int j = 0; j < L; j++) {
            for(int k = 0; k < C; k++) {
                for(int t = 0; t < tamPal; t++) {
                    if(k+t < C)
                        palTempH[t] = matriz[j][k+t];
                    else
                        break;
                }
            }
        }
    }

    return 0;
}
