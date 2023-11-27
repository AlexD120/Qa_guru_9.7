import os

print(os.path.abspath(__file__))
print(os.path.abspath("script_open.py"))
current_file = os.path.abspath(__file__)

"""СКЛЕИТЬ ДИРЕКТОРИЮ"""
current_dir = os.path.dirname(current_file)
tmp_dir = os.path.join(current_dir, 'tmp')
print(tmp_dir)