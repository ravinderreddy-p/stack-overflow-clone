import { Component, OnInit } from '@angular/core';
import { Router, ActivatedRoute } from '@angular/router';
import { AuthenticationService } from '../service/authentication.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {

  username = ''
  unauthorizedMessage = ''
  errorMessage = 'Invalid login'
  invalidLogin = false;
  isSuccessLogin = true;

  constructor(
    private router: Router,
    private route: ActivatedRoute,
    private authenicationService: AuthenticationService
  ) { }

  ngOnInit(): void {
  }

  handleLogin() {
    this.authenicationService.authenticate(this.username).subscribe(
      response => this.handleSuccessfulResponse(response),
      error => this.handleErrorResponse(error)
    )
    
  }

  handleSuccessfulResponse(response){
    this.username = response.username;
    if (response.success) {
      sessionStorage.setItem('authenticatedUser', this.username);
      this.router.navigate(['dashboard', this.username])
    }
    else {
      this.unauthorizedMessage = response.message;
      this.isSuccessLogin = false;
    }
    
  }

  handleErrorResponse(error){
    this.errorMessage = error.error.message;
  }

}
