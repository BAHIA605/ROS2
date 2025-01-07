from setuptools import setup

package_name = 'localisation_librairie'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/ament_package',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='VotreNom',
    maintainer_email='votreemail@exemple.com',
    description='Votre description du package',
    license='Propriétaire',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'book_database = localisation_librairie.book_database:main',  # Assurez-vous que le fichier book_database.py a aussi une fonction main
            'request_manager = localisation_librairie.request_manager:main',  # Lien vers la fonction main dans request_manager.py
        ],
    },
)

