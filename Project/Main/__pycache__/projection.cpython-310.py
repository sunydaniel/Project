o
    %�cd  �                   @   s"   d dl Z d dlZG dd� d�ZdS )�    Nc                   @   s   e Zd Zdd� ZdS )�
Projectionc              	   C   s�   |j j}|j j}t�|j jd �}| }t�|j jd �}| }d||  }d||  }	|| ||  }
d| | ||  }t�|dddgd|	ddgdd|
dgdd|dgg�| _	|j
|j}}t�|dddgd| ddgg d�||ddgg�| _d S )N�   �����r   �   )r   r   r   r   )�camera�
near_plane�	far_plane�math�tan�h_fov�v_fov�np�array�projection_matrix�H_WIDTH�H_HEIGHT�to_screen_matrix)�self�renderZNEARZFARZRIGHTZLEFTZTOPZBOTTOMZm00Zm11Zm22Zm32ZHWZHH� r   �D   c:\Users\Даниил\Desktop\Псевдо дум\Main\projection.py�__init__   s.   



�

�zProjection.__init__N)�__name__�
__module__�__qualname__r   r   r   r   r   r      s    r   )r	   �numpyr   r   r   r   r   r   �<module>   s    