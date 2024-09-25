#ifndef HEAD_H
#define HEAD_H

#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

// 定义状态类型
typedef int status;

#define OK 1
#define ERROR 0
#define FOUND 1
#define NOTFOUND 0
#define UNASSIGNED 0
#define YES 1
#define NO 0
#define N 9 // 数独的大小

// 定义数据结构
typedef struct LiteralNode
{
    int data;
    struct LiteralNode *right;
} LiteralNode;

typedef struct ClauseNode
{
    struct LiteralNode *right;
    struct ClauseNode *down;
} ClauseNode;

// 函数声明
ClauseNode *AddClause(ClauseNode *s, int var);
ClauseNode *IsUnitClause(ClauseNode *s);
ClauseNode *CopyS(ClauseNode *s);
ClauseNode *CopyClause(ClauseNode *s);
ClauseNode *DeleteClause(ClauseNode *s);
ClauseNode *DeleteLiteral(ClauseNode *s, int var);
status Print(ClauseNode *s);
status IsEmptyClause(ClauseNode *s);
status RecordTruth(ClauseNode *s, int *truth_table);
status RemoveVar(ClauseNode *s, int var);
int PickVar(ClauseNode *s);
ClauseNode *CnfParser(int *literal_num, char *filename, int *max_var);
int PickVar_1(ClauseNode *s);
int PickVar_2(ClauseNode *s);
int PickVar_3(ClauseNode *s);

#endif // HEAD_H
