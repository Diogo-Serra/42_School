/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_itoa_base.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: diosoare <diosoare@student.42lisboa.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/22 07:12:49 by diosoare          #+#    #+#             */
/*   Updated: 2025/11/22 07:24:45 by diosoare         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

char	*ft_itoa_base(long n, int base, const char *digits)
{
	char			arr[33];
	char			*out;
	unsigned long	nb;
	int				i;

	nb = (unsigned long)n;
	if (n < 0 && base == 10)
		nb = -n;
	i = 32;
	if (nb == 0)
		arr[--i] = '0';
	while (nb)
	{
		arr[--i] = digits[nb % base];
		nb /= base;
	}
	if (n < 0 && base == 10)
		arr[--i] = '-';
	out = (char *)ft_calloc((32 - i) + 1, sizeof(char));
	if (!out)
		return (NULL);
	ft_memcpy(out, arr + i, 32 - i);
	return (out);
}
