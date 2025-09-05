/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strlcat.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: diserra <diserra@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/09/05 13:59:27 by diserra           #+#    #+#             */
/*   Updated: 2025/09/05 14:42:42 by diserra          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

size_t	ft_strlcat(char *dest, const char *src, size_t size)
{
	size_t	dlen;
	size_t	slen;
	size_t	i;

    while (dlen < dstsize && dst[dlen] != '\0')
        dlen++;
    while (src[slen] != '\0')
        slen++;

    if (dlen == dstsize)
        return (dstsize + slen);          /* no room to append */

    /* bytes available including space for the NUL */
    while (src[i] != '\0' && i + 1 < (dstsize - dlen))
    {
        dst[dlen + i] = src[i];
        i++;
    }
    dst[dlen + i] = '\0';
    return (dlen + slen);     
}
