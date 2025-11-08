/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line_utils.c                              :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: diosoare <diosoare@student.42lisboa.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/08 19:26:34 by diosoare          #+#    #+#             */
/*   Updated: 2025/11/08 23:18:30 by diosoare         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "get_next_line.h"

char	*ft_strdup(const char *s)
{
	char	*dup;
	size_t	lensrc;

	lensrc = 0;
    while (s[lensrc])
    {
        lensrc++;
    }
    dup = (char *)ft_calloc(lensrc + 1, sizeof(char));
	if (!dup)
		return (NULL);
	ft_memcpy(dup, s, lensrc);
	return (dup);
}

size_t	ft_strnlen(const char *s)
{
	size_t	i;

	i = 0;
	while (s[i] != '\n')
		i++;
	return (i);
}


void	*ft_memchr(const void *s, int c, size_t n)
{
	const unsigned char		*p;
	unsigned char			uc;

	p = (const unsigned char *)s;
	uc = (unsigned char)c;
	while (n--)
	{
		if (*p == uc)
			return ((void *)p);
		p++;
	}
	return (NULL);
}

void	*ft_calloc(size_t nmemb, size_t size)
{
    size_t  i;
	size_t	total;
    char	*ptr;

    if (size != 0 && nmemb > SIZE_MAX / size)
		return (NULL);
	total = nmemb * size;
	ptr = malloc(total);
	if (!ptr)
		return (NULL);
	i = 0;
    while (i < total)
    {
        ptr[i++] = 0;
    }
    return (ptr);
}

void	*ft_memcpy(void *dst, const void *src, size_t n)
{
	unsigned char			*d;
	const unsigned char		*s;

	d = (unsigned char *)dst;
	s = (const unsigned char *)src;
	while (n--)
		*d++ = *s++;
	return (dst);
}
