# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_count_harvest_recursive.py                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: diosoare <diosoare@student.42lisboa.com    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/02/24 03:20:32 by diosoare          #+#    #+#              #
#    Updated: 2026/02/24 03:29:25 by diosoare         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def	ft_count_harvest_recursive(count):
	if count > 5:
		print("Ready to harvest!")
	else:
		print(count)
		ft_count_harvest_recursive(count + 1)
