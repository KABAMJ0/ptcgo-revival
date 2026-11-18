from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import bonus_if


def _three_or_fewer_in_deck(ctx):
    return len(ctx.deck()) <= 3

card = PokemonCardDef(
    guid="a8ee20d7-9f29-5581-bad3-3bf00a0f5102",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Excadrill.Name",
    display_name="Excadrill",
    searchable_by=["Excadrill", "Stage 1", "Excadrill"],
    subtypes=["Stage 1"],
    collector_number=115,
    set_code="SM12",
    rarity=Rarities.RareHolo,
    hp=140,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Drilbur.Name",
    family_id=529,
    abilities=[
        Attack(
            title="Eleventh Hour Tackle",
            game_text="If there are 3 or fewer cards in your deck, this attack does 150 more damage.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=30,
            damage_operator="+",
            effect=bonus_if(_three_or_fewer_in_deck, 150),
        ),
        Attack(
            title="Drill Bazooka",
            game_text="Discard the top 4 cards of your deck.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=120,
            effect=unimplemented,
        ),
    ],
)