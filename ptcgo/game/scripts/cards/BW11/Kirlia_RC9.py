from ptcgo.game.card_effects.attacks_common import flip_damage
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import count_energy


async def tiptoe_step(ctx):
    """Draw 1 for each Psychic Energy attached to this Pokemon."""
    count = count_energy("self", PokemonTypes.PSYCHIC)(ctx)
    if count > 0:
        await ctx.draw_cards(count)


card = PokemonCardDef(
    guid="463ccdb8-0dc8-5795-b62a-69f7cc343cc2",
    key="BW11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Kirlia.Name",
    display_name="Kirlia",
    searchable_by=["Kirlia", "Stage 1", "Kirlia"],
    subtypes=["Stage 1"],
    collector_number=1009,
    set_code="BW11",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Ralts.Name",
    family_id=280,
    abilities=[
        Attack(
            title="Tiptoe Step",
            game_text="Draw a card for each Psychic Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=tiptoe_step,
        ),
        Attack(
            title="Double Slap",
            game_text="Flip 2 coins. This attack does 20 damage times the number of heads.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="x",
            effect=flip_damage(coins=2, per_heads=20),
        ),
    ],
)