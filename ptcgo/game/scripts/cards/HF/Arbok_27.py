from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import (
    bonus_if, count_discard, discard_random_from_hand,
)
from ptcgo.game.card_effects.passives_common import on_ko_from_attack
from ptcgo.game.card_effects.support_common import entity_name


def _jessie_and_james_in_discard(ctx) -> bool:
    return count_discard(
        "mine", lambda card: entity_name(card) == "Jessie & James")(ctx) > 0


async def _last_pattern(ctx):
    await discard_random_from_hand(ctx, ctx.opponent_id, 2)


card = PokemonCardDef(
    guid="f7d31cd5-1fef-5210-a9fa-36d6ffee2777",
    key="HF",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Arbok.Name",
    display_name="Arbok",
    searchable_by=["Arbok", "Stage 1", "Arbok"],
    subtypes=["Stage 1"],
    collector_number=27,
    set_code="HF",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Ekans.Name",
    family_id=23,
    abilities=[
        Ability(
            title="Last Pattern",
            game_text="If this Pok\u00e9mon is Knocked Out by damage from an opponent's attack, discard 2 random cards from your opponent's hand.",
            trigger=Triggers.ON_KNOCKED_OUT,
            effect=on_ko_from_attack(_last_pattern),
        ),
        Attack(
            title="Rocket Tail",
            game_text="If Jessie & James is in your discard pile, this attack does 80 more damage.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            damage_operator="+",
            effect=bonus_if(_jessie_and_james_in_discard, 80),
        ),
    ],
)
