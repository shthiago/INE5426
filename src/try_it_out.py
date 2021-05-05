from compiler.semantic.CC20202_semantic import parse

with open('../examples/exemplo2.ccc') as f:
    text = f.read()

parse(text)
