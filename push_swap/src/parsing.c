/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   parsing.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: diosoare <diosoare@student.42lisboa.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/02/17 17:19:53 by diosoare          #+#    #+#             */
/*   Updated: 2026/02/18 12:46:30 by diosoare         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

static void	validate_and_add(t_stack **a, char *str, char **split)
{
	long	num;

	if (!is_valid_number(str))
		error_exit_split(a, NULL, split);
	num = ft_atol(str);
	if (num > INT_MAX || num < INT_MIN)
		error_exit_split(a, NULL, split);
	add_number(a, num);
}

static void	process_split(t_stack **a, char **split)
{
	int	i;

	i = 0;
	while (split[i])
	{
		validate_and_add(a, split[i], split);
		i++;
	}
}

t_stack	*parse_input(int argc, char **argv)
{
	int		i;
	t_stack	*a;
	char	**split;

	a = NULL;
	i = 1;
	while (i < argc)
	{
		split = ft_split(argv[i], ' ');
		if (!split)
			error_exit(&a, NULL);
		if (!*split)
		{
			free(split);
			error_exit(&a, NULL);
		}
		process_split(&a, split);
		free_split(split);
		i++;
	}
	return (a);
}
