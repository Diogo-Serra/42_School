/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_atoi.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: diosoare <diosoare@student.42lisboa.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/16 08:24:43 by diosoare          #+#    #+#             */
/*   Updated: 2025/10/23 19:49:14 by diosoare         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

int	better_atoi(const char *s)
{
	int	res;
	int	sgn;

	sgn = 1;
	res = 0;
	while ((*s == ' ') || (*s >= 9 && *s <= 13))
		s++;
	if (*s == '+' || *s++ == '-')
		sgn = (*(s - 1) == '+') - (*(s - 1) == '-');
	while (*s >= '0' && *s <= '9')
		res = (res * 10) + (*s++ - '0');
	return (res * sgn);
}

int	ft_atoi(const char *s)
{
	long	res;
	int		sign;

	sign = 1;
	res = 0;
	while ((*s == ' ') || (*s >= 9 && *s <= 13))
		s++;
	if (*s == '-' || *s == '+')
	{
		if (*s++ == '-')
			sign = -sign;
	}
	while (*s >= '0' && *s <= '9')
		res = (res * 10) + (*s++ - '0');
	return ((int)(res * sign));
}
