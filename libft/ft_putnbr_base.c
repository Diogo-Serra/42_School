/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_putnbr_base.c                                   :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: diosoare <diosoare@student.42lisboa.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/22 07:39:33 by diosoare          #+#    #+#             */
/*   Updated: 2025/11/22 20:16:00 by diosoare         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

int	ft_putnbr_base(long n, const char *digits)
{
	char			arr[12];
	unsigned long	nb;
	int				i;
	int				count;
	int				base;

	nb = (unsigned long)n;
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
