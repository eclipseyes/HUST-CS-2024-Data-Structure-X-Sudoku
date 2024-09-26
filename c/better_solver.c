// better_solver.c

#include "head.h"

// 修改后的 DPLL 求解器
status DpllSolver(ClauseNode *s, int *truth_table, int pickvar_choice)
{
    ClauseNode *s_tmp = s;
    ClauseNode *unit_clause = IsUnitClause(s_tmp);

    while (unit_clause)
    {
        RecordTruth(unit_clause, truth_table);
        int var = unit_clause->right->data;
        RemoveVar(s, var);

        if (s->down == NULL)
            return FOUND;
        else if (IsEmptyClause(s))
            return NOTFOUND;

        s_tmp = s;
        unit_clause = IsUnitClause(s_tmp);
    }

    // 根据参数选择不同的 PickVar 函数
    int var;
    if (pickvar_choice == 1)
        var = PickVar_1(s);
    else if (pickvar_choice == 2)
        var = PickVar_2(s);
    else
        var = PickVar_3(s);

    if (DpllSolver(AddClause(CopyS(s), var), truth_table, pickvar_choice))
        return FOUND;
    return DpllSolver(AddClause(s, -var), truth_table, pickvar_choice);
}

// 添加子句到子句集
ClauseNode *AddClause(ClauseNode *s, int var)
{
    ClauseNode *c_tmp = (ClauseNode *)malloc(sizeof(ClauseNode));
    c_tmp->right = (LiteralNode *)malloc(sizeof(LiteralNode));
    c_tmp->right->data = var;
    c_tmp->right->right = NULL;
    c_tmp->down = s->down;
    s->down = c_tmp;
    return s;
}

// 判断是否存在单子句
ClauseNode *IsUnitClause(ClauseNode *s)
{
    ClauseNode *c_tmp = s;
    while (c_tmp)
    {
        if (c_tmp->right && !c_tmp->right->right)
            return c_tmp;
        c_tmp = c_tmp->down;
    }
    return NULL;
}

// 复制子句集
ClauseNode *CopyS(ClauseNode *s)
{
    ClauseNode *s_new, *c_tmp, *s_origin = s->down;
    s_new = (ClauseNode *)malloc(sizeof(ClauseNode));
    s_new->right = NULL;
    c_tmp = s_new;

    while (s_origin)
    {
        c_tmp->down = CopyClause(s_origin);
        c_tmp = c_tmp->down;
        s_origin = s_origin->down;
    }
    return s_new;
}

// 复制单个子句
ClauseNode *CopyClause(ClauseNode *s)
{
    ClauseNode *clause_tmp = (ClauseNode *)malloc(sizeof(ClauseNode));
    LiteralNode *literal_tmp, *s_tmp = s->right;

    clause_tmp->down = NULL;
    clause_tmp->right = NULL;

    if (s_tmp)
    {
        literal_tmp = (LiteralNode *)malloc(sizeof(LiteralNode));
        literal_tmp->data = s_tmp->data;
        literal_tmp->right = NULL;
        s_tmp = s_tmp->right;
        clause_tmp->right = literal_tmp;
    }

    while (s_tmp)
    {
        literal_tmp->right = (LiteralNode *)malloc(sizeof(LiteralNode));
        literal_tmp->right->data = s_tmp->data;
        literal_tmp->right->right = NULL;
        literal_tmp = literal_tmp->right;
        s_tmp = s_tmp->right;
    }
    return clause_tmp;
}

// 删除子句
ClauseNode *DeleteClause(ClauseNode *s)
{
    ClauseNode *c_tmp = s;
    LiteralNode *l;
    while (s->right)
    {
        l = s->right;
        s->right = s->right->right;
        free(l);
    }
    s = s->down;
    free(c_tmp);
    return s;
}

