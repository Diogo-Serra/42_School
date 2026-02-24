# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_plant_age.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: diosoare <diosoare@student.42lisboa.com    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/02/24 03:04:42 by diosoare          #+#    #+#              #
#    Updated: 2026/02/24 03:09:14 by diosoare         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def	ft_plant_age():
	age = int(input("Enter plant's age: "))
	if age <= 60:
		print("Plant needs more time to grow.")
	else:
		print("Plant is ready to harvest.")

ft_plant_age()