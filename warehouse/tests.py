from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from warehouse.models import Product, Category
from warehouse.forms import ProductListForm, ProductUpdateForm, ProductDeleteForm
from warehouse.choices import Unit_choices



class CategoryModelTests(TestCase):

    def test_category_str(self):
        c = Category.objects.create(name="Office")
        self.assertEqual(str(c), "Office")


class ProductModelTests(TestCase):

    def test_product_create_minimal(self):
        c = Category.objects.create(name="Tools")
        p = Product.objects.create(
            name="Hammer",
            price=10,
            category=c,
            internal_code="HM001",
            min_quantity=1,
        )
        self.assertIsNotNone(p.id)
        self.assertEqual(p.quantity, 0)
        self.assertEqual(p.unit, Unit_choices.PIECE)

    def test_product_price_validator(self):
        c = Category.objects.create(name="Tools")
        p = Product(
            name="Screwdriver",
            price=0,
            category=c,
            internal_code="SC001",
            min_quantity=1,
        )
        with self.assertRaises(ValidationError):
            p.full_clean()

    def test_product_internal_code_unique(self):
        c = Category.objects.create(name="Tools")
        Product.objects.create(
            name="Item1",
            price=5,
            category=c,
            internal_code="X001",
            min_quantity=1,
        )
        with self.assertRaises(Exception):
            Product.objects.create(
                name="Item2",
                price=5,
                category=c,
                internal_code="X001",
                min_quantity=1,
            )

    def test_product_str(self):
        c = Category.objects.create(name="Tools")
        p = Product.objects.create(
            name="Wrench",
            price=12,
            category=c,
            internal_code="WR001",
            min_quantity=1,
        )
        self.assertEqual(str(p), "Wrench")


class ProductListViewTests(TestCase):

    def setUp(self):
        self.client = Client()

    def test_product_list_view_all(self):
        c = Category.objects.create(name="Office")
        Product.objects.create(name="Printer", price=100, category=c, internal_code="P1", min_quantity=1)
        Product.objects.create(name="Paper", price=5, category=c, internal_code="P2", min_quantity=1)

        url = reverse("warehouse:product-list")
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context["products"]), 2)

    def test_product_create_requires_login(self):
        url = reverse("warehouse:product-create")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

    def test_product_edit_permission_denied(self):
        c = Category.objects.create(name="Office")
        p = Product.objects.create(name="Chair", price=50, category=c, internal_code="C1", min_quantity=1)

        user = User.objects.create_user(username="u", password="p")
        self.client.login(username="u", password="p")

        url = reverse("warehouse:product-edit", args=[p.id])
        response = self.client.get(url)

        self.assertEqual(response.status_code, 403)

class ProductFormTests(TestCase):

    def test_product_update_form_missing_required(self):
        c = Category.objects.create(name="Office")
        form = ProductUpdateForm(data={
            "price": 100,
            "category": c.id,
            "internal_code": "X1",
            "min_quantity": 1,
            "unit": Unit_choices.PIECE,
        })
        self.assertFalse(form.is_valid())
        self.assertIn("name", form.errors)

    def test_product_delete_form_disables_fields(self):
        c = Category.objects.create(name="Office")
        p = Product.objects.create(name="Item", price=10, category=c, internal_code="I1", min_quantity=1)

        form = ProductDeleteForm(instance=p)
        for field in form.fields.values():
            self.assertTrue(field.disabled)

    def test_product_form_widgets_have_css_class(self):
        form = ProductListForm()
        self.assertEqual(form.fields["name"].widget.attrs.get("class"), "form-control")
        self.assertEqual(form.fields["description"].widget.attrs.get("class"), "form-control")
