/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   printfhelper.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: diosoare <diosoare@student.42lisboa.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/22 06:01:09 by diosoare          #+#    #+#             */
/*   Updated: 2025/11/24 14:18:26 by diosoare         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

size_t	ft_strlen(const char *s)
{
	size_t	i;

	i = 0;
	while (s[i])
		i++;
	return (i);
}

int	ft_putnbr_base(long n, const char *digits)
{
	char			arr[12];
	long			nb;
	int				i;
	int				count;
	int				base;

	nb = n;
	base = ft_strlen(digits);
	if (n < 0 && base == 10)
		nb = -n;
	i = 11;
	if (nb == 0)
		arr[--i] = '0';
	while (nb)
	{
		arr[--i] = digits[nb % base];
		nb /= base;
	}
	if (n < 0 && base == 10)
		arr[--i] = '-';
	count = 11 - i;
	write(1, arr + i, count);
	return (count);
}