// 删除负变元
ClauseNode *DeleteLiteral(ClauseNode *s, int var)
{
    LiteralNode *l = s->right, *l_tmp;

    if (l->data == -var)
    {
        l_tmp = s->right->right;
        free(l);
        s->right = l_tmp;
        return s;
    }
    else if (l->data == var)
    {
        return NULL;
    }

    while (l)
    {
        if (l->right && l->right->data == -var)
        {
            l_tmp = l->right;
            l->right = l->right->right;
            free(l_tmp);
        }
        else if (l->right && l->right->data == var)
        {
            return NULL;
        }
        l = l->right;
    }
    return s;
}

// 判断是否存在空子句
status IsEmptyClause(ClauseNode *s)
{
    ClauseNode *c_tmp = s->down;
    while (c_tmp)
    {
        if (!c_tmp->right)
            return YES;
        c_tmp = c_tmp->down;
    }
    return NO;
}

// 记录单子句中元素的真值
status RecordTruth(ClauseNode *s, int *truth_table)
{
    int idx = abs(s->right->data) - 1;
    if (s->right->data > 0)
        truth_table[idx] = 1;
    else
        truth_table[idx] = 0;
    return OK;
}

// 删除变元所在子句与负变元
status RemoveVar(ClauseNode *s, int var)
{
    ClauseNode *c_tmp = s->down, *last_c_tmp = s;
    while (c_tmp)
    {
        c_tmp = DeleteLiteral(c_tmp, var);
        if (c_tmp == NULL)
        {
            c_tmp = DeleteClause(last_c_tmp->down);
            last_c_tmp->down = c_tmp;
            continue;
        }
        if (c_tmp == NULL)
            break;
        last_c_tmp = c_tmp;
        c_tmp = c_tmp->down;
    }
    return OK;
}

int PickVar_1(ClauseNode *s) // 选择出现次数最多的变元
{
    int max_var = 0;
    ClauseNode *c_tmp = s->down;
    while (c_tmp)
    {
        LiteralNode *l_tmp = c_tmp->right;
        while (l_tmp)
        {
            if (abs(l_tmp->data) > max_var)
                max_var = abs(l_tmp->data);
            l_tmp = l_tmp->right;
        }
        c_tmp = c_tmp->down;
    }

    int *count = (int *)malloc(sizeof(int) * (2 * max_var + 1));
    for (int i = 0; i <= 2 * max_var; i++)
        count[i] = 0;

    c_tmp = s->down;
    while (c_tmp)
    {
        LiteralNode *l_tmp = c_tmp->right;
        while (l_tmp)
        {
            int lit = l_tmp->data;
            if (lit > 0)
                count[lit]++;
            else
                count[max_var - lit]++;
            l_tmp = l_tmp->right;
        }
        c_tmp = c_tmp->down;
    }

    int selected_var = 1;
    int max_count = 0;
    for (int i = 1; i <= max_var; i++)
    {
        if (count[i] > max_count)
        {
            max_count = count[i];
            selected_var = i;
        }
    }

    if (max_count == 0)
    {
        for (int i = max_var + 1; i <= 2 * max_var; i++)
        {
            if (count[i] > max_count)
            {
                max_count = count[i];
                selected_var = max_var - i;
            }
        }
    }

    free(count);
    return selected_var;
}

int PickVar_2(ClauseNode *s) // 选择下一个变元
{
    int var = s->down->right->data;
    return var;
}

int PickVar_3(ClauseNode *s) // 为所在子句较短的变元分配较大权重
{
    int max_var = 0;
    ClauseNode *c_tmp = s->down;
    while (c_tmp)
    {
        LiteralNode *l_tmp = c_tmp->right;
        while (l_tmp)
        {
            if (abs(l_tmp->data) > max_var)
                max_var = abs(l_tmp->data);
            l_tmp = l_tmp->right;
        }
        c_tmp = c_tmp->down;
    }

    double *weight = (double *)malloc(sizeof(double) * (2 * max_var + 1));
    for (int i = 0; i <= 2 * max_var; i++)
        weight[i] = 0.0;

    c_tmp = s->down;
    while (c_tmp)
    {
        int clause_length = 0;
        LiteralNode *l_tmp = c_tmp->right;
        while (l_tmp)
        {
            clause_length++;
            l_tmp = l_tmp->right;
        }

        l_tmp = c_tmp->right;
        while (l_tmp)
        {
            int lit = l_tmp->data;
            double factor = pow(2.0, (double)(-clause_length));
            if (lit > 0)
                weight[lit] += factor;
            else
                weight[max_var - lit] += factor;
            l_tmp = l_tmp->right;
        }
        c_tmp = c_tmp->down;
    }

    double max_weight = 0.0;
    int selected_var = 1;
    for (int i = 1; i <= max_var; i++)
    {
        if (weight[i] + weight[i + max_var] > max_weight)
        {
            max_weight = weight[i] + weight[i + max_var];
            selected_var = i;
        }
    }

    if (weight[selected_var] < weight[selected_var + max_var])
        selected_var = -selected_var;

    free(weight);
    return selected_var;
}

