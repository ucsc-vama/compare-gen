
NAME = error
SRC	= $(NAME).cpp
OBJ	= $(SRC:%.cpp=%.o)

CFLAGS	= -std=c++17 -Wall

$(NAME): $(OBJ)
	g++ $(CFLAGS) -o $@ $^

%.o: %.cpp
	g++ $(CFLAGS) -c $<

clean:
	rm -f $(NAME) $(OBJ)