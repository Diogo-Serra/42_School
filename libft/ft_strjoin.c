/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strjoin.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: diserra <diserra@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/09/08 15:50:58 by diserra           #+#    #+#             */
/*   Updated: 2025/09/08 15:56:44 by diserra          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

char	*ft_strjoin(char const *s1, char const *s2)
{
	size_t	l1;
	size_t	l2;
	char	*out;

	if (!s1 || !s2)
		return (NULL);
	l1 = ft_strlen(s1);
	l2 = ft_strlen(s2);
	out = (char *)malloc(l1 + l2 + 1);
	if (!out)
		return (NULL);
	ft_memcpy(out, s1, l1);
	ft_memcpy(out + l1, s2, l2);
	out[l1 + l2] = '\0';
	return (out);
}
