"""Bundle products: one shop purchase that grants several things at once.

A bundle names archetype GUIDs (cards or other products, each granted once) and an
amount of Trainer Tokens credited to the wallet. It is typed as a pack so the shop files
it under Booster Packs, the only tab the client renders for a purchasable non-deck
product, but it is never put through the pack reveal: a purchase grants its contents
directly (see expand_bundles in ptcgo/game/models/product.py).
"""
from ptcgo.game.content.definitions import BoosterPackDef


class BundleDef(BoosterPackDef):
    def __init__(self, *, contents, tokens=0, once_per_account=False, **kwargs):
        super().__init__(**kwargs)
        if not contents and not tokens:
            raise ValueError("a bundle must grant something")
        if int(tokens) < 0:
            raise ValueError("bundle tokens cannot be negative")
        self.contents = [str(g).lower() for g in contents]
        self.tokens = int(tokens)
        # Enforced at purchase, atomically with the grant (economy_data.purchase_products).
        self.once_per_account = bool(once_per_account)
