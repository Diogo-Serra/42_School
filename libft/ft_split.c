/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_split.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: diosoare <diosoare@student.42lisboa.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/20 17:37:43 by diosoare          #+#    #+#             */
/*   Updated: 2025/10/23 23:22:57 by diosoare         ###   ########.fr       */
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

static void	free_table(char **tab, int filled)
{
	while (filled >= 0)
		free(tab[filled--]);
	free(tab);
}

char	**ft_split(const char *src, char sep)
{
	char	**tab;
	const char	*p;
	int		nwords;
	int		i;
	size_t	lenwords;

	if (!src)
		return (NULL);
	i = 0;
	p = src;
	nwords = ft_nwords(src, sep);
	tab = ft_calloc((size_t)nwords + 1, sizeof(char *));
	if (!tab)
		return (NULL);
	while (i < nwords)
	{
		while (*p && *p == sep)
			p++;
		lenwords = ft_wordlen(p, sep);
		tab[i] = ft_calloc(lenwords + 1, sizeof(char));
		if (!tab[i])
		{
			free_table(tab, i - 1);
			return (NULL);
		}
		ft_memcpy(tab[i], p, lenwords);
		tab[i][lenwords] = '\0';
		p += lenwords;
		i++;
	}
	return (tab);
}

int main(void)
{
	char	source[] = "Teste 1 2 3";
	char	sep = ' ';
	char	**split;
	int		words;
	int		i;

	i = 0;
	words = ft_nwords(source, sep);
	split = ft_split(source, sep);
	while (i < words)
		printf("%s\n", split[i++]);
	while (i >= 0)
		free(split[i--]);
	free(split);
	return (0);
}
