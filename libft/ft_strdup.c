/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strdup.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: diosoare <diosoare@student.42lisboa.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/20 13:23:37 by diosoare          #+#    #+#             */
/*   Updated: 2025/10/30 00:22:30 by diosoare         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"
#include "string.h"

char	*ft_strdup(const char *s)
{
	char	*dup;
	size_t	lenSrc;
	
	if (!s)
		return (NULL);
	lenSrc = ft_strlen(s);
	dup = ft_calloc(lenSrc + 1, sizeof(char));
	if (!dup)
		return (NULL);
	ft_memcpy(dup, s, lenSrc);
	return (dup);
}
