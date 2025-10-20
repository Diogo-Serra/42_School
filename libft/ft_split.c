/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_split.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: diosoare <diosoare@student.42lisboa.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/20 17:37:43 by diosoare          #+#    #+#             */
/*   Updated: 2025/10/20 17:47:11 by diosoare         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

static size_t	word_len(char const *s, char c)
{
	size_t	i;

	i = 0;
	while (s[i] && s[i] != c)
		i++;
	return (i);
}

static int	count_words(char const *s, char c)
{
	int	cnt;
	int	in;

	cnt = 0;
	in = 0;
	while (*s)
	{
		if (*s != c && !in)
		{
			in = 1;
			cnt++;
		}
		else if (*s == c)
			in = 0;
		s++;
	}
	return (cnt);
}

static char	**free_all(char **tab, int i)
{
	while (i-- > 0)
		free(tab[i]);
	free(tab);
	return (NULL);
}

static char	*dup_word(char const *s, char c)
{
	size_t	len;
	char	*w;

	len = word_len(s, c);
	w = (char *)malloc(len + 1);
	if (!w)
		return (NULL);
	ft_memcpy(w, s, len);
	w[len] = '\0';
	return (w);
}

char	**ft_split(char const *s, char c)
{
	char	**tab;
	int		i;

	if (!s)
		return (NULL);
	tab = (char **)malloc(sizeof(char *) * (count_words(s, c) + 1));
	if (!tab)
		return (NULL);
	i = 0;
	while (*s)
	{
		while (*s && *s == c)
			s++;
		if (!*s)
			break ;
		tab[i] = dup_word(s, c);
		if (!tab[i])
			return (free_all(tab, i));
		s += word_len(s, c);
		i++;
	}
	tab[i] = NULL;
	return (tab);
}
