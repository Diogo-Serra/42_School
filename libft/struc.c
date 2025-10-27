/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   struc.c                                            :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: diosoare <diosoare@student.42lisboa.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/27 14:30:13 by diosoare          #+#    #+#             */
/*   Updated: 2025/10/27 14:40:06 by diosoare         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>

typedef struct s_Player
{
	int		x;
	char	c;
}	t_player;

t_player	*db(void)
{
	static t_player	data;

	return (&data);
}

int	main(void)
{
	db()->x = 5;
	printf("%d\n", db()->x);
	return (0);
}