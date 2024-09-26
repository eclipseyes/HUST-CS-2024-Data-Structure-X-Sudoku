// cnf_parser.c

#include "head.h"

// 解析 CNF 文件
ClauseNode *CnfParser(int *literal_num, const char *filename, int *max_var)
{
    FILE *file = fopen(filename, "r");
    if (!file)
    {
        printf("Error opening file: %s\n", filename);
        return NULL;
    }

    ClauseNode *cnf = (ClauseNode *)malloc(sizeof(ClauseNode));
    cnf->down = NULL;
    cnf->right = NULL;
    ClauseNode *cnf_tail = cnf; // 尾指针，保持对最后一个子句的引用
    *max_var = 0;

    char line[11000];
    while (fgets(line, sizeof(line), file))
    {
        if (line[0] == 'c' || line[0] == 'p') // 跳过注释和头信息
        {
            continue;
        }

        ClauseNode *new_clause = (ClauseNode *)malloc(sizeof(ClauseNode));
        new_clause->down = NULL;
        new_clause->right = NULL;
        LiteralNode *literal_tail = NULL; // 文字链表的尾指针

        char *token = strtok(line, " ");
        while (token)
        {
            int lit = atoi(token);
            if (lit == 0)
                break; // 结束符为0
            if (abs(lit) > *max_var)
                *max_var = abs(lit); // 更新最大变元编号

            LiteralNode *literal = (LiteralNode *)malloc(sizeof(LiteralNode));
            literal->data = lit;
            literal->right = NULL; // 新的文字节点的next为NULL

            // 将新文字插入到子句链表的尾部
            if (new_clause->right == NULL)
            {
                new_clause->right = literal;
                literal_tail = literal; // 初始化尾指针
            }
            else
            {
                literal_tail->right = literal;
                literal_tail = literal; // 更新尾指针
            }

            token = strtok(NULL, " ");
        }

        // 将新子句插入到CNF链表的尾部
        cnf_tail->down = new_clause;
        cnf_tail = new_clause;
    }

    fclose(file);
    return cnf;
}

// 打印 CNF 公式
void clause_print(ClauseNode *root, FILE *output_file)
{
    ClauseNode *current_clause = root->down; // 跳过头结点
    while (current_clause)
    {
        LiteralNode *literal = current_clause->right;
        while (literal)
        {
            fprintf(output_file, "%d ", literal->data);
            literal = literal->right;
        }
        fprintf(output_file, "0\n"); // 每个子句结束以0结尾
        current_clause = current_clause->down;
    }
}

// 主程序
int main(int argc, char *argv[])
{
    if (argc != 3)
    {
        fprintf(stderr, "Usage: %s <cnf file path> <output file path>\n", argv[0]);
        return 1;
    }

    const char *cnf_path = argv[1];
    const char *output_path = argv[2];
    int literal_num = 0;
    int max_var = 0;

    // 解析 CNF 文件
    ClauseNode *cnf = CnfParser(&literal_num, cnf_path, &max_var);
    if (!cnf)
    {
        return 1;
    }

    // 打印 CNF 公式到输出文件
    FILE *output_file = fopen(output_path, "w");
    if (!output_file)
    {
        fprintf(stderr, "Cannot open the output file: %s\n", output_path);
        return 1;
    }

    clause_print(cnf, output_file);
    fclose(output_file);
    return 0;
}
