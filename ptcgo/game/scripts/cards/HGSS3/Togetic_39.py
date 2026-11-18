from ptcgo.game.card_effects.passives_common import apply_protection
from ptcgo.game.card_effects.attacks_common import flip_or_nothing
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

async def _fly_success(ctx):
    await ctx.deal_damage()
    await apply_protection(ctx, prevent=True, effects_too=True)

card = PokemonCardDef(
    guid="9de1a1f4-b7c5-5426-a5f6-2dd9abdaf391",
    key="HGSS3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Togetic.Name",
    display_name="Togetic",
    searchable_by=["Togetic", "Stage 1", "Togetic"],
    subtypes=["Stage 1"],
    collector_number=39,
    set_code="HGSS3",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Togepi.Name",
    family_id=175,
    abilities=[
        Attack(
            title="Chase Up",
            game_text="Search your deck for any 1 card and put it into your hand. Shuffle your deck afterward.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Fly",
            game_text="Flip a coin. If tails, this attack does nothing. If heads, prevent all effects of attacks, including damage done to Togetic during your opponent's next turn.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=flip_or_nothing(then=_fly_success),
        ),
    ],
)