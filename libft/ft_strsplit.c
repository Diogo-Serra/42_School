/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strsplit.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: diserra <diserra@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/09/08 18:29:23 by diserra           #+#    #+#             */
/*   Updated: 2025/09/08 18:50:35 by diserra          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

static size_t	wc(char const *s, char c)
{
	size_t	i;
	size_t	w;

	i = 0;
	w = 0;
	while (s[i])
	{
		while (s[i] && s[i] == c)
			i++;
		if (s[i])
		{
			w++;
			while (s[i] && s[i] != c)
				i++;
		}
	}
	return (w);
}

static void	*free_tab(char **tab, size_t n)
{
	size_t	i;

	i = 0;
	while (i < n)
	{
		free(tab[i]);
		i++;
	}
	free(tab);
	return (NULL);
}

static int	fill_words(char **tab, char const *s, char c, size_t w)
{
	size_t	i;
	size_t	j;
	size_t	k;

	i = 0;
	j = 0;
	while (j < w)
	{
		while (s[i] && s[i] == c)
			i++;
		k = i;
		while (s[i] && s[i] != c)
			i++;
		tab[j] = ft_strsub(s, (unsigned int)k, i - k);
		if (!tab[j])
			return (free_tab(tab, j) == NULL);
		j++;
	}
	return (1);
}

char	**ft_strsplit(char const *s, char c)
{
	size_t	w;
	char	**tab;

	if (!s)
		return (NULL);
	w = wc(s, c);
	tab = (char **)malloc((w + 1) * sizeof(char *));
	if (!tab)
		return (NULL);
	if (!fill_words(tab, s, c, w))
		return (NULL);
	tab[w] = NULL;
	return (tab);
}
