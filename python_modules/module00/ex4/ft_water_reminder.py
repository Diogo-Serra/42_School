# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_water_reminder.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: diosoare <diosoare@student.42lisboa.com    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/02/24 03:10:54 by diosoare          #+#    #+#              #
#    Updated: 2026/02/24 03:29:44 by diosoare         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def	ft_water_reminder():
	days = int(input("Days since last watering: "))
	if days <= 2:
		print("Plants are fine.")
	else:
		print("Water the plants!")
