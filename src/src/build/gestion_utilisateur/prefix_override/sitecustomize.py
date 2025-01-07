import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/codespace/ros2_ws/src/src/install/gestion_utilisateur'
