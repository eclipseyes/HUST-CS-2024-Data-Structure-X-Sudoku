// cnf_parser.c

#include "head.h"

// 数据结构的定义
typedef struct bool_element
{
    int name;                  // 元素的名称（文字的编号）
    bool sts;                  // 元素的状态：true 或 false
    struct bool_element *next; // 指向下一个文字的指针
    bool lock;                 // 是否已锁定
    bool back;                 // 是否在判定列表中
} bool_element;

typedef struct clause_line
{
    bool_element *c_element;  // 当前文字
    bool c_element_head;      // 文字的头是“是”或“非”
    bool exit;                // 判断文字在子句中是否存在
    struct clause_line *next; // 指向子句中下一个文字
} clause_line;

typedef struct clause_root
{
    clause_line *root;             // 指向子句链表的头
    bool exit;                     // 判断子句是否存在
    struct clause_root *next_root; // 指向下一个子句
} clause_root;

// 函数声明和定义

// 初始化新子句
clause_root *create_clause()
{
    clause_root *new_clause = (clause_root *)malloc(sizeof(clause_root));
    new_clause->root = NULL;
    new_clause->next_root = NULL;
    new_clause->exit = true;
    return new_clause;
}

// 添加文字到子句
void add_literal_to_clause(clause_root *clause, int literal_name, bool is_positive)
{
    clause_line *new_line = (clause_line *)malloc(sizeof(clause_line));
    new_line->c_element = (bool_element *)malloc(sizeof(bool_element));
    new_line->c_element->name = literal_name;
    new_line->c_element->sts = is_positive;
    new_line->c_element->next = NULL;
    new_line->c_element->lock = false;
    new_line->c_element->back = false;
    new_line->c_element_head = is_positive;
    new_line->exit = true;
    new_line->next = NULL;

    if (clause->root == NULL)
    {
        clause->root = new_line;
    }
    else
    {
        clause_line *current = clause->root;
        while (current->next != NULL)
        {
            current = current->next;
        }
        current->next = new_line;
    }
}

// 添加子句到公式
void add_clause_to_cnf(clause_root **cnf, clause_root *new_clause)
{
    if (*cnf == NULL)
    {
        *cnf = new_clause;
    }
    else
    {
        clause_root *current = *cnf;
        while (current->next_root != NULL)
        {
            current = current->next_root;
        }
        current->next_root = new_clause;
    }
}

// 读取 CNF 文件并解析为内部数据结构
clause_root *read_cnf_file(const char *filepath)
{
    FILE *file = fopen(filepath, "r"); // 打开文件进行读取
    if (!file)
    {
        printf("Cannot open the file %s\n", filepath);
        return NULL;
    }

    clause_root *cnf = NULL; // CNF公式链表的头

    char line[1024];
    while (fgets(line, sizeof(line), file))
    {
        if (line[0] == 'c' || line[0] == 'p')
        {
            continue; // 跳过注释和文件信息行
        }

        clause_root *new_clause = create_clause(); // 创建一个新的子句
        char *token = strtok(line, " ");
        while (token)
        {
            int lit = atoi(token);
            if (lit == 0)
                break; // 子句结束
            add_literal_to_clause(new_clause, abs(lit), lit > 0);

            token = strtok(NULL, " ");
        }

        add_clause_to_cnf(&cnf, new_clause); // 添加子句到CNF公式
    }

    fclose(file);
    return cnf;
}

// 打印 CNF 公式
void clause_print(clause_root *root, FILE *output_file)
{
    clause_root *current = root;
    while (current)
    {
        clause_line *line = current->root;
        while (line)
        {
            fprintf(output_file, "%s%d ", line->c_element_head ? "" : "-", line->c_element->name);
            line = line->next;
        }
        fprintf(output_file, "0\n");
        current = current->next_root;
    }
}

// 主程序
int main(int argc, char *argv[])
{
    if (argc != 3)
    {
        fprintf(stderr, "usage: %s <cnf file path> <output file path>\n", argv[0]);
        return 1;
    }

    const char *cnf_path = argv[1];
    const char *output_path = argv[2];

    clause_root *cnf = read_cnf_file(cnf_path);
    if (!cnf)
    {
        return 1;
    }

    FILE *output_file = fopen(output_path, "w"); // 使用UTF-8编码打开输出文件
    if (!output_file)
    {
        fprintf(stderr, "cannot open the output file: %s\n", output_path);
        return 1;
    }

    clause_print(cnf, output_file);

    fclose(output_file);
    return 0;
}
