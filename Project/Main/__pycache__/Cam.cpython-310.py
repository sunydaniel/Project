o
    �$�cG  �                   @   s"   d dl Zd dlT G dd� d�ZdS )�    N)�*c                   @   s,   e Zd Zdd� Zdd� Zdd� Zdd� Zd	S )
�Camerac                 C   sz   || _ t�g |�d��| _t�g d��| _t�g d��| _t�g d��| _tjd | _	| j	|j
|j  | _d| _d| _d S )Ng      �?)r   r   �   r   �r   r   r   r   )r   r   r   r   �   g�������?�d   )�render�np�array�position�forward�up�right�math�piZh_fov�HEIGHT�WIDTHZv_fovZ
near_planeZ	far_plane)�selfr   r   � r   �=   c:\Users\Даниил\Desktop\Псевдо дум\Main\Cam.py�__init__   s   
zCamera.__init__c              	   C   s:   | j \}}}}t�g d�g d�g d�| | | dgg�S )N)r   r   r   r   r   )r   r   r   r   r   )r   r	   r
   )r   �x�y�z�wr   r   r   �translate_matrix   s   �zCamera.translate_matrixc                 C   sX   | j \}}}}| j\}}}}| j\}}	}
}t�|||dg||	|dg||
|dgg d�g�S )Nr   )r   r   r   r   )r   r   r   r	   r
   )r   ZrxZryZrzr   ZfxZfyZfzZuxZuyZuzr   r   r   �rotate_matrix   s   


�zCamera.rotate_matrixc                 C   s   | � � | ��  S )N)r   r   )r   r   r   r   �camera_matrix"   s   zCamera.camera_matrixN)�__name__�
__module__�__qualname__r   r   r   r   r   r   r   r   r      s
    
r   )�pygame�pg�matrix_functionsr   r   r   r   r   �<module>   s    