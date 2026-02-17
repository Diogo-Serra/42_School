/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strrchr.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: diosoare <diosoare@student.42lisboa.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/16 08:44:31 by diosoare          #+#    #+#             */
/*   Updated: 2025/10/30 17:10:19 by diosoare         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

char	*ft_strrchr(const char *s, int c)
{
	char		ch;
	size_t		i;

	i = 0;
	ch = (char)c;
	while (s[i])
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
