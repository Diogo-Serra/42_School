/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memccpy.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: diserra <diserra@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/09/07 17:17:14 by diserra           #+#    #+#             */
/*   Updated: 2025/09/07 17:41:55 by diserra          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	*ft_memccpy(void *dest, const void *src, int c, size_t n)
{
	unsigned char	*d;
	unsigned char	*s;
	unsigned char	ch;
	size_t			i;

	d = (unsigned char *) dest;
	s = (unsigned char *) src;
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
