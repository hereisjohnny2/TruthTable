#include <iostream>
#include<cmath>

int** matrizAlloc(int linhas, int col);
int** montarTabela(int linhas, int col);
void montarLinhaPreps(int col);
void printTabela(int **Tabela, int linhas, int col);

int main()
{
    int col;
    std::cout << "Digite o numero de preposicoes: ";
    std::cin >> col;
    
    int linhas = pow(2, col);
    int **Tabela = montarTabela(linhas, col);  
    printTabela(Tabela, linhas, col);

    system("pause");
    
    return 0;
}

int** matrizAlloc(int linhas, int col) {
    int **Mat = (int **)malloc(linhas * sizeof(int *)); 
    for (int i = 0; i < linhas; i++) {
        Mat[i] = (int *)malloc(col * sizeof(int));
    }

    return Mat;
}

int** montarTabela(int linhas, int col) {
    int **Tabela = matrizAlloc(linhas, col);  
    for (int k=0; k<col; k++) {
        int linha = 0;
        int grupo = pow(2,col-(k+1));
        int grupoLinha = linhas/grupo;
        for (int i=0; i<grupoLinha; i++) {
            for (int j=0; j<grupo; j++) {
                if (i%2) {
                    Tabela[linha][k] = 0;
                } else {
                    Tabela[linha][k] = 1;
                }
                linha++;
            }
        }
    }
    return Tabela;
}

void montarLinhaPreps(int col) {
    char * prepName = "p";

    int ListaPreps[col];

    for (int i=0; i<col; i++) {
        ListaPreps[i] = (int)*prepName + i;
    }

    std::cout << "\n";
    for (int i=0; i<col; i++) {
        std::cout << (char)ListaPreps[i] << "\t\t";
    }
}

void printTabela(int **Tabela, int linhas, int col) {
    
    int valor;
    montarLinhaPreps(col);
    std::cout << sizeof(Tabela) << std::endl;
    std::cout << "\n\n";

    for (int i=0; i<linhas; i++) {
        for (int j=0; j<col; j++) {
            valor = Tabela[i][j];
            std::cout << valor << "\t\t"; 
        }
        std::cout << "\n";
    }
}
