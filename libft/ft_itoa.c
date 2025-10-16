/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_itoa.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: diosoare <diosoare@student.42lisboa.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/16 08:28:32 by diosoare          #+#    #+#             */
/*   Updated: 2025/10/16 08:28:34 by diosoare         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

size_t	intlen(long n)
{
	size_t	l;

	l = (n <= 0);
	while (n)
	{
		l++;
		n /= 10;
	}
	return (l);
}

char	*ft_itoa(int n)
{
	long	nb;
	size_t	len;
	size_t	i;
	char	*s;

	nb = n;
	len = intlen(nb);
	s = (char *)malloc(len + 1);
	if (!s)
		return (NULL);
	s[len] = '\0';
	if (nb < 0)
		nb = -nb;
	i = len;
	if (nb == 0)
		s[--i] = '0';
	while (nb)
	{
		s[--i] = (char)('0' + (nb % 10));
		nb /= 10;
	}
	if (n < 0)
		s[0] = '-';
	return (s);
}
