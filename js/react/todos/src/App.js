import { Component } from 'react';
import TodoList from './TodoList';

// date of cre4ated 
const date1 = new Date(2024, 7, 19, 14, 5);
const date2 = new Date(2024, 7, 19, 15, 23);

const initialData = [ 
{ title: 'Изучить React',
desc: 'за пару дней)))',
image: '',
done: true, 
createdAt: date1.toLocaleString(),
key: date1.getTime()
},
{ title: 'Написать первое React-приложение',
desc: 'Список запланированных дел',
image:'',
done: false,
createdAt: date2.toLocaleString(),
key: date2.getTime()
}
]; 

export default class App extends Component { 
constructor(props) { 
super(props); 
this.data = initialData; 
} render() { 
return ( 
<div> 
<nav className="navbar is-light"> 
<div className="navbar-brand"> 
<span className="navbar-item is-uppercase"> 
Todos
</span>
</div>
</nav>
<main className="content px-6 mt-6"> 
<TodoList list={this.data}/>
</main>
</div>
); 
} 
}