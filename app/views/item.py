from flask import render_template, redirect, url_for
from flask_classy import FlaskView, route
from flask_login import login_required, current_user
from ..models import ItemModel
from ..forms import ItemForm


def validate_ownership(item):
    """ Validate if a user is owner of a item. """
    if current_user.id == item.user_id:
        return True
    return


class Item(FlaskView):

    def get(self, id):
        item = ItemModel.query.get_or_404(id)
        return render_template('item.html', item=item)

    def post(self):
        pass

    @login_required
    @route('new/', methods=['GET', 'POST'])
    def new(self):
        form = ItemForm()
        if form.validate_on_submit():
            item = ItemModel.add(user_id=current_user.id, name=form.name.data,
                                 description=form.description.data,
                                 category_id=form.category_id.data)
            return redirect(url_for('Item:get', id=item.id))
        return render_template("macros/form.html", url='Item:new', form=form)

    @login_required
    @route('edit/<id>', methods=['GET', 'POST'])
    def edit(self, id):
        item = ItemModel.query.get_or_404(id)
        if not validate_ownership(item):
            return redirect(url_for('Item:get', id=item.id))
        form = ItemForm(obj=item)
        if form.validate_on_submit():
            form.populate_obj(item)
            item.update()
            return redirect(url_for('Item:get', id=item.id))
        return render_template("macros/form.html", url='Item:edit', form=form,
                               kwargs={'id': item.id})

    @login_required
    def delete(self, id):
        item = ItemModel.query.get_or_404(id)
        if not validate_ownership(item):
            return "No ownership over this item.", 403
        item.delete()
        return '', 200
