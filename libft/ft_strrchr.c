/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strrchr.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: diosoare <diosoare@student.42lisboa.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/16 08:44:31 by diosoare          #+#    #+#             */
/*   Updated: 2025/10/16 08:44:34 by diosoare         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

char	*ft_strrchr(const char *s, int c)
{
	const char	ch = (char)c;
	size_t		i;

	i = 0;
	while (s[i] != '\0')
		i++;
	if (s[i] == ch)
		return ((char *)&s[i]);
	while (i > 0)
	{
		i--;
		if (s[i] == ch)
			return ((char *)&s[i]);
	}
	return (NULL);
}
