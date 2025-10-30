/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_atoi.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: diosoare <diosoare@student.42lisboa.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/16 08:24:43 by diosoare          #+#    #+#             */
/*   Updated: 2025/10/30 00:43:41 by diosoare         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

int	ft_atoi(const char *s)
{
	int	number;
	int	sign;

	number = 0;
	sign = 1;
	while ((*s == 32) || (*s >= 9 && *s <= 13))
		s++;
	if (*s == '-' || *s == '+')
	{
		if (*s++ == '-')
			sign *= -1;
	}
	while (*s >= '0' && *s <= '9')
		number = (number * 10) + (*s++ - '0');
	return (number * sign);
}
