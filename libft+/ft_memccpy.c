/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memccpy.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: diosoare <diosoare@student.42lisboa.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/16 08:30:57 by diosoare          #+#    #+#             */
/*   Updated: 2025/10/16 08:31:00 by diosoare         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	*ft_memccpy(void *dst, const void *src, int c, size_t n)
{
	unsigned char	*d;
	unsigned char	*s;
	unsigned char	ch;
	size_t			i;

	d = (unsigned char *)dst;
	s = (unsigned char *)src;
	ch = (unsigned char) c;
	i = 0;
	while (i < n)
	{
		d[i] = s[i];
		if (s[i] == ch)
			return ((void *)&d[i + 1]);
		i++;
	}
	return (NULL);
}
