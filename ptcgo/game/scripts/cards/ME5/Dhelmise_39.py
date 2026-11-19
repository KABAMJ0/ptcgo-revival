from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import bonus_if
from ptcgo.game.data_utils import def_for


def _hide_n_sneak_in_discard(ctx) -> int:
    """Pokemon in your discard pile that print the Hide 'n' Sneak Ability."""
    count = 0
    for card in ctx.discard_pile():
        definition = def_for(card.archetype_id)
        if any(getattr(ability, "title", "") == "Hide 'n' Sneak"
               for ability in getattr(definition, "abilities", []) or []):
            count += 1
    return count


def _four_hide_n_sneak(ctx) -> bool:
    return _hide_n_sneak_in_discard(ctx) >= 4


card = PokemonCardDef(
    guid="71eb30d6-8ef0-5c0a-b729-83c221c406df",
    key="ME5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dhelmise.Name",
    display_name="Dhelmise",
    searchable_by=["Dhelmise", "Basic", "Dhelmise"],
    subtypes=["Basic"],
    collector_number=39,
    set_code="ME5",
    rarity=Rarities.Uncommon,
    hp=140,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=781,
    abilities=[
        Attack(
            title="Vengeful Anchor",
            game_text="If you have 4 or more Pok\u00e9mon that have the Hide 'n' Sneak Ability in your discard pile, this attack does 140 more damage.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=30,
            damage_operator="+",
            effect=bonus_if(_four_hide_n_sneak, 140),
        ),
    ],
)