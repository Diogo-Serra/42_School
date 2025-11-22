/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   printfhelper.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: diosoare <diosoare@student.42lisboa.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/22 06:01:09 by diosoare          #+#    #+#             */
/*   Updated: 2025/11/22 07:30:22 by diosoare         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libftprintf.h"

size_t	ft_strlen(const char *s)
{
	size_t	i;

	i = 0;
	while (s[i])
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

void	*ft_calloc(size_t nmemb, size_t size)
{
	void	*ptr;
	char	*p;
	size_t	total;

	if (size != 0 && nmemb > SIZE_MAX / size)
		return (NULL);
	total = nmemb * size;
	ptr = malloc(total);
	if (!ptr)
		return (NULL);
	p = (char *)ptr;
	while (total--)
		*p++ = 0;
	return (ptr);
}

char	*ft_itoa_base(long n, int base, const char *digits)
{
    char			arr[12];
    char			*out;
    unsigned long	nb;
    int				i;

    nb = (unsigned long)n;
    if (n < 0 && base == 10)
        nb = -n;
    i = 11;
    if (nb == 0)
        arr[--i] = '0';
    while (nb)
    {
        arr[--i] = digits[nb % base];
        nb /= base;
    }
    if (n < 0 && base == 10)
        arr[--i] = '-';
    out = (char *)ft_calloc((11 - i) + 1, sizeof(char));
    if (!out)
        return (NULL);
    ft_memcpy(out, arr + i, 11 - i);
    return (out);
}
