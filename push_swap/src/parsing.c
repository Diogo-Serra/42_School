/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   parsing.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: diosoare <diosoare@student.42lisboa.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/02/17 17:19:53 by diosoare          #+#    #+#             */
/*   Updated: 2026/02/17 18:27:03 by diosoare         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

t_stack	*parse_input(int argc, char **argv)
{
	int		i;
	t_stack	*a;
	char	**split;

	i = 1;
	a = NULL;
	while (i < argc)
	{
		split = ft_split(argv[i++], ' ');
		if (!split || !*split)
		{
			if (split)
				free(split);
			error_exit(&a, NULL);
		}
		process_split(&a, split);
		free_split(split);
	}
	return (a);
}
