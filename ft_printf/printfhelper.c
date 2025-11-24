/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   printfhelper.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: diosoare <diosoare@student.42lisboa.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/22 06:01:09 by diosoare          #+#    #+#             */
/*   Updated: 2025/11/24 20:38:26 by diosoare         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

int	ft_putnbr_base(long n, const char *digits, int base)
{
	char			arr[12];
	int				count;
	long			nb;
	int				i;

	nb = n;
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
