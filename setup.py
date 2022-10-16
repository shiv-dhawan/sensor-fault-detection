from setuptools import find_packages,setup

def get_requirements()->'list[str]':
    '''
    This function will returns a list of requirements
    '''
    requirement_list:list[str] = []
    return requirement_list


setup(
    name = 'sensor',
    version = '0.0.1',
    author = 'shivanshu',
    author_email='shividhawan114@gmail.com',
    packages= find_packages(),
    install_requires = get_requirements()
)