import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';

export class UserAuthenication {
  constructor(
    public message: string,
    public username: string,
    public id: number,
    public status: number,
    public success: boolean
  ){}
}

@Injectable({
  providedIn: 'root'
})
export class AuthenticationService {

  constructor(
    private http: HttpClient
  ) { }

  authenticate(username){
    return this.http.get<UserAuthenication>(`http://127.0.0.1:5000/api/authenticate/${username}`);
  }

  isUserLoggedIn(){
    let user = sessionStorage.getItem('authenticatedUser')
    return !(user === null)
  }
  logout() {
    sessionStorage.removeItem('authenticatedUser')
    sessionStorage.removeItem('id')
  }
}
