/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_split.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: diosoare <diosoare@student.42lisboa.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/20 17:37:43 by diosoare          #+#    #+#             */
/*   Updated: 2025/10/30 01:25:40 by diosoare         ###   ########.fr       */
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

static size_t	ft_nwords(const char *src, char c)
{
	size_t	i;
	size_t	words;

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

static void	*free_heap(char **tab)
{
	size_t	i;

	i = 0;
	while (tab[i])
	{
		free(tab[i]);
		i++;
	}
	free(tab);
	return (NULL);
}

char	**ft_split(const char *src, char sep)
{
	char	**tab;
	size_t	i;
	size_t	nwords;
	size_t	lenwords;

	if (!src)
		return (NULL);
	i = 0;
	nwords = ft_nwords(src, sep);
	tab = (char **)ft_calloc(nwords + 1, sizeof(char *));
	if (!tab)
		return (NULL);
	while (i < nwords)
	{
		while (*src && *src == sep)
			src++;
		lenwords = ft_wordlen(src, sep);
		tab[i] = (char *)ft_calloc(lenwords + 1, sizeof(char));
		if (!tab[i])
			return (free_heap(tab));
		ft_memcpy(tab[i++], src, lenwords);
		src += lenwords;
	}
	return (tab);
}
