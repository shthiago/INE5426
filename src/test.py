from compiler.gci.CC20202_gci import gen_code


input = '''
def func1(int A, int B)
{
  int SM[2];
  SM[0] = A + B;
  SM[1] = B * C;

  int i;
  return;
}

def principal()
{
  int C;
  int D;
  int R;
  C = 4;
  D = 5;
  R = func1(C, D);
  return;
}
'''

print(gen_code(input))
