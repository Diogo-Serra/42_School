/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: diosoare <diosoare@student.42lisboa.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/08 19:26:08 by diosoare          #+#    #+#             */
/*   Updated: 2025/11/08 22:57:50 by diosoare         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "get_next_line.h"

char *get_next_line(int fd)
{
	char		buffer[BUFFER_SIZE];
	static char	*parts;

	if (fd == -1)
		return (NULL);
	read(fd, buffer, BUFFER_SIZE);
	parts = ft_calloc(ft_strnlen(buffer) + 2, sizeof(char));
	parts = ft_memcpy(parts, buffer, ft_strnlen(buffer) + 1);
	if (!parts)
		return (NULL);	
	close(fd);
	return (parts);
}

int main(void)
{
    char    *out;
    int     fd;

    fd = open("test.txt", O_RDONLY);
    out = get_next_line(fd);
	printf("%s\n", out);
    free(out);
    return (0);
}
