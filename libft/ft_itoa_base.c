/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_itoa_base.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: diosoare <diosoare@student.42lisboa.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/22 07:12:49 by diosoare          #+#    #+#             */
/*   Updated: 2025/11/23 16:02:01 by diosoare         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

char	*ft_itoa_base(long n, const char *digits)
{
	char			arr[65];
	char			*out;
	long			nb;
	int				base;
	int				i;

	nb = n;
	base = ft_strlen(digits);
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
	out = (char *)ft_calloc((64 - i) + 1, sizeof(char));
	if (!out)
		return (NULL);
	ft_memcpy(out, arr + i, 64 - i);
	return (out);
}
