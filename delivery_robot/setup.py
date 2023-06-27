from setuptools import setup
import os
from glob import glob
package_name = 'delivery_robot'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share',package_name,'launch'),  glob('launch/*')),
        (os.path.join('share',package_name,'config'), glob('config/*')),
        (os.path.join('share',package_name,'world/maze'), glob('world/maze/*')),
        (os.path.join('share',package_name,'models/table'), glob('models/table/*')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='dinakar',
    maintainer_email='dinakar@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'occupancy_grid_pub = delivery_robot.occupancy_grid_pub:main',
            'sdf_spawner = delivery_robot.spawn_entity:main',
            'maze_solver = delivery_robot.maze_solver:main',
            'delivery_waiter_lite = delivery_robot.hotel_waiter_single_button:start_app',
            'delivery_waiter = delivery_robot.hotel_waiter_multi_button:start_app'

        ],
    },
)
