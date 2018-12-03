class Tag {

	constructor({name, inner, attrs={}}={}){
		this.name = name
		this.inner = inner 
		this.attrs = attrs
	}

	stringifyAttrs() {
		var str_attrs = []
		this.attrs.forEach(function(attr){
			str_attrs.push(attr.content)
		})
		return str_attrs.join(' ')
	}

	get content(){
		return `<${this.name}${this.attrs.length ? ' '+this.stringifyAttrs() : ''}>${this.inner}</${this.name}>`
	}

};

Tag.Attribute = class {

	constructor({name, values}={}){
		this.name = name
		this.values = values
	}

	get content(){
		return `${this.name}="${this.values.join(' ')}"`
	}
}


class Schedule {

	constructor({data, config}={}){
		this.config = config
		this.groups = this.parseData(data)
		this.timeBorderMax = this.getTimeBorders().max
		this.timeBorderMin = this.getTimeBorders().min
	}

	parseData(data) {

		var groups = []

		data.forEach(function(group){

			var tasks = []

			group.tasks.forEach(function(task){

				tasks.push(new Schedule.Task({'title': task.title, 'initial_date': task.initial_date, 'end_date': task.end_date}))

			})

			groups.push(new Schedule.Group({'title': group.title, 'tasks': tasks}))
			
		})

		return groups

	}

	getTimeBorders() {
		var min = Number.MAX_SAFE_INTEGER
		var max = 0
		var a = this

		this.groups.forEach(function(group){
			group.tasks.forEach(function(task){
				if(task.initial_date.getTime() < min)
					min = task.initial_date.getTime()
				if(task.end_date.getTime() > max)
					max = task.end_date.getTime()
			})
		})

		return {
			'min': min,
			'max': max,
		}
	}

 	get HTMLTable() {
		return new Schedule.HTMLTable({schedule: this})
	}

}

Schedule.Task = class {

	constructor({title, initial_date, end_date}={}) {
		this.title = title
		this.initial_date = new Date(initial_date); 
		this.end_date = new Date(end_date);
	}
}

Schedule.Group = class {
	constructor({title, tasks}={}) {
		this.title = title
		this.tasks = tasks
	}
}

