/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strdup.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: diserra <diserra@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/09/05 00:25:03 by diserra           #+#    #+#             */
/*   Updated: 2025/09/14 17:02:27 by diserra          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

char	*ft_strdup(const char *s)
{
	char	*dest;
	size_t	i;
	size_t	len;

	len = ft_strlen(s);
	dest = (char *)malloc(len + 1);
	if (!dest)
		return (NULL);
	i = 0;
	while (i <= len)
	{
		dest[i] = s[i];
		i++;
	}
	return (dest);
}
