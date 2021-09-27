import { Component, OnInit } from '@angular/core';
import { Router, ActivatedRoute } from '@angular/router';
import { AuthenticationService } from '../service/authentication.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {
  public userName = ''
  public unAuthorizedMessage = ''
  public errorMessage = 'Invalid login'
  public invalidLogin = false;
  public isSuccessLogin = true;

  constructor(
    private router: Router,
    private route: ActivatedRoute,
    private authenicationService: AuthenticationService
  ) { }

  ngOnInit(): void {
  }

  handleLogin() {
    this.authenicationService.authenticate(this.userName).subscribe(
      response => this.handleSuccessfulResponse(response),
      error => this.handleErrorResponse(error)
    )
    
  }

  handleSuccessfulResponse(response){
    if (response.success) {
      sessionStorage.setItem('id', response.id);
      sessionStorage.setItem('authenticatedUser', this.userName);
      this.router.navigate(['dashboard', response.id])
    }
    else {
      this.unAuthorizedMessage = response.message;
      this.isSuccessLogin = false;
    }
    
  }

  handleErrorResponse(error){
    this.errorMessage = error.error.message;
  }

}
