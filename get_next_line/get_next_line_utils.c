/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line_utils.c                              :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: diosoare <diosoare@student.42lisboa.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/08 19:26:34 by diosoare          #+#    #+#             */
/*   Updated: 2025/11/08 22:52:07 by diosoare         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "get_next_line.h"

size_t	ft_strnlen(const char *s)
{
	size_t	i;

	i = 0;
	while (s[i] != '\n')
		i++;
	return (i);
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
