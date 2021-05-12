from compiler.gci.CC20202_gci import gen_code


input = '''
{
    int i;
    int a;
    i = 1;
    a = 0;
    if (a < i) {
        a = i;
    } else {
        a = 0;
    }
}
'''

print(gen_code(input))
