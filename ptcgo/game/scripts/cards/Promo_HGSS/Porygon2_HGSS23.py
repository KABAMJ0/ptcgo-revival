from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, def_for, unimplemented
from ptcgo.game.card_effects.passives_common import retreat_cost_modifier

PORYGON_NAMES = ("Porygon", "Porygon2", "Porygon-Z")


def _porygon_line(pokemon, board) -> bool:
    definition = def_for(pokemon.archetype_id)
    return getattr(definition, "display_name", "") in PORYGON_NAMES
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import recoil_attack

card = PokemonCardDef(
    guid="e6999596-3cef-53f0-bb83-5ae1a1f085b9",
    key="Promo_HGSS",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Porygon2.Name",
    display_name="Porygon2",
    searchable_by=["Porygon2", "Stage 1", "Porygon2"],
    subtypes=["Stage 1"],
    collector_number=23,
    set_code="Promo_HGSS",
    rarity=Rarities.RarePromo,
    hp=80,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Porygon.Name",
    family_id=137,
    abilities=[
        Ability(
            title="Shortcut",
            game_text="The Retreat Cost for each Porygon, Porygon2, and Porygon-Z you have in play is Colorless less.",
            passive=retreat_cost_modifier(-1, pred=_porygon_line),
        ),
        Attack(
            title="Reckless Charge",
            game_text="Porygon2 does 10 damage to itself.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=50,
            effect=recoil_attack(10),
        ),
    ],
)