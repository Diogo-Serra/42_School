/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strlcat.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: diserra <diserra@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/09/05 13:59:27 by diserra           #+#    #+#             */
/*   Updated: 2025/09/05 14:37:52 by diserra          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

size_t	ft_strlcat(char *dest, char *src, size_t size)
{
	size_t	dlen;
	size_t	slen;
	size_t	i;

	dlen = 0;
	while (dlen < size && dest[dlen] != '\0')
		dlen++;
	slen = 0;
	while (src[slen] != '\0')
		slen++;
	if (dlen = size)
		return (dlen + slen);
	i = 0;
	while (src[i] != '\0' && dlen + i + 1 < size)
	{
		dest[dlen] = src[i];
		dlen++;
		i++;
	}
	dest[dlen] = '\0';

}
