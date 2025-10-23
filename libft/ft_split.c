/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_split.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: diosoare <diosoare@student.42lisboa.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/20 17:37:43 by diosoare          #+#    #+#             */
/*   Updated: 2025/10/23 17:17:12 by diosoare         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

size_t	ft_wordlen(const char *src, char c)
{
	size_t	i;

	if (!src)
		return (0);
	i = 0;
	while (src[i] && src[i] != c)
		i++;
	return (i);
}

int	ft_nwords(const char *src, char c)
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

char	*ft_strnchr(const char *s, int c)
{
	char		ch;
	size_t		i;

	i = 0;
	ch = (const char)c;
	while (s[i])
	{
		if (s[i] == ch && s[i + 1] != ch)
			return ((char *)&s[i]);
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

	i = 0;
	if (!src)
		return (NULL);
	nwords = ft_nwords(src, c);
	tab = ft_calloc(nwords + 1, sizeof(char));
	if (!tab)
		return (NULL);
	next = ft_strnchr(src, (int)c);
	while (i <= nwords)
	{
		tab[i] = calloc((size_t)ft_wordlen + 1, sizeof(char));
		ft_memcpy(tab[i], next, ft_wordlen(next, c));
		nwords--;
		i++;
	}
	return (tab);
}

int	main(void)
{
	char	**tab;
	char	*src = "Hello World Escola 42";
	char	sep = ' ';
	int		nwords;
	int		i;

	nwords = ft_nwords(src, sep);
	tab = ft_split(src, sep);
	i = 0;
	while (i <= nwords)
		printf("%s\n", tab[i++]);
	free(tab);
	return (0);
}
