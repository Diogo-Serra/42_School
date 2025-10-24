/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_itoa.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: diosoare <diosoare@student.42lisboa.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/16 08:28:32 by diosoare          #+#    #+#             */
/*   Updated: 2025/10/24 14:22:09 by diosoare         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

static int	get_len(int n)
{
	int	len;

	len = 0;
	if (n <= 0)
		len++;
	while (n != 0)
	{
		n = n / 10;
		len++;
	}
	return (len);
}

char	*ft_itoa(int n)
{
	char	*out;
	int		len;
	long	nb;

	nb = n;
	len = get_len(nb);
	out = (char *)malloc(sizeof(char) * (len + 1));
	if (!out)
		return (NULL);
	out[len] = '\0';
	len--;
	if (nb == 0)
		out[0] = '0';
	if (nb < 0)
	{
		out[0] = '-';
		nb = -nb;
	}
	while (nb > 0)
	{
		out[len] = (nb % 10) + '0';
		nb = nb / 10;
		len--;
	}
	return (out);
}
