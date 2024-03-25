package main

import (
	"fmt"
	"log"
	"net/http"
	"strings"

	"github.com/gorilla/mux"
)

type mockStore struct {
	climbs []string
}

func main() {

	s := &mockStore{climbs: make([]string, 0)}

	r := mux.NewRouter()

	r.PathPrefix("/addClimb/").HandlerFunc(handlePostClimb(s)).Methods("POST")

	srv := &http.Server{Addr: ":6969", Handler: r}
	err := srv.ListenAndServe()
	if err != nil {
		log.Fatalf("server failed")
	}

}

func handlePostClimb(s *mockStore) http.HandlerFunc {

	return func(w http.ResponseWriter, r *http.Request) {
		coords := strings.Split(r.URL.Path[len("/addClimb/"):], "/")
		fmt.Fprint(w, coords)
		s.climbs = append(s.climbs, coords[0])
		log.Printf(s.climbs[0])

		// w.WriteHeader(http.StatusOK)

	}

}
