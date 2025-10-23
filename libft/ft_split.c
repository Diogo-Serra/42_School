/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_split.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: diosoare <diosoare@student.42lisboa.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/20 17:37:43 by diosoare          #+#    #+#             */
/*   Updated: 2025/10/23 19:46:36 by diosoare         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

static size_t	ft_wordlen(const char *src, char c)
{
	size_t	i;

	if (!src)
		return (0);
	i = 0;
	while (src[i] && src[i] != c)
		i++;
	return (i);
}

static int	ft_nwords(const char *src, char c)
{
	size_t	i;
	int		words;

	i = 0;
	words = 0;
	if (!src)
		return (0);
	while (src[i])
	{
		if (src[i] != c && (i == 0 || src[i - 1] == c))
			words++;
		i++;
	}
	return (words);
}

static char	*ft_strnchr(const char *s, int c)
{
	char		ch;
	size_t		i;

	i = 0;
	ch = (const char)c;
	while (s[i])
	{
		if (s[0] != c)
			return ((char *)&s[i]);
		if (s[i] == ch && s[i + 1] != ch)
			return ((char *)&s[i + 1]);
		i++;
	}
	return ((char *)s);
}

char	**ft_split(const char *src, char c)
{
	char	**tab;
	char	*next;
	int		nwords;
	int		i;
	size_t	lenwords;

	if (!src)
		return (NULL);
	i = 0;
	next = ft_strnchr(src, (int)c);
	nwords = ft_nwords(next, c);
	tab = ft_calloc((size_t)nwords, sizeof(char *));
	if (!tab)
		return (NULL);
	while (i < nwords)
	{
		lenwords = ft_wordlen(next, c);
		tab[i] = ft_calloc(lenwords, sizeof(char));
		if (!tab)
			return (NULL);
		ft_memcpy(tab[i++], next, lenwords);
		next += lenwords;
		next = ft_strnchr(next, (int)c);
	}
	return (tab);
}
