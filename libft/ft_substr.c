/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_substr.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: diosoare <diosoare@student.42lisboa.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/20 17:36:36 by diosoare          #+#    #+#             */
/*   Updated: 2025/10/30 01:19:05 by diosoare         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

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
