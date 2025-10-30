/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strdup.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: diosoare <diosoare@student.42lisboa.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/20 13:23:37 by diosoare          #+#    #+#             */
/*   Updated: 2025/10/30 00:46:00 by diosoare         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

char	*ft_strdup(const char *s)
{
	char	*dup;
	size_t	lensrc;

	if (!s)
		return (NULL);
	lensrc = ft_strlen(s);
	dup = ft_calloc(lensrc + 1, sizeof(char));
	if (!dup)
		return (NULL);
	ft_memcpy(dup, s, lensrc);
	return (dup);
}
