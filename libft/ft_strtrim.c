/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strtrim.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: diosoare <diosoare@student.42lisboa.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/16 08:46:00 by diosoare          #+#    #+#             */
/*   Updated: 2025/10/16 08:46:01 by diosoare         ###   ########.fr       */
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
