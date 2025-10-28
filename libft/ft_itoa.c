/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_itoa.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: diosoare <diosoare@student.42lisboa.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/28 13:17:31 by diosoare          #+#    #+#             */
/*   Updated: 2025/10/28 14:02:38 by diosoare         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

char	*ft_itoa(int n)
{
	char	arr[11];
	char	*out;
	long	nb;
	int		i;

	nb = (long)n;
	i = 10;
	if (nb < 0)
		nb *= -1;
	if (nb == 0)
		arr[--i] = '0';
	while (nb)
	{
		arr[--i] = (nb % 10) + '0';
		nb /= 10;
	}
	if (n < 0)
		arr[--i] = '-';
	out = ft_calloc((10 - i) + 1, sizeof(char));
	if (!out)
		return (NULL);
	ft_memcpy(out, arr + i, 10 - i);
	return (out);
}
