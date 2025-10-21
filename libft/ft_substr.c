/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_substr.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: diosoare <diosoare@student.42lisboa.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/20 17:36:36 by diosoare          #+#    #+#             */
/*   Updated: 2025/10/21 15:24:35 by diosoare         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

char	*ft_substr(char const *s, unsigned int start, size_t len)
{
	size_t	slen;
	size_t	n;
	size_t	i;
	char	*out;

	if (!s)
		return (NULL);
	slen = ft_strlen(s);
	if (start >= slen)
		n = 0;
	else if (len > slen - start)
		n = slen - start;
	else
		n = len;
	out = (char *)malloc(n + 1);
	if (!out)
		return (NULL);
	i = 0;
	while (i < n)
	{
		out[i] = s[start + i];
		i++;
	}
	out[n] = '\0';
	return (out);
}
