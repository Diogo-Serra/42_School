/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_putnbr_base.c                                   :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: diosoare <diosoare@student.42lisboa.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/22 07:39:33 by diosoare          #+#    #+#             */
/*   Updated: 2025/11/23 16:10:16 by diosoare         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

int	ft_putnbr_base(long n, const char *digits)
{
	char			arr[65];
	long			nb;
	int				i;
	int				count;
	int				base;

	nb = n;
	base = (int)ft_strlen(digits);
	if (n < 0 && base == 10)
		nb = -n;
	i = 64;
	if (nb == 0)
		arr[--i] = '0';
	while (nb)
	{
		arr[--i] = digits[nb % base];
		nb /= base;
	}
	if (n < 0 && base == 10)
		arr[--i] = '-';
	count = 64 - i;
	write(1, arr + i, count);
	return (count);
}
