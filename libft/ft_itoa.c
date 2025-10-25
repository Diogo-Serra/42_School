/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_itoa.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: diosoare <diosoare@student.42lisboa.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/16 08:28:32 by diosoare          #+#    #+#             */
/*   Updated: 2025/10/26 00:22:19 by diosoare         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

char	*ft_itoa(int n)
{
	char	arr[12];
	char	*out;
	long	nb;
	int		i;

	nb = n;
	i = sizeof(arr) - 1;
	if (nb == 0)
		arr[--i] = '0';
	if (n < 0)
		nb *= -1;
	while (nb)
	{
		arr[--i] = (nb % 10) + '0';
		nb /= 10;
	}
	if (n < 0)
		arr[--i] = '-';
	out = (char *)ft_calloc((sizeof(arr) - i) + 1, sizeof(char));
	if (!out)
		return (NULL);
	ft_memcpy(out, arr + i, sizeof(arr) - i);
	return (out);
}
