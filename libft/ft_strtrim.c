/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strtrim.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: diserra <diserra@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/09/08 18:05:39 by diserra           #+#    #+#             */
/*   Updated: 2025/09/08 18:11:33 by diserra          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

char	*ft_strtrim(char const *s)
{
	size_t	start;
	size_t	end;
	size_t	i;
	char	*out;

	if (!s)
		return (NULL);
	start = 0;
	while (s[start] == ' ' || s[start] == '\n' || s[start] == '\t')
		start++;
	end = start;
	while (s[end])
		end++;
	while (end > start
		&& (s[end - 1] == ' ' || s[end - 1] == '\n' || s[end - 1] == '\t'))
		end--;
	out = (char *)malloc((end - start) + 1);
	if (!out)
		return (NULL);
	i = 0;
	while (start < end)
		out[i++] = s[start++];
	out[i] = '\0';
	return (out);
}