Schedule.HTMLTable = class {

	constructor({schedule}={}){
		this.schedule = schedule
		this.config
		this.section_time = (schedule.timeBorderMax - schedule.timeBorderMin) / schedule.config.resolution
		console.log('section_time', this.section_time)
	}

	tdSection({colspan, attrs=[]}={}){
		if(colspan){
			var colspan_attr = new Tag.Attribute({'name': 'colspan', 'values': [String(colspan)]})
			return (new Tag({'name': 'td', 'inner': ' ', 'attrs':[colspan_attr].concat(attrs)})).content
		} else {
			return ''
		}
	}

	htmlTimeCells(task){
		var td_tags = []
		var resolution = this.schedule.config.resolution
		var initial_date = task.initial_date.getTime()
		var end_date = task.end_date.getTime()

		var cspan_left = 0
		var cspan_time = 0

		for (var i = 1; i <= this.schedule.config.resolution; i++) {
			var level = this.schedule.timeBorderMin + i * this.section_time
			if ((level > initial_date) &&
				(level <= end_date)){
				cspan_left = (cspan_left == 0) ? i : cspan_left 
				cspan_time++
			}
		}

		var i_d = task.initial_date.getUTCDate()
		var i_m = task.initial_date.getUTCMonth() + 1
		var i_y = task.initial_date.getUTCFullYear().toString().substr(-2)
		var e_d = task.end_date.getUTCDate()
		var e_m = task.end_date.getUTCMonth() + 1
		var e_y = task.end_date.getUTCFullYear().toString().substr(-2)
		var duration_days = (task.end_date - task.initial_date)/86400000
		var dt = new Tag.Attribute({'name': 'data-toggle', 'values': ['tooltip']})
		var dh = new Tag.Attribute({'name': 'data-html', 'values': ['true']})
		var tt = new Tag.Attribute({'name': 'title', 'values': [`${duration_days} dia${duration_days > 1 ? 's' : ''}, de <b>${i_d}/${i_m}/${i_y}</b> a <b>${e_d}/${e_m}/${e_y}</b>`]})
		var tb = new Tag.Attribute({'name': 'data-container', 'values': ['body']})
		var class_attr = new Tag.Attribute({'name': 'class', 'values': ['schedule-intime', 'test']})
		var td_time = this.tdSection({'colspan': cspan_time, 'attrs': [class_attr, dt, dh, tt, tb]})

		cspan_left -= 1
		var class_attr = new Tag.Attribute({'name': 'class', 'values': ['schedule-outtime']})
		var td_left = this.tdSection({'colspan': cspan_left, 'attrs': [class_attr]})

		var cspan_right = this.schedule.config.resolution - (cspan_left + cspan_time)
		var td_right = this.tdSection({'colspan': cspan_right, 'attrs': [class_attr]})

		return [td_left, td_time, td_right]
	}

	get html(){
		var a = this
		var trs = []

		var first_td = (new Tag({'name': 'td', 'inner': this.schedule.config.title})).content
		var scale_tds = []

		for (var i = 0; i < this.schedule.config.resolution; i++) {
			scale_tds.push((new Tag({'name': 'td', 'inner': ' '})).content)
		}

		var c = new Tag.Attribute({'name': 'class', 'values': ['colspanreference']})
		var first_tr = (new Tag({'name': 'tr', 'inner': first_td + scale_tds.join(''), 'attrs': [c]})).content
		var trs = [first_tr]

		this.schedule.groups.forEach(function(group){

			var c = new Tag.Attribute({'name': 'class', 'values': ['schedule-group-label']})
			var group_label_td = (new Tag({'name': 'td', 'inner': group.title, 'attrs': [c]})).content
			var group_right_line = a.tdSection({'colspan': a.schedule.config.resolution, 'attrs': [c]})

			var group_label_tr = (new Tag({'name': 'tr', 'inner': group_label_td + group_right_line})).content

			trs.push(group_label_tr)
			group.tasks.forEach(function(task){

				var c = new Tag.Attribute({'name': 'class', 'values': ['schedule-label']})
				var tag = new Tag({'name': 'td', 'inner': task.title, 'attrs': [c]})
				var tags = a.htmlTimeCells(task)
				tags.unshift(tag.content)
				trs.push((new Tag({'name': 'tr', 'inner': tags.join('')})).content)

			})
		})

		var c = new Tag.Attribute({'name': 'class', 'values': ['schedule']})
		return (new Tag({'name': 'table', 'inner': trs.join('\n'), 'attrs':[c]})).content
	}	

}


data = [

	{
		'title': 'Teste',
		'tasks': [
			{
				'title': 'task1', 
				'initial_date': '2018-10-12', 
				'end_date': '2018-10-15'
			},

			{
				'title': 'task2', 
				'initial_date': '2018-10-10', 
				'end_date': '2018-10-11',
			},

			{
				'title': 'task3', 
				'initial_date': '2018-10-10', 
				'end_date': '2018-10-12'
			},

		]
	},


	{
		'title': 'Teste 2',
		'tasks': [
			{
				'title': 'task4', 
				'initial_date': '2018-10-15', 
				'end_date': '2018-10-17'
			},

			{
				'title': 'task5', 
				'initial_date': '2018-10-10', 
				'end_date': '2018-11-12'
			},

			{
				'title': 'task6', 
				'initial_date': '2018-10-23', 
				'end_date': '2018-11-11'
			},

			{
				'title': 'task7', 
				'initial_date': '2018-10-10', 
				'end_date': '2018-10-11'
			},

			{
				'title': 'task8', 
				'initial_date': '2018-10-16', 
				'end_date': '2018-12-10'
			},

		]
	},


]

schedule = new Schedule({'data': data, 'config': {'resolution': 365, 'title': 'Tabela de Cronograma'}})

c = new Tag.Attribute({'name': 'class', 'values': ['hello', 'motherfucker']})
d = new Tag.Attribute({'name': 'for', 'values': ['mean', 'ok']})

tag = new Tag({'name': 'div', 'inner': 'hello', 'attrs': [c, d]})

document.getElementById('schedule-table-container').innerHTML = schedule.HTMLTable.html









