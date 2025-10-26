/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strjoin.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: diosoare <diosoare@student.42lisboa.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/16 08:39:45 by diosoare          #+#    #+#             */
/*   Updated: 2025/10/26 01:16:50 by diosoare         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

char	*ft_strjoin(char const *s1, char const *s2)
{
	size_t	l[2];
	char	*out;

	if (!s1 || !s2)
		return (NULL);
	l[0] = ft_strlen(s1);
	l[1] = ft_strlen(s2);
	out = (char *)ft_calloc(l[0] + l[1] + 1, sizeof(char));
	if (!out)
		return (NULL);
	ft_memcpy(out, s1, l[0]);
	ft_memcpy(out + l[0], s2, l[1]);
	return (out);
}
