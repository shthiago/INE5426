from compiler.gci.CC20202_gci import gen_code


input = '''
{
    int i;
    int a;
    a = 0;
    for (i = 0; i < 10; i = i + 1) {
        a = a + i;
    }
}
'''

print(gen_code(input))
