from setuptools import setup

setup(
    name='Huggingface Deduplication',
    version='0.1.0',
    url='https://github.com/AlekseyKorshuk/Huggingface-deduplicate',
    license='GPL-3.0',
    author='AlekseyKorshuk',
    author_email='ale-kor02@mail.ru',
    description='Huggingface Deduplication',
    install_requires=['datasets>=2.10.1', 'datasketch==1.5.7', 'dpu_utils==0.6.1', 'tqdm>=4.65.0'],
)
