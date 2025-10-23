/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_split.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: diosoare <diosoare@student.42lisboa.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/20 17:37:43 by diosoare          #+#    #+#             */
/*   Updated: 2025/10/24 00:39:00 by diosoare         ###   ########.fr       */
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
	int		i;
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

static void	*free_heap(char **tab)
{
	int	i;

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
	tab = ft_calloc(nwords + 1, sizeof(char *));
	if (!tab)
		return (NULL);
	while (i < nwords)
	{
		while (*src && *src == sep)
			src++;
		lenwords = ft_wordlen(src, sep);
		tab[i] = ft_calloc(lenwords + 1, sizeof(char));
		if (!tab[i])
			return (free_heap(tab));
		ft_memcpy(tab[i], src, lenwords);
		tab[i++][lenwords] = '\0';
		src += lenwords;
	}
	return (tab);
}

int	main(void)
{
	char	**split;

	printf("--- Test 1: Basic ---\n");
	split = ft_split("Teste 1 2 3", ' ');
	if (split)
	{
		for (int i = 0; split[i]; i++)
			printf("'%s'\n", split[i]);
		free_heap(split);
	}
	printf("\n--- Test 2: Edge spaces ---\n");
	split = ft_split("  leading and trailing spaces  ", ' ');
	if (split)
	{
		for (int i = 0; split[i]; i++)
			printf("'%s'\n", split[i]);
		free_heap(split);
	}
	printf("\n--- Test 3: Multiple spaces ---\n");
	split = ft_split("word1   word2", ' ');
	if (split)
	{
		for (int i = 0; split[i]; i++)
			printf("'%s'\n", split[i]);
		free_heap(split);
	}
	printf("\n--- Test 4: Empty string ---\n");
	split = ft_split("", ' ');
	if (split)
	{
		printf("Result array is not NULL. Word count: ");
		int count = 0;
		while(split[count]) count++;
		printf("%d\n", count);
		if (split[0] == NULL)
			printf("First element is NULL, as expected.\n");
		free_heap(split);
	}
	printf("\n--- Test 5: String with only separators ---\n");
	split = ft_split("       ", ' ');
	if (split)
	{
		printf("Result array is not NULL. Word count: ");
		int count = 0;
		while(split[count]) count++;
		printf("%d\n", count);
		if (split[0] == NULL)
			printf("First element is NULL, as expected.\n");
		free_heap(split);
	}
	printf("\n--- Test 6: NULL input ---\n");
	split = ft_split(NULL, ' ');
	if (!split)
		printf("Result is NULL as expected.\n");
	return (0);
}
