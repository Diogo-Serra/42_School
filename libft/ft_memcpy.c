/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memcpy.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: diosoare <diosoare@student.42lisboa.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/16 08:31:41 by diosoare          #+#    #+#             */
/*   Updated: 2025/10/28 15:35:47 by diosoare         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"
#include <string.h>

void	*ft_memcpy(void *dst, const void *src, size_t n)
{
	unsigned char		*d;
	unsigned char		*s;

	if (dst == src || n == 0)
		return (dst);
	d = (unsigned char *)dst;
	s = (unsigned char *)src;
	while (n--)
		*d++ = *s++;
	return (dst);
}
