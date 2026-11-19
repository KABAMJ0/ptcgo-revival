from ptcgo.game.card_effects.attacks_common import condition_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from ptcgo.game.card_effects.attacks_common import condition_attack, count_energy

async def hundred_foot_flames(ctx):
    """Discard the top card of your opponent's deck for each Fire Energy
    attached to this Pokémon."""
    count = count_energy("self", energy_type=PokemonTypes.FIRE)(ctx)
    if count > 0:
        await ctx.discard_cards(ctx.deck_top(count, player_id=ctx.opponent_id))

card = PokemonCardDef(
    guid="4fe8b0d5-b9aa-57f8-b96e-135b5e30dede",
    key="SWSH45SV",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Centiskorch.Name",
    display_name="Centiskorch",
    searchable_by=["Centiskorch", "Stage 1", "Centiskorch"],
    subtypes=["Stage 1"],
    collector_number=19,
    set_code="SWSH45SV",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Sizzlipede.Name",
    family_id=850,
    abilities=[
        Attack(
            title="Hundred Foot Flames",
            game_text="For each Fire Energy attached to this Pok\u00e9mon, discard the top card of your opponent's deck.",
            cost={PokemonTypes.FIRE: 1},
            effect=hundred_foot_flames,
        ),
        Attack(
            title="Searing Flame",
            game_text="Your opponent's Active Pok\u00e9mon is now Burned.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 3},
            damage=110,
            effect=condition_attack(SpecialConditions.BURNED),
        ),
    ],
)