/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strdup.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: diosoare <diosoare@student.42lisboa.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/14 19:20:53 by diosoare          #+#    #+#             */
/*   Updated: 2025/10/14 23:54:20 by diosoare         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdlib.h>

size_t	ft_strlen(const char *src)
{
	size_t	i;

	i = 0;
	while (src[i])
		i++;
	return (i);
}

char	*ft_strdup(char *src)
{
	char		*dest;
	size_t		i;
	size_t		len;

	if (src == NULL)
		return (NULL);
	len = (ft_strlen(src));
	dest = malloc((len + 1) * sizeof(*dest));
	if (!dest)
		return (NULL);
	i = 0;
	while (i <= len)
	{
		dest[i] = src[i];
		i++;
	}
	return (dest);
}