// 打印子句集
status Print(ClauseNode *s)
{
    ClauseNode *c_tmp = s->down;
    LiteralNode *l_tmp;
    printf("\n-----Start-----\n");
    while (c_tmp)
    {
        l_tmp = c_tmp->right;
        while (l_tmp)
        {
            printf("%d ", l_tmp->data);
            l_tmp = l_tmp->right;
        }
        if (c_tmp->right)
            printf("\n");
        else
            printf("空\n");
        c_tmp = c_tmp->down;
    }
    printf("------End------\n");
    return OK;
}

// 解析 CNF 文件
ClauseNode *CnfParser(int *literal_num, char *filename, int *max_var)
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
    *max_var = 0;

    char line[11000];
    while (fgets(line, sizeof(line), file))
    {
        if (line[0] == 'c' || line[0] == 'p')
        {
            continue;
        }
        ClauseNode *new_clause = (ClauseNode *)malloc(sizeof(ClauseNode));
        new_clause->down = NULL;
        new_clause->right = NULL;

        char *token = strtok(line, " ");
        while (token)
        {
            int lit = atoi(token);
            if (lit == 0)
                break;
            if (abs(lit) > *max_var)
                *max_var = abs(lit);
            LiteralNode *literal = (LiteralNode *)malloc(sizeof(LiteralNode));
            literal->data = lit;
            literal->right = new_clause->right;
            new_clause->right = literal;

            token = strtok(NULL, " ");
        }

        new_clause->down = cnf->down;
        cnf->down = new_clause;
    }
    fclose(file);
    return cnf;
}

// 修改后的主程序入口
int main(int argc, char *argv[])
{
    if (argc != 3)
    {
        fprintf(stderr, "Usage: %s <cnf file path> <pickvar choice>\n", argv[0]);
        return 1;
    }

    char cnf_path[256];
    strcpy(cnf_path, argv[1]);
    int pickvar_choice = atoi(argv[2]);
    int truth_table[5000] = {0};
    int max_var = 0;

    ClauseNode *cnf = CnfParser(truth_table, cnf_path, &max_var);

    if (!cnf)
    {
        fprintf(stderr, "Error reading CNF file: %s\n", cnf_path);
        return 1;
    }

    clock_t start_time = clock();
    status result = DpllSolver(cnf, truth_table, pickvar_choice);
    clock_t end_time = clock();

    double elapsed_time = ((double)(end_time - start_time)) / CLOCKS_PER_SEC * 1000;

    char result_path[1024];
    snprintf(result_path, sizeof(result_path), "%s_faster.res", cnf_path);

    FILE *output_file = fopen(result_path, "w");
    if (!output_file)
    {
        fprintf(stderr, "Cannot open output file.\n");
        return 1;
    }

    if (result == FOUND)
    {
        fprintf(output_file, "s 1\nv ");
        for (int i = 0; i < max_var; i++)
        {
            if (truth_table[i] == 1)
                fprintf(output_file, "%d ", i + 1);
            else if (truth_table[i] == 0)
                fprintf(output_file, "-%d ", i + 1);
        }
        fprintf(output_file, "\n");
    }
    else
    {
        fprintf(output_file, "s 0\n");
    }

    fprintf(output_file, "t %.2f\n", elapsed_time);
    fclose(output_file);

    Print(cnf);

    return 0;
}
