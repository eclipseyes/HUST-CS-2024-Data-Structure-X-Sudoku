//cnf_to_grid.c

#include "head.h"

// 初始化数独网格
void initializeGrid(int grid[N][N])
{
    for (int i = 0; i < N; i++)
        for (int j = 0; j < N; j++)
            grid[i][j] = 0;
}

// 从CNF文件读取并转换为数独网格
int readCNFToGrid(const char *cnfFile, int grid[N][N])
{
    FILE *file = fopen(cnfFile, "r");
    if (!file)
    {
        fprintf(stderr, "Error opening CNF file: %s\n", cnfFile);
        return 1;
    }

    char line[256];
    while (fgets(line, sizeof(line), file))
    {
        if (line[0] == 'c' || line[0] == 'p')
            continue; // 跳过注释和头信息行

        int lit;
        sscanf(line, "%d", &lit);

        if (lit > 0)
        { // 确保是正文字
            int row = (lit / 100) - 1;
            int col = ((lit / 10) % 10) - 1;
            int num = (lit % 10);
            grid[row][col] = num;
        }
    }

    fclose(file);
    return 0;
}

// 打印数独网格到文件
void printGridToFile(int grid[N][N], const char *outputFile)
{
    FILE *file = fopen(outputFile, "w");
    if (!file)
    {
        fprintf(stderr, "Error creating output file: %s\n", outputFile);
        return;
    }

    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
        {
            if (grid[i][j] == 0)
                fprintf(file, "0 ");
            else
                fprintf(file, "%d ", grid[i][j]);
        }
        fprintf(file, "\n");
    }

    fclose(file);
}

int main(int argc, char *argv[])
{
    if (argc != 3)
    {
        fprintf(stderr, "Usage: %s <input_file.cnf> <output_file.txt>\n", argv[0]);
        return 1;
    }

    const char *cnfFile = argv[1];
    const char *outputFile = argv[2];
    int grid[N][N];

    initializeGrid(grid);

    if (readCNFToGrid(cnfFile, grid) != 0)
    {
        return 1;
    }

    printGridToFile(grid, outputFile);
    printf("Puzzle parsed and grid generated, saved to: %s\n", outputFile);

    return 0;
}
