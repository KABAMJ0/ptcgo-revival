from ptcgo.game.data_utils import StadiumCardDef, unimplemented, Ability, Triggers
from ptcgo.game.attributes import AttrID, PokemonTypes, Rarities
from ptcgo.game.card_effects.pokemon import has_pokemon_subtype
from ptcgo.game.card_effects.support_common import trigger_counters


def _basic_non_water(pokemon, ctx) -> bool:
    """The printed scope: 1 of their Basic non-Water Pokemon.

    The body that stood here was `has_pokemon_subtype(p, "Basic") or True` --
    always true, and calling a name it never imported, so it raised on the first
    Energy attach AND would have put counters on every receiver."""
    if not has_pokemon_subtype(pokemon, "Basic"):
        return False
    types = pokemon.get_attribute(AttrID.POKEMON_TYPES) or []
    return PokemonTypes.WATER.value not in types


card = StadiumCardDef(
    guid="a662e600-bd33-50bd-9832-dac9d73d0729",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.CalamitousSnowyMountain.Name",
    display_name="Calamitous Snowy Mountain",
    searchable_by=["Calamitous Snowy Mountain", "Stadium"],
    subtypes=["Stadium"],
    collector_number=174,
    set_code="SV2",
    rarity=Rarities.Uncommon,
    ability=Ability(
        title="Calamitous Snowy Mountain",
        game_text="Whenever any player attaches an Energy card from their hand to 1 of their Basic non-Water Pok\u00e9mon, put 2 damage counters on that Pok\u00e9mon.",
        trigger=Triggers.ON_ENERGY_ATTACHED,
        effect=trigger_counters(2, _basic_non_water),
    )
)
