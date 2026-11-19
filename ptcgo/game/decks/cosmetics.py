"""A deck's coin, sleeve and deck box must be something the account can show.

A deck naming a cosmetic the account no longer owns cannot be resolved by the client,
and the whole deck goes dead with no error anywhere. Decks are rewritten to the default
cosmetic for each slot the account does not own, when they are saved and when they are
sent to the client.
"""
import logging

from ptcgo.game.attributes import AttrID, DefaultCosmetic

DEFAULTS = {
    AttrID.SELECTED_COIN.value: DefaultCosmetic.COIN.value,
    AttrID.SELECTED_SLEEVE.value: DefaultCosmetic.SLEEVE.value,
    AttrID.SELECTED_DECK_BOX.value: DefaultCosmetic.DECK_BOX.value,
}


def allowed_cosmetics(account_id):
    """Lower-case GUIDs a deck may name: owned collection rows, the defaults, and the
    deck boxes our deck products ship with (granted decks name them without the
    account owning a deck box row)."""
    from ptcgo.database import db_session, Collection
    from ptcgo.game.scripts.products import loader as product_loader
    with db_session() as session:
        owned = {row.archetype_id.lower() for row in session.query(Collection).filter(
            Collection.account_id == account_id,
            (Collection.tradable_count + Collection.nontradable_count) > 0)}
    shipped = {str(getattr(p, "deck_box", None) or "").lower() for p in product_loader.products}
    return owned | {v.lower() for v in DEFAULTS.values()} | (shipped - {""})


def fix_deck_cosmetics(deck_dict, allowed):
    """Rewrites unowned cosmetic slots in place; returns [(attr, old, new)] changes.
    Handles the attribute list the client sends and the dict form used while saving."""
    attributes = deck_dict.get("attributes")
    if isinstance(attributes, dict):
        entries = list(attributes.values())
    elif isinstance(attributes, list):
        entries = attributes
    else:
        return []
    changes = []
    for entry in entries:
        if not isinstance(entry, dict):
            continue
        try:
            name = int(entry.get("name"))
        except (TypeError, ValueError):
            continue
        default = DEFAULTS.get(name)
        if default is None:
            continue
        value = entry.get("value")
        if isinstance(value, str) and value.lower() in allowed:
            continue
        entry["value"] = default
        changes.append((name, value, default))
    if changes:
        logging.info("[Decks] deck %s named unowned cosmetics, reset to defaults: %s",
                     deck_dict.get("deckID"), changes)
    return changes
