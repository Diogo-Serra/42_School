/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   libft.h                                            :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: diserra <diserra@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/09/04 18:05:58 by diserra           #+#    #+#             */
/*   Updated: 2025/09/04 22:46:31 by diserra          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef LIBFT_H
# define LIBFT_H

# include <stddef.h>
# include <stdio.h>

size_t	ft_strlen(const char *string);
char	*ft_strcpy(char *dest, const char *source);

#endif

/* Tests
int	main(int argc, char **argv)
{
	int	result;

	if (argc == 2)
	{
		result = ft_strlen(argv[1]);
		printf("strlen: %d\n", result);
	}
	return (0);
}

int	main(int argc, char **argv)
{
	char	*ptr;
	char	dest[20];

	if (argc == 2)
	{
		ptr = ft_strcpy(dest, argv[1]);
		printf("strcpy: %s\n", ptr);
	}
	return (0);
}*/
