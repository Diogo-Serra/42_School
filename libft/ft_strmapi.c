/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strmapi.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: diosoare <diosoare@student.42lisboa.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/16 08:43:08 by diosoare          #+#    #+#             */
/*   Updated: 2025/10/30 01:26:54 by diosoare         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

char	*ft_strmapi(char const *s, char (*f)(unsigned int, char))
{
	size_t			len;
	size_t			i;
	char			*out;

	if (!s || !f)
		return (NULL);
	len = ft_strlen(s);
	out = (char *)ft_calloc((len + 1), sizeof(char));
	if (!out)
		return (NULL);
	i = 0;
	while (i < len)
	{
		out[i] = f((unsigned int)i, s[i]);
		i++;
	}
	return (out);
}
