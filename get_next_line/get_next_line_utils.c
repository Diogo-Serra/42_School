/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line_utils.c                              :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: diosoare <diosoare@student.42lisboa.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/08 19:26:34 by diosoare          #+#    #+#             */
/*   Updated: 2025/11/09 00:29:52 by diosoare         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "get_next_line.h"

size_t	ft_strlen(const char *s)
{
	size_t	len;

	len = 0;
	while (s[len])
		len++;
	return (len);
}

char	*ft_strchr(const char *s, int c)
{
    if (!s)
    {
        return (NULL);
	}
    while (*s)
	{
		if (*s == (char)c)
			return ((char *)s);
		s++;
	}
	if ((char)c == '\0')
		return ((char *)s);
	return (NULL);
}

char	*ft_strjoin(char const *s1, char const *s2)
{
	size_t	len1;
	size_t	len2;
	char	*out;

	if (!s1 || !s2)
		return (NULL);
	len1 = ft_strlen(s1);
	len2 = ft_strlen(s2);
	out = (char *)ft_calloc(len1 + len2 + 1, sizeof(char));
	if (!out)
		return (NULL);
	ft_memcpy(out, s1, len1);
	ft_memcpy(out + len1, s2, len2);
	return (out);
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

char	*ft_substr(char const *s, unsigned int start, size_t len)
{
	char	*out;
	size_t	slen;
	size_t	n;

	if (!s)
		return (NULL);
	slen = ft_strlen(s);
	if (start >= slen)
		n = 0;
	else if (len > slen - start)
		n = slen - start;
	else
		n = len;
	out = (char *)ft_calloc(n + 1, sizeof(char));
	if (!out)
		return (NULL);
	ft_memcpy(out, s + start, n);
	return (out);
}

void	*ft_calloc(size_t nmemb, size_t size)
{
	void	*ptr;
	size_t	total;

	if (size != 0 && nmemb > SIZE_MAX / size)
		return (NULL);
	total = nmemb * size;
	ptr = malloc(total);
	if (!ptr)
		return (NULL);
	if (total)
		ft_bzero(ptr, total);
	return (ptr);
}

void	ft_bzero(void *s, size_t n)
{
	unsigned char	*p;
	size_t			i;

	p = (unsigned char *)s;
	i = 0;
	while (i < n)
	{
		p[i] = 0;
		i++;
	}
}

char	*ft_strdup(const char *s)
{
	char	*dup;
	size_t	lensrc;

	lensrc = ft_strlen(s);
	dup = (char *)ft_calloc(lensrc + 1, sizeof(char));
	if (!dup)
		return (NULL);
	ft_memcpy(dup, s, lensrc);
	return (dup);
}
