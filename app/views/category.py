from flask import render_template, redirect, url_for
from flask_classy import FlaskView, route
from flask_login import login_required, current_user
from ..models import CategoryModel
from ..forms import CategoryForm


class Category(FlaskView):

    def get(self, id):
        category = CategoryModel.query.get_or_404(id)
        return render_template('category.html', category=category)

    def post(self):
        pass

    @login_required
    @route("new/", methods=['GET', 'POST'])
    def new(self):
        form = CategoryForm()
        if form.validate_on_submit():
            category = CategoryModel.add(user_id=current_user.id,
                                         name=form.name.data)
            return redirect(url_for('Category:get', id=category.id))
        return render_template('macros/form.html', url='Category:new', form=form)
