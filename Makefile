
SRC	= Runner.cpp
OBJ	= $(SRC:%.cpp=%.o)

CFLAGS	= -std=c++17 -Wall

Runner: $(OBJ)
	g++ $(CFLAGS) -o $@ $^

%.o: %.cpp
	g++ $(CFLAGS) -c $<

clean:
	rm -f Runner $(OBJ)