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
  errorMessage = "Invalid User"
  invalidLogin = false;

  constructor(
    private router: Router,
    private route: ActivatedRoute,
    private authenicationService: AuthenticationService
  ) { }

  ngOnInit(): void {
  }

  handleLogin() {
    if(this.authenicationService.authenticate(this.username)){
      this.router.navigate(['dashboard', this.username])
      this.invalidLogin = false;
    }
    else {
      this.invalidLogin = true;
    }
    
  }

}
