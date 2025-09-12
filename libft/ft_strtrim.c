/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strtrim.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: diserra <diserra@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/09/08 18:05:39 by diserra           #+#    #+#             */
/*   Updated: 2025/09/13 00:37:48 by diserra          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

static int	is_sp(char c)
{
	return (c == ' ' || c == '\n' || c == '\t');
}

char	*ft_strtrim(char const *s)
{
	size_t	i;
	size_t	j;
	char	*out;

	if (!s)
		return (NULL);
	i = 0;
	while (s[i] && is_sp(s[i]))
		i++;
	j = ft_strlen(s);
	while (j > i && is_sp(s[j - 1]))
		j--;
	out = (char *)malloc(j - i + 1);
	if (!out)
		return (NULL);
	ft_memcpy(out, s + i, j - i);
	out[j - i] = '\0';
	return (out);
}
