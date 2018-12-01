class Tag {

	constructor(name, inner, attrs=[]){
		this.name = name
		this.inner = inner 
		this.attrs = attrs
	}

	stringfyAttrs() {
		var str_attrs = []
		this.attrs.forEach(function(attr){
			str_attrs.push(attr.content)
		})
		return str_attrs.join(' ')
	}

	get content(){
		return `<${this.name}${this.attrs.length ? ' '+this.stringfyAttrs() : ''}>${this.inner}</${this.name}>`
	}

};

Tag.Attribute = class {

	constructor(name, values=[]){
		this.name = name
		this.values = values
	}

	get content(){
		return `${this.name}="${this.values.join(' ')}"`
	}
}

class Task {

	constructor(title, initial_date, end_date) {
		this.initial_date = initial_date; 
		this.end_date = end_date;
	}
}

data = [

	{
		'title': 'task0', 
		'initial_date': '2018-01-01', 
		'end_date': '2018-02-01'
	},

	{
		'title': 'task1', 
		'initial_date': '2018-01-01', 
		'end_date': '2018-02-01'
	},

	{
		'title': 'task2', 
		'initial_date': '2018-01-01', 
		'end_date': '2018-02-01'
	},

	{
		'title': 'task3', 
		'initial_date': '2018-01-01', 
		'end_date': '2018-02-01'
	},

	{
		'title': 'task4', 
		'initial_date': '2018-01-01', 
		'end_date': '2018-02-01'
	},

]

var tasks = []

data.forEach(function(elem){
	tasks.push(new Task(elem.title, elem.initial_date, elem.end_date))
})

c = new Tag.Attribute('class', ['hello', 'motherfucker'])
d = new Tag.Attribute('for', ['mean', 'ok'])

tag = new Tag('div', 'hello', attrs=[c, d])

console.log(tag.content)






