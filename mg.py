U
    ��^�  �                   @   s�  d dl Z d dlZd dlZe�d� edd�Ze��  edd�Zdd� Zdd	� Z	e
d
� ed�Zedk�r@ed�Zz�e jed�Ze jeddd�Zzejjdd� e�d� W n   dZY nX ejjded� ejjddd�d d  d Zejjed d� edd�Ze�ed � e��  W n   e
d� Y nX e
d� e�  ned k�rXe
d!� e�  e
d"� ed�Zed k�r�e
d#� ed�Zed k�r�d$Znd%Zed�Zz2e jed�Ze jeddd�Zejjd&ded'� W n   e
d(� e�  Y nX e	� Z ed)�Z!e
d*� d Z"ed k�rVe� Zed$k�r$�q�zejje d d� W n   dZY nX e�d+� z�ejje d e!d� ed k�r�e�r�e�d,� nje�d� ejje d dd�d d  d Zejjed d� e�d-� ejj#e d d� ej�$�  e�d� W n$   ed k�rY �q�nY �qY nX e"d k�r6e
d.� e"d7 Z"nNe"dk�rRe
d/� e"d7 Z"n2e"d0k�rne
d1� e"d7 Z"ne"d2k�r�e
d3� d Z"e�d� �qe
d4� dS )5�    N�clearz.tokensza+�rc                  C   sH   t �� } | d t| �d � } | dkr(dS tj| d�}tj|ddd�S d S )N�   � T�Zaccess_token�5.89�ru��vZlang)�f�readline�len�vk�Session�API)�token�session� r   �mg.py�login   s    r   c                  C   s  d} d}d}d}d}t d�}tt|��D ]�}|| dkr@|d } || k rJq(|dkr�| dkr�z4|| dkrp|d7 }t|| � d}||| 7 }W q�   ||| 7 }Y q�X q(|dkr�|| dkr�||| 7 }q�d	}q(|d	kr(||| 7 }q(|dkr�td
� t�  |||fS )Nr   r   z[35mEnter the link: [0m�.�   �-r   �_�   z
[31mInvalid link
)�input�ranger   �int�print�quit)Zspace�step�typeZfirstIDZsecondIDZlink�charr   r   r   �getlink   s>    r#   u�  [37m
 InvertedOnes          Vk: @inverted_ones[32m
 ┏━━┳━━┳━━━━━┓  ┏━━━━━┳━━━━━┳━━━━━┳━━┳━━┓
 ┃     ┃  ┏━━┫  ┃  ━━━┫  ━  ┃  ━  ┃     ┃
 ┃ ┃ ┃ ┃  ┗  ┃  ┣━━━  ┃ ┏━━━┫     ┃ ┃ ┃ ┃
 ┗━┻━┻━┻━━━━━┛  ┗━━━━━┻━┛   ┗━━┻━━┻━┻━┻━┛
[35m
[1] Spam
[2] Add token
z&Please, enter your task's number: [0m�2z[35mEnter the token: [0mr   r   r   r	   i�ϭ)�owner_idgffffff�?Zpidor)�user_id�messager   )r&   �count�items�id)Zmessage_idsZdelete_for_all�a�
z
[31mInvalid tokenr   �1z
[31mInvalid task's number
z[35m
[1] Single
[2] Multiple
z[35m
[1] Infinitely
[2] Fast
TFi
��)r%   Zpost_idr'   z
[31mInvalid token
z[35mMessage's text:[0m z
[33mg333333�?g������@gffffff�?z[FSending                 z[FSending.                r   z[FSending..               �   z[FSending...              z&[F                                [F)%r   �time�os�system�open�w�closer   r   r#   r   r   ZtaskZtkr   r   r   ZapiZaccountZunban�sleepZyouZmessages�sendZ
getHistoryZmg_id�delete�writer   Z
infinitelyZwallZcreateCommentZ	parametrsZmessZdowZbanZ
setOffliner   r   r   r   �<module>   s�   


	"












 









